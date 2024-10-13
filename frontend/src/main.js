import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  root: 'frontend', // Cambia 'frontend' si tu index.html está en otro directorio
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'proyectoweb-bmeqh6ftezb4cwh2.canadacentral-01.azurewebsites.net',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
