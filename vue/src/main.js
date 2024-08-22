import { createApp } from 'vue';
import App from './App.vue';
import './assets/global.css';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

//createApp(App).mount('#app');
library.add(fas)

const app = createApp(App)

app.use(ElementPlus)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
