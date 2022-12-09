import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
      path: '/',
      name: 'Auctions',
      component: () => import('../views/Auctions.vue')
    },
    // {
    //   path: '/auctions',
    //   name: 'Auctions',
    //   //component: () => import('../views/Auctions.vue')
    // },
    {
      path: '/search',
      name: 'Search',
      component: () => import('../views/Search.vue')
    },
    {
      path: '/items/:pid',
      name: 'Items',
      component: () => import('../views/Items.vue'),
      props: true 
    },
    {
      path: '/profile',
      name: 'Profile',
      component: () => import('../views/Profile.vue')
    },
    {
      path: '/logout',
      name: 'Logout',
      component: () => import('../views/Logout.vue')
    },
  ]

const router = createRouter({
    // history: createWebHistory(process.env.BASE_URL),
    history: createWebHistory(),
    routes
})

export default router