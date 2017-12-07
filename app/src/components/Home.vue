<template>
  <div class="home">
    <header-components></header-components>
    <div id="main">
      <div class="sidebar">
        <div class="sidebar-inner">
          <ul class="mobile-list">
            <li>
              <el-input v-model="input" placeholder="请输入内容"></el-input>
            </li>
          <li v-for="item in items" class="otherLi-h">{{item}}</li>
          </ul>
          <div class="list">
            <ul class="articles">
          <li v-for="item in Articles" class="otherLi-h">{{item}}</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="content guide with-sidebar components-guide">
组件 (Component) 是 Vue.js 最强大的功能之一。组件可以扩展 HTML 元素，封装可重用的代码。在较高层面上，组件是自定义元素，Vue.js
 的编译器为它添加特殊功能。在有些情况下，组件也可以表现为用 is 特性进行了扩展的原生 HTML 元素。
所有的 Vue 组件同时也都是 Vue 的实例，所以可接受相同的选项对象 (除了一些根级特有的选项) 并提供相同的生命周期钩子。
      </div>
      <div class="right-menu">
        <ul>

          <li><a href="#/article" target="_blank"><i class="el-icon-edit-outline"></i></a></li>
          <li><i class="el-icon-share"></i></li>
          <li><i class="el-icon-setting"></i></li>
          <li><i class="el-icon-arrow-up" v-on:click="goTop"></i></li>
        </ul>
      </div>
    </div>
    <!--<footer-components></footer-components>-->
  </div>
</template>
<script>
import HeaderComponents from './common/header'
import FooterComponents from './common/footer'

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      input: '',
      items: ['Vue', 'Python', 'Linux', '生活', '游戏'],
      Articles: ['Django建模', 'Mysql数据库讲解', 'Linux初识', 'Vue的初步学习', '运维之路', 'sql优化的n种方法']

    }
  },
  components: {
    HeaderComponents, FooterComponents
  },
  mounted: function () {
    $('.otherLi-h').eq(0).addClass('bottomLine')
    $('.otherLi-h').hover(function () {
      $(this).addClass('bottomLine').siblings().removeClass('bottomLine')
    })
  },
  methods: {
    goTop: function () {
      document.body.scrollTop = document.documentElement.scrollTop = 0
    }
  },
  created: function () {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .mobile-list li{
    display: list-item;

  }
  .bottomLine{
    border-bottom: 2px solid #22de64;

  }
  .right-menu ul li{
    list-style-type: none;
    position: relative;
    margin-left: -22px;
    margin-top: 20px;
    text-decoration:none;
    color:#333;
  }
  i{
    color: black;
  }
  .right-menu{
    width: 52px;
    position: fixed;
    bottom: 10px;
    right: 29px;
    z-index: 2;
    -webkit-box-shadow: 0 0 10px rgba(0,0,0,0.2);
    box-shadow: 0 0 10px rgba(0,0,0,0.2);
    background: #f9f9f9;

  }
  .content{
    position: relative;
    padding: 2.2em 0;
    max-width: 600px;
    margin: 0 auto;
    padding-left: 50px;
  }
  .mobile-list{
    display: none;
  }
  .home {
  padding-top: 61px;
  }
  #main{
    position: relative;
    z-index: 1;
    padding: 0 60px 30px;
    overflow-x: hidden;
    height: 100%;
  }
  .sidebar{
    position: fixed;
    z-index: 10;
    top: 61px;
    left: 0;
    bottom: 0;
    overflow-x: hidden;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
    -ms-overflow-style: none;
  }
  .sidebar .sidebar-inner{
    width: 260px;
    padding: 40px 20px 60px 60px;
  }
  .sidebar-inner ul{
    list-style-type: none;
    margin: 0;
    line-height: 1.5em;
    padding-left: 1em;
    margin-bottom: 40px;

  }
  .articles  li{
    display: list-item;
    text-align: -webkit-match-parent;
    margin-top: 7px;

  }
  @media screen and (max-width: 1300px){
  .content.with-sidebar {
    margin-left: 290px;
  }
  }
  @media screen and (max-width: 900px) {
    .content.with-sidebar {
      margin: auto;
    }
    .content{
      padding-left: 0;
      height: 100%;
    }
    .sidebar{
      box-sizing: border-box;
      box-shadow: 0 0 10px rgba(0,0,0,0.2);
      padding: 0 10px 10px 0;
      -webkit-box-sizing: border-box;
      -webkit-box-shadow: 0 0 10px rgba(0,0,0,0.2);
      margin-left: -47px;
      margin-top: -22px;
      background: #f9f9f9;
      transition: all 0.4s cubic-bezier(0.4, 0, 0, 1);
      -webkit-transform: translate(-280px, 0);
      transform: translate(-280px, 0);
    }
    .sidebar-inner{
      padding: 50px 10px 10px 20px;
      box-sizing: border-box;
    }
    .home{
      padding-top: 0;
      height: 100%;
    }
    .mobile-list{
      display: block;
    }
    .open {
      -webkit-transform: translate(0, 0);
      transform: translate(0, 0);
    }
  }
</style>
