<template>
  <div>
    <div id="mobile-bar">
      <span v-on:click="changeSide"><i class="el-icon-success"></i></span>
      <a class="log" href="/"></a>
    </div>
    <div id="head">
      <a id="log" href="/">
        <img src="../../assets/logo.png"/>
        <span>Burning</span>
      </a>
      <ul id="nav">
        <li>
          <el-input v-model="input" placeholder="请输入内容"></el-input>
        </li>
        <li>python</li>
        <li>Linux</li>
        <li>生活</li>
        <li>游戏</li>
      </ul>
    </div>
  </div>

</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      input: 0,
      open: false
    }
  },
  methods: {
    changeSide () {
      if (this.open) {
        $('.sidebar').removeClass('open')
        this.open = false
      } else {
        console.log('ss')
        $('.sidebar').addClass('open')
        this.open = true
      }
    }
  },
  created: function () {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #mobile-bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 40px;
    background-color: #fff;
    z-index: 9;
    display: none;
    box-shadow: 0 0 2px rgba(0,0,0,0.25);
}
  #mobile-bar .log{
    position: absolute;
    width: 30px;
    height: 30px;
    background: url("../../assets/logo.png") center center no-repeat;
    top: 5px;
    left: 50%;
    margin-left: -15px;
    background-size: 30px;
  }

  a{
    text-decoration:none;
  }
  #log{
    display: inline-block;
    font-size: 1.5em;
    line-height: 40px;
    color: #2c3e50;
    font-family: "Dosis", "Source Sans Pro", "Helvetica Neue", Arial, sans-serif;
    font-weight: 500;
  }
  #log img{
    vertical-align: middle;
    margin-right: 6px;
    width: 40px;
    height: 40px;
  }
  #head {
    position: fixed;
    width:100%;
    top:0;
    left:0;
    box-shadow: 0 0 1px rgba(0,0,0,0.25);
    transition: background-color 0.3s ease-in-out;
    background-color: #fff;
    height: 40px;
    padding: 10px 60px;
    z-index: 2;
  }
  #nav{
    list-style-type: none;
    margin: 0;
    padding: 0;
    position: fixed;
    right: 30px;
    top: 10px;
    height: 40px;
    line-height: 40px;
  }
  #nav li{
    display: inline-block;
    position: relative;
    margin: 0 0.6em;
  }
  @media screen and (max-width: 900px) {
    #nav li{
      display: block;
    }
    .el-input{
      width: 25%;
    }
    #mobile-bar{
      display: block;
    }
    #head{
      display: none;
    }
  }
</style>
