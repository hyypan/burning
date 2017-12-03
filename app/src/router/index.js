import Vue from 'vue'
import Router from 'vue-router'
import Article from '@/components/Article'
import Home from '@/components/Home'
import NotFound from '@/components/common/NotFound'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/article/',
      name: 'Article',
      component: Article
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
