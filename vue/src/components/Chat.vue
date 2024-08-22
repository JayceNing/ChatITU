<template>
  <div class="font-set">
    <el-container>
      <el-aside class="side-bar" :width="sideWidth +'px'">
        <!-- 侧边栏内容 -->
        <div style="position:relative;text-align: right;">
          <font-awesome-icon style="margin: 5px; color: #e5f1fb" class="fa-2x" :icon="['fas', 'bars']" @click="collapse"/>
        </div>
      </el-aside>
      <el-container class="main-container">
        <el-main class="main-content">
          <!-- 主要内容区域 -->
          <!-- 对话栏 -->
          <div class="chat-container" ref="container">
            <div class="chat-messages">
                <div v-for="message in messages" :key="message.id" class="chat-message">
                    <div v-if="message.character==0" style="padding: 30px">
                        <div class="user-message">
                            <img src="../assets/logo2.jpg" style="width:50px;height: 50px; margin-right: 16px">
                            {{ message.content }}
                        </div>
                    </div>
                    <div v-if="message.character==1" style="background-color: #f0f4ff;padding: 30px">
                      <div class="assistant-message" style="display: block">
                          <div style="display: flex">
                            <img src="../assets/logo1.jpg" style="width:50px;height: 50px; margin-right: 16px">
                            <div class="markdown-body" style="background-color: #f0f4ff; text-align: left;" v-html="message.content"></div>
                          </div>
                          <p v-if="message.isTyping != 0"><span class="typing-cursor" style="margin-left: 80px;"></span></p>
                      </div>
                    </div>
                    <div v-if="message.character==2" style="background-color: #f0f4ff;padding: 30px">
                      <div v-if="useplugin" class="assistant-message" style="display: block">
                        <div style="display: flex">
                          <img src="../assets/itu.jpg" style="width:50px;height: 50px; margin-right: 16px">
                          <div class="markdown-body" style="background-color: #f0f4ff; text-align: left;" v-html="message.content"></div>
                        </div>
                        <br>
                        <div v-if="work_item_list.length > 0">
                          <el-table :data="work_item_list" style="width: 100%" height="300">
                            <el-table-column fixed prop="work_item" label="Work item" width="100" />
                            <el-table-column prop="question" label="Question" width="100" />
                            <el-table-column label="Subject/title" width="150" >
                            <template #default="scope">
                              <div>
                                <a :href="scope.row.url" target="_blank">{{ scope.row.title }}</a>
                              </div>
                            </template>
                            </el-table-column>
                            <el-table-column prop="timing" label="Timing" width="100" />
                            <el-table-column prop="study_group" label="Study group" width="100" />
                            <el-table-column prop="study_period" label="Study period"
                            width="100" />
                            <el-table-column prop="detail" label="detail" width="100">
                              <template #default="scope">
                                <el-button type="primary" style="width: 50px" @click="read_detail(scope.row.url)">详细</el-button>
                              </template>
                            </el-table-column>
                            <!-- <el-table-column prop="abstract_translate" label="Abstract translate" width="90">
                              <template #default="scope">
                                <el-button>
                                  <el-icon>
                                    <component :is="checkIcon" />
                                  </el-icon>
                                </el-button>
                              </template>
                            </el-table-column> -->
                          </el-table>
                          </br>
                          <br>
                          <el-button type="primary" @click="download_excel()">下载Excel</el-button>
                        </div>
                      </div>
                    </div>
                    <div v-if="message.character==3" style="background-color: #f0f4ff;padding: 30px">
                      <div class="assistant-message" style="display: block">
                          <div style="display: flex">
                            <img src="../assets/itu.jpg" style="width:50px;height: 50px; margin-right: 16px">
                            <div class="markdown-body" style="background-color: #f0f4ff; text-align: left;" v-html="message.content"></div>
                          </div>
                          <br>
                          <el-descriptions
                            :title="cur_detail.Subject_title"
                            direction="vertical"
                            :column="1"
                            :size="size"
                            border
                          >
                          <el-descriptions-item v-for="(value, key) in cur_detail" :label="key">
                            {{ value }}
                          </el-descriptions-item>
                          </el-descriptions>    
                      </div>
                    </div>

                </div>
            </div>
            <div style="height: 200px;"></div>
          </div>

          <!-- 输入栏 -->
          <div class="chat-input" >
            <el-input
                v-model="inputMessage"
                placeholder="请输入消息"
                @keyup.enter="sendMessage"
                size="large"
            >
              <template #prepend>
                  插件
                  <img v-if="useplugin==1" src="../assets/itu.jpg" style="width:auto;height: 30px;" @click="setplugin">
                  <img v-if="useplugin==0" src="../assets/itu2.jpg" style="width:auto;height: 30px;" @click="setplugin">
              </template>
              <template #suffix>
                  <el-icon v-if="iconState==0" style="font-size: large; padding: 5px;" @click="sendMessage"><promotion /></el-icon>
                  <el-icon v-if="iconState==1" style="font-size: large; color:white; background-color: seagreen; padding: 5px; border-radius: 20%" @click="sendMessage"><promotion /></el-icon>
              </template>
            </el-input>
          </div>
          <!-- 弹出框 -->
          <div v-if="popup>0" class="popup font-set">
            <div class="popup-content">
                <h2 style="margin-bottom: 80px">提示</h2>
                <div v-if="popup==11">
                    <h2 v-if="popup==11" style="font-size: 20px;color: black;margin-bottom: 80px">{{ popMsg }}</h2>
                    <el-button class="button" style="background-color: green;" text><h1 style="font-size: 20px;color: white;" @click="reverseplugin">确定</h1></el-button>
                </div>

                <el-button class="button" style="background-color: black;" text><h1 style="font-size: 20px;color: white;" @click="closepop">关闭</h1></el-button>
            </div>
          </div>

        </el-main>
      </el-container>
    </el-container>
  </div>

</template>

<script>
import axios from 'axios'
import showdown from 'showdown';

const converter = new showdown.Converter();

export default {
  name: 'Chat.vue',
  data() {
    return {
      sideWidth: '64', // 侧边栏宽度可以根据需要调整
      isCollapse: true,
      // sideWidth: '400', // 侧边栏宽度可以根据需要调整
      // isCollapse: false,
      inputMessage: "",
      messages: [],
      iconState: 1,
      popup: 0,
      popMsg: '',
      useplugin: 1,
      work_item_dict: {},
      work_item_list: [],
      explain_message: 0,
      isSparkClientClosed: false,  // 新增标志变量
      cur_detail: {},
    };
  },
  mounted() {
    this.adjustSidebarHeight();
    window.addEventListener('resize', this.adjustSidebarHeight);
  },
  updated() {
    this.adjustSidebarHeight();
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.adjustSidebarHeight);
  },
  methods: {
    adjustSidebarHeight() {
      // 获取父页面元素的高度，减去顶栏的高度
      // 这里假设父页面的容器类名为 'font-set'
      const parentElement = document.querySelector('.font-set');
      if (parentElement) {
        const parentHeight = parentElement.clientHeight;
        console.log(parentHeight);
        // 假设顶栏的高度为 60px
        const adjustedHeight = document.documentElement.clientHeight - parentHeight;
        console.log(adjustedHeight);
        // 设置子页面侧边栏的高度，假设侧边栏的类名为 'side-bar'
        const sidebarElement = this.$el.querySelector('.side-bar');
        const mainContainerElement = this.$el.querySelector('.main-container');
        if (sidebarElement) {
          sidebarElement.style.height = `${adjustedHeight}px`;
        }
        if (mainContainerElement) {
          mainContainerElement.style.height = `${adjustedHeight}px`;
        }
      }
    },

    closepop() {
      this.popup = 0
      // if (globalVariables.login == 0) {
      //     this.$emit('update-data', 3);
      // }
    },

    setplugin() {
      this.popup = 11
      if(this.useplugin == 0){
          this.popMsg = "ITU搜索未开启，是否开启？"
      }else{
          this.popMsg = "ITU搜索已开启，点击确认关闭"
      }
    },
    reverseplugin() {
      if(this.useplugin == 0){
          this.useplugin = 1
      }else{
          this.useplugin = 0
      }
      this.popup=0
    },

    collapse() { // 点击收缩按钮触发
      console.log(this.sideWidth);
      this.isCollapse = !this.isCollapse
      if (this.isCollapse) {
          this.sideWidth = 64
          this.logoTextShow = false
          this.sideView = 0
      } else {
        this.sideWidth = 400
          this.logoTextShow = true
          this.sideView = 1
      }
    },

    async spark_client(pre_prompt){
      this.isSparkClientClosed = false;
      const socket = new WebSocket("ws://localhost:8009/ws");
      const assistantReply = {
              id: Date.now(),
              content: '',
              isUser: false,
              character: 1,
              isTyping: 1
          };
      this.messages.push(assistantReply);
      //console.log(this.messages)
      var that = this
      console.log(that.messages)
      var message = '';
      if (that.useplugin == 1 && that.explain_message == 1){
        message = that.messages[that.messages.length-4].content + '。上面是用户的问题，请结合下面的额外信息，对用户问题进行解答。' + pre_prompt;
      } else {
        message = that.messages[that.messages.length-2].content + pre_prompt;
      }
      console.log(message)
      // var send_messages = [...that.messages]
      var send_messages = JSON.parse(JSON.stringify(that.messages));
      send_messages[that.messages.length-2].content = message
      // 仅保留最后两条
      // send_messages = send_messages.slice(-2)
      console.log("-------------------------------------")
      console.log(send_messages)

      // 当连接建立时
      socket.onopen = function(event) {
          console.log("WebSocket connection established.");
          socket.send(JSON.stringify(send_messages));
      };

      // 当从服务器接收到消息时
      socket.onmessage = function(event) {
          const message = event.data;
          console.log(message)
          that.messages[that.messages.length - 1].content = that.messages[that.messages.length - 1].content + message
      };

      // 当连接关闭时
      socket.onclose = function(event) {
          console.log("WebSocket connection closed.");
          that.messages[that.messages.length - 1].isTyping = 0
          that.inputMessage = ""; // 清空输入框
          that.isSparkClientClosed = true;
          that.messages[that.messages.length - 1].content = converter.makeHtml(that.messages[that.messages.length - 1].content)
          console.log(that.messages[that.messages.length - 1].content)
      };

    },
    // 使用插件时的几个函数：1.大模型提取关键词 2.获取work item列表 3.获取预提示信息
    async extract_key_words() {
      var pre_prompt = ' 以上是用户输入的问题，请判断是否需要在ITU搜索引擎进行检索。如果需要的话，请返回该问题检索项目对应的英文关键词或句子。回答的关键词或句子要包含在双引号里，比如，当用户问题是“请调研ITU下与相机相关的内容”时，回答“根据您的问题，将在ITU按照关键词《camera》进行检索”。如果不需要检索，直接回答用户的问题。'
      this.spark_client(pre_prompt)
    },

    async get_work_item_list(key_words) {
      let da = {
        "key_words": key_words,
        "x": ""
      };

      try {
        const response = await axios.post('http://localhost:8009/v1/get_work_item_list', da, {
          headers: {
            'Content-Type': 'application/json'
          },
        });
        console.log("get_work_item_list");
        console.log(response.data);

        const tableData = [];
        for (let i = 0; i < response.data.urls.length; i++) {
            const item = {
                url: response.data.urls[i],
                work_item: response.data.work_items[i],
                question: response.data.questions[i],
                title: response.data.titles[i],
                timing: response.data.timings[i],
                study_group: response.data.study_groups[i],
                study_period: response.data.study_periods[i]
            };
            tableData.push(item);
        }
        if (response.data.urls.length>0){
          this.messages[this.messages.length - 1].content = '以下是插件的检索结果：'
        } else {
          this.messages[this.messages.length - 1].content = '未检索到相关项目'
        }
        this.work_item_dict = response.data;
        this.work_item_list = tableData;
      } catch (error) {
        console.error(error);
      }
    },
    async read_detail(url) {
      let da = {
        "url": url,
        "x": ""
      };
      // 首先删除之前的 assistant 回复中为 3 的部分（即之前关于提案详细信息的描述）
      const characterValue = 3;
      const existingMessageIndex = this.messages.findIndex(message => message.character === characterValue);
      if (existingMessageIndex!== -1) {
          this.messages.splice(existingMessageIndex, 1);
      }
      // 将提案列表提到最前面
      const characterToFind = 2;
      const index = this.messages.findIndex(message => message.character === characterToFind);
      if (index!== -1) {
          const foundMessage = this.messages.splice(index, 1)[0];
          this.messages.push(foundMessage);
      }
      // 添加一个新的 assistant 回复，内容为指定提案的详细信息
      const assistantReply = {
              id: Date.now(),
              content: '',
              isUser: false,
              character: 3,
              isTyping: 1
          };
      this.messages.push(assistantReply);

      try {
        const response = await axios.post('http://localhost:8009/v1/read_programme_page', da, {
          headers: {
            'Content-Type': 'application/json'
          },
        });
        console.log("read_programme_page");
        console.log(response.data);
        console.log(response.data.data);
        this.cur_detail = response.data.data;

        if (response.data){
          this.messages[this.messages.length - 1].content = '以下是指定提案的详细信息：'
        } else {
          this.messages[this.messages.length - 1].content = '查看详细信息失败'
        }
        this.work_item_list.forEach(item => {
            if (item.url === url) {
                item.detail = response.data.data;
            }
        });
      } catch (error) {
        console.error(error);
      }
    },
    download_excel() {
      let da = {
        "urls": this.work_item_dict["urls"],
        "x": ""
      };
      axios.post('http://localhost:8009/v1/download_excel', da, {
        headers: {
          'Content-Type': 'application/json'
        },
        responseType: 'blob'
      }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        console.log(response.data);
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'work_item_list.xlsx');
        document.body.appendChild(link);
        link.click();
      });
    },
    async extractInfoFromAnswer(str) {
      const regex = /《([^《》]+)》/g;
      const matches = str.match(regex);
      if (matches) {
        return matches.map(match => match.slice(1, -1));
      }
      return [];
    },

    async pluginWorkflow() {
      await this.extract_key_words();
      // 等待标志变为 true 表示完成
      while (!this.isSparkClientClosed) {
        await new Promise(resolve => setTimeout(resolve, 100));  // 短暂等待并检查
      }
      var key_words = await this.extractInfoFromAnswer(this.messages[this.messages.length - 1].content);
      console.log(this.messages[this.messages.length - 1].content)
      console.log("key_words")
      console.log(key_words)
      if (key_words.length == 0) {
        this.pre_prompt = ''
        this.explain_message = 0
      } else {
        // 首先删除之前的 assistant 回复中为 2 的部分（即之前关于提案列表的描述）
        const characterToFind = 2;
        const index = this.messages.findIndex(message => message.character === characterToFind);
        if (index!== -1) {
            this.messages.splice(index, 1);
        }
        // 添加一个新的 assistant 回复
        const assistantReply = {
              id: Date.now(),
              content: '检索中，请稍候...',
              isUser: true,  // 这里要设置成 true，因为额外的信息作为prompt和用户问题一起输入大模型
              character: 2,
              isTyping: 1
            };
        this.messages.push(assistantReply);
        // 等待 get_work_item_list 执行完成
        await this.get_work_item_list(key_words[0]);
        // 获取并转换 titles 列表为字符串
        let pre_prompt = this.work_item_dict["titles"];
        this.pre_prompt = "ITU中检索" + key_words[0] + "得到的全部相关项目标题有：" + pre_prompt.join(", ");
        this.explain_message = 1
      }

    },

    sendMessage() {
        this.iconState = 0
        const message = {
            id: Date.now(),
            content: this.inputMessage,
            isUser: true,
            character: 0
        };
        this.messages.push(message);
        if (this.useplugin == 1){
          //key_words = extract_key_words(this.inputMessage)
          this.pluginWorkflow().then(() => {
            if (this.pre_prompt != ''){
              this.spark_client(this.pre_prompt)
            } 
          });
        }
        else{
            this.spark_client('')
        }
    },
  }
};
</script>

<style scoped>
.font-set {
  font-family: Arial, sans-serif;
  margin: 0;
}

.side-bar {
  height: 100vh;
  background-color: lightgray;
  box-shadow: 2px 0px 6px rgba(0,21,41,0.35);
  overflow-y: auto;
}

.main-container {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.main-content {
  flex-grow: 1;
  overflow-y: auto;
  padding: 10px;
}

.chat-input {
  position: absolute;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  margin-left: 24vw;
  height: 50px;
  width: 40vw;
  bottom: 16vh;
  display: flex;
}
.chat-container {
  border: 2px black;
  height: 86vh;
  overflow-y: auto;
}
.chat-messages {
  display: flex;
  flex-direction: column;
}
.user-message {
    display: flex;
    width: 50%;
    margin-left: 20%;
}
.assistant-message {
    display: flex;
    width: 50%;
    margin-left: 20%;
}

/* 弹窗 */
.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9999;
}

.popup-content {
  background-color: #fff;
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

/* 其他样式 */
</style>