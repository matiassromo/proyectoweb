import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  //root: 'frontend', // Asegúrate de que esto apunte a la carpeta correcta
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'https://proyectoweb-bmeqh6ftezb4cwh2.canadacentral-01.azurewebsites.net',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
});
