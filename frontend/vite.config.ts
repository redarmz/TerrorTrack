import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import Components from 'unplugin-vue-components/vite';
import IconsResolver from 'unplugin-icons/resolver';
import path from 'path';

export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [
        IconsResolver(),
      ],
    }),
  ],
  define: {
    __VUE_PROD_DEVTOOLS__: false,
    __VUE_OPTIONS_API__: false,
  },
  resolve: {
    alias: [
      { find: '@/', replacement: '/src/' },
      {
        find: 'vue',
        replacement: path.resolve('./node_modules/vue'),
      },
    ],
  },
  server: {
    proxy: {
      '/api': 'http://127.0.0.1:8000',  // Utilisation explicite d'IPv4
    },
  },
});

