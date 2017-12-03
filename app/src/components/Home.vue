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
            <li>python</li>
            <li>Linux</li>
            <li>生活</li>
            <li>游戏</li>
          </ul>
          <div class="list">
            <ul class="articles">
              <li>django 模型中的orm操作详细讲解以及数据库的查询优化方法</li>
              <li>b</li>
              <li>c</li>
              <li>d</li>
              <li>e</li>
              <li>f</li>
              <li>g</li>

            </ul>
          </div>
        </div>
      </div>
      <div class="content guide with-sidebar components-guide">
        <ul>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
          <li>111</li>
          <li>222</li>
          <li>333</li>
        </ul>
      </div>
      <div class="right-menu">
        <ul>

          <li><a href="#/article" target="_blank"><i class="el-icon-edit"></i></a></li>
          <li><i class="el-icon-caret-top" v-on:click="goTop"></i></li>
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
      input: ''
    }
  },
  components: {
    HeaderComponents, FooterComponents
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
  .right-menu ul li{
    list-style-type: none;
    position: relative;
    margin-left: -17px;
    margin-top: 20px;
  }
  .right-menu{
    height: 120px;
    width: 52px;
    position: fixed;
    top: 200px;
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
  }
  .sidebar-inner ul li{
    display: list-item;
    text-align: -webkit-match-parent;
  }
  @media screen and (max-width: 1300px){
  .content.with-sidebar {
    margin-left: 290px;
  }
  }
  @media screen and (max-width: 900px) {
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
