import { createRouter, createWebHistory } from 'vue-router'

import Inventory from '../views/Inventory.vue'
import InventoryDetail from '@/views/InventoryDetail.vue'
import Categories from '../views/Categories.vue'
import CategoryDetail from '../views/CategoryDetail.vue'
import Suppliers from '../views/Suppliers.vue'
import SupplierDetail from '@/views/SupplierDetail.vue'
import Products from '../views/Products.vue'
import ProductDetail from '../views/ProductDetail.vue'
import Management from '../views/Management.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/management',
      name: 'management',
      component: Management
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: Inventory
    },
    {
      path: '/inventory/:id',
      name: 'inventoryDetail',
      component: InventoryDetail
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
    {
      path: '/products/:id',
      name: 'productDetail',
      component: ProductDetail
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
