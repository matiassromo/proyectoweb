import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  build: {
    root: 'frontend',
    outDir: 'dist' // Esto es correcto
  },
});
