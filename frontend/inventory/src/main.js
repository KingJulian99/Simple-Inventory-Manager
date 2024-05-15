import { createApp } from 'vue'
import Base from './Base.vue'
import router from './router'
import './index.css'

const app = createApp(Base)

app.use(router)

app.mount('#app')
