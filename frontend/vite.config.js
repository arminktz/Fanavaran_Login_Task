import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite' // حتما باید این خط بالا باشد

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
})