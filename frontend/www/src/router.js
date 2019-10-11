import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'
import Top from './components/Top'
import Index from './components/ddd_sample/Index'
import Create from './components/ddd_sample/Create'
// import { brotliCompress } from 'zlib'

Vue.use(Router)


export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: Top
    },
    {
      path: '/dddSample',
      component: Index
    },
    {
      path: '/dddSample/create',
      component: Create
    }
  ]
})
