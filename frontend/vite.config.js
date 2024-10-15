import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({

  plugins: [vue()],
  build: {
    outDir: 'dist' // Generar los archivos en frontend/dist
  },
});
