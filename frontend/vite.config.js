import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  root: 'dist', // Ajusta esta línea si `index.html` está en `src`
  server: {
    proxy: {
      '/api': {
        target: 'https://proyectoweb-bmeqh6ftezb4cwh2.canadacentral-01.azurewebsites.net/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
