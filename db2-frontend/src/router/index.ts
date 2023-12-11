import { RouteRecordRaw, createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'
import ListBooks from '../views/ListBooks.vue'
import NewBook from '../views/NewBook.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/books/', component: ListBooks, name: 'ListBooks' },
  { path: '/books/new', component: NewBook, name: 'NewBook' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
