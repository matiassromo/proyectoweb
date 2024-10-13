import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'https://proyectoweb-bmeqh6ftezb4cwh2.canadacentral-01.azurewebsites.net/', // Cambia esto a la URL de tu API en Azure
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
