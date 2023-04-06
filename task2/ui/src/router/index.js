import Vue from 'vue'
//导入路由
import Router from 'vue-router'
import Home from "../views/Home";
import First from "../views/First"
import Second from "../views/Second";
//使用路由
Vue.use(Router);

export default new Router({
  routes:[
    {
      path:'/',
      name:'Home',
      component:Home
    },
    {
      path:'/1',
      name:'First',
      component:First
    },
    {
      path:'/2',
      name:'Second',
      component:Second
    },

  ]
})
