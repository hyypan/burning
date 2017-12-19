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
          <li v-for="item in items" class="otherLi-o">{{item}}</li>
          </ul>
        </div>
      </div>
      <div class="content guide with-sidebar components-guide">
        <div class="list">
            <ul class="articles">
              <li v-for="item in Articles" class="otherLi-h">
                <div class="activeArticles" @click="articleDetail(item)">
                <div :value="item">{{item.title}}</div>
                <div class="a-text">{{item.content}}</div>
                </div>
                <ul class="a-belongs">
                  <li><i class="el-icon-view">
                  </i>{{item.belongs.views}}</li>
                  <li><i class="el-icon-time">
                  </i>{{item.belongs.create_time}}</li>
                  <li><i class="el-icon-edit">
                  </i>{{item.belongs.comments_count}}</li>
                  <li><i class="el-icon-star-off">
                  </i>{{item.belongs.loves}}</li>

                </ul>
              </li>
            </ul>
        </div>
      <div id="p1" class="block">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          layout="prev, pager, next"
          background
          :total="200">
        </el-pagination>
      </div>
      <div id="p2" class="block">
        <el-pagination class="aaa"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page.sync="currentPage3"
          background
          :page-size="4"
          layout=" total ,prev, pager, next, jumper"
          :total="1000">
        </el-pagination>
        </div>
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
      currentPage3: 4,
      Articles: [
        {
          'title': 'Django建模',
          'content': '在网站上动态渲染任意 HTML 是非常危险的，因为容易导致 XSS 攻击。只在可信内容上使用 v-html，永不用在用户提交的内容上。在单文件组件里，scoped 的样式不会应用在 v-html 内部，因为那部分 HTML 没有被 Vue 的模板编译器处理。如果你希望针对 v-html 的内容设置带作用域的 CSS，你可以替换为 CSS Modules 或用一个额外的全局 <style> 元素手动设置类似 BEM 的作用域策略。',
          'belongs': {'views': 10, 'create_time': '2017-11-11', 'comments': 3, 'loves': 2}},
        {'title': 'Mysql数据库讲解',
          'content': 'baabfsfnsn',
          'belongs': {'views': 10, 'create_time': '2017-11-11', 'comments': 3, 'loves': 2}},
        {'title': 'Linux初识',
          'content': 'baabfsfnsn',
          'belongs': {'views': 10, 'create_time': '2017-11-11', 'comments': 3, 'loves': 2}}]

    }
  },
  components: {
    HeaderComponents, FooterComponents
  },
  mounted: function () {
    $('.otherLi-o').eq(0).addClass('bottomLine')
    $('.otherLi-o').hover(function () {
      $(this).addClass('bottomLine').siblings().removeClass('bottomLine')
    })
  },
  methods: {
    articleDetail: function (item) {
      console.log(item)
    },
    goTop: function () {
      document.body.scrollTop = document.documentElement.scrollTop = 0
    },
    handleSizeChange (val) {
      console.log(`每页 ${val} 条`)
    },
    handleCurrentChange (val) {
      console.log(`当前页: ${val}`)
    }
  },
  created: function () {
    let that = this
    $.get('/api/v1/website/articles/', function (res) {
      that.Articles = res['results']['data']
      console.log('fdsfs', that.Articles)
    }).error(function (error) {
      console.log(error)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .otherLi-h{
    border-bottom: 1px solid rgba(0,0,0,0.2);
  }
  .a-text{
    padding-top: 10px;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
  }

  .articles{
    padding-top: 10px;
    padding-left: 3px;

  }
  .a-belongs{
    margin-left: -42px;
  }
  .a-belongs li{
    display: inline-block !important;
    list-style-type: none;
    padding: 5px;
  }
  #p1{
    display: none;
  }

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
    bottom: 75px;
    right: 5px;
    z-index: 2;
    -webkit-box-shadow: 0 0 10px rgba(0,0,0,0.2);
    box-shadow: 0 0 10px rgba(0,0,0,0.2);
    background: #f9f9f9;

  }
  .content{
    position: relative;
    padding: 2.2em 0;
    max-width: 800px;
    margin: 0 auto;
  }
  .mobile-list{
    display: none;
  }
  /*.home {*/
  /*padding-top: 61px;*/
  /*}*/
  #main{
    position: relative;
    z-index: 1;
    /*padding: 0 60px 30px;*/
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
    display: none;
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
    list-style-type: none;

  }
  @media screen and (max-width: 1300px){
  .content.with-sidebar {
    /*margin-left: 290px;*/
  }
  }
  @media screen and (max-width: 900px) {
    .aaa{

    }
    #p1{
      display: block;
    }
    #p2{
      display: none;
    }
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
      display: block;
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
    .mobile-list li{
      margin-top: 10px;

    }
    .open {
      -webkit-transform: translate(0, 0);
      transform: translate(0, 0);
    }
  }
</style>
