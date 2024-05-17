import { createRouter, createWebHistory } from 'vue-router'

import Inventory from '../views/Inventory.vue'
import Categories from '../views/Categories.vue'
import CategoryDetail from '../views/CategoryDetail.vue'
import Suppliers from '../views/Suppliers.vue'
import Products from '../views/Products.vue'
import SupplierDetail from '@/views/SupplierDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/inventory',
      name: 'inventory',
      component: Inventory
    },
    {
      path: '/categories',
      name: 'categories',
      component: Categories
    },
    {
      path: '/categories/:id',
      name: 'categoryDetail',
      component: CategoryDetail
    },
    {
      path: '/suppliers',
      name: 'suppliers',
      component: Suppliers
    },
    {
      path: '/suppliers/:id',
      name: 'supplierDetail',
      component: SupplierDetail
    },
    {
      path: '/products',
      name: 'products',
      component: Products
    },
  ]
})

router.beforeEach((to, from, next) => {
  if (to.path === '/') {
    next('/inventory');
  } else {
    next();
  }
});

export default router
