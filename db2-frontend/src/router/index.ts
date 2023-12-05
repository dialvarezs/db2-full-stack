import { RouteRecordRaw, createRouter, createWebHistory } from "vue-router";
import Home from '../views/Home.vue'
import NewBook from '../views/NewBook.vue'

const routes: RouteRecordRaw[] = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/new-book', component: NewBook, name: 'NewBook' },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router