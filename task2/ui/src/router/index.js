import Vue from 'vue'
//导入路由
import Router from 'vue-router'
import Home from "../views/Home";
//使用路由
Vue.use(Router);

export default new Router({
  routes:[
    {
      path:'/',
      name:'Home',
      component:Home
    },


  ]
})
