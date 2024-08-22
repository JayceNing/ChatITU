<template>

  <div class="font-set">
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
      style="background-color: white;"
      background-color="grey"
      text-color="black"
      active-text-color="black"
  >

      <nav style="margin-left: 10px;margin-top: 10px">
        <!-- <img src="./assets/logo1.png" style="width:50px;height: 50px;margin-right: 5px"> -->
        <h1 class="gradient-text">基于大模型的ITU调研辅助系统</h1>
      </nav>

      <el-menu-item index="1"><h1>ChatITU</h1></el-menu-item>

      <el-sub-menu index="2">
        <template #title><text><h1>个人资料</h1></text></template>
        <div v-if="login==0">
          <el-menu-item index="2-0"><h2>登录</h2></el-menu-item>
        </div>
        <div v-if="login==1">
          <el-menu-item index="2-1"><h2>个人信息</h2></el-menu-item>
          <el-menu-item index="2-2"><h2>退出登录</h2></el-menu-item>
        </div>
      </el-sub-menu>
    </el-menu>
  </div>

  <chat></chat>

  <footer>
    <!-- <p>&copy; 2023 BrainBase Future Tech Company. All rights reserved.</p> -->
  </footer>
</template>

<script>
import chat from './components/Chat.vue'
import { globalVariables } from './utils/globalVariables.js';


export default {
  name: 'Home',
  data() {
    return {
      currentPage: 0,
      login: 0,
    }
  },
  components: {
    chat
  },
  created() {


  },

  updated() {
    this.login = globalVariables.login

  },
  methods: {


  }
};

</script>

<style>
.font-set {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 0;
}


.gradient-text {
  background: linear-gradient(45deg,#000000, #484848, #b9b9b9);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  height: 100%;
}


nav {
  display: flex;
  margin: 0 auto;
  left: 0px;
}

nav h1 {
  margin-top: 4px;
  font-size: 28px;
  margin-right: 10px;
  color: #ffffff;
}

/*菜单字体*/
/* 修改菜单项的字体 */
.el-menu {
  border: 0px;
}
.el-menu-item {
  font-family: Arial, sans-serif;
  font-weight: bold;
}

.el-sub-menu {
  font-family: Arial, sans-serif;
  font-weight: bold;
}

/*页脚*/
footer {
  background-color: white;
  position: relative;
  text-align: center;
  width: 100%;
  bottom: 0px;
  color: #fff;
}
footer p {
  font-size: 16px;
  color: black;
}
</style>
