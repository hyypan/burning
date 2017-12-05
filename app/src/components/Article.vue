<template>
  <div class="article">
    <select v-model="category">
      <option value="Python">Python</option>
      <option value="Linux">Linux</option>
      <option value="Linux">生活</option>
      <option value="Linux">游戏</option>
    </select>
    <quill-editor v-model="articles"></quill-editor>
    <el-button type="info" plain>发布</el-button>
  </div>
</template>

<script>
  import { quillEditor } from 'vue-quill-editor'

  export default {
    name: 'HelloWorld',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App',
        articles: '',
        options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        category: 'Python'
      }
    },
    watch: {
      'articles': function (a) {
        console.log(a)
      }
    },
    components: {
      quillEditor
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
