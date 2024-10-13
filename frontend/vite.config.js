import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  // Eliminar la línea root si causa problemas al ejecutar en modo dev
  // root: 'frontend', 
  build: {
    outDir: 'dist', // Este es el directorio donde se generará el build
    emptyOutDir: true // Esto asegurará que se vacíe la carpeta antes de construir
  },
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
