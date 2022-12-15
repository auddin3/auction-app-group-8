import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
      path: '/',
      name: 'Auctions',
      component: () => import('../views/Auctions.vue')
    },
    {
      path: '/search',
      name: 'Search',
      component: () => import('../views/Inventory.vue')
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
  ]

const router = createRouter({
    // history: createWebHistory(process.env.BASE_URL),
    history: createWebHistory(),
    routes
})

export default router