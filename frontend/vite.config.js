import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/Chatbot_for_admissions/', // BẮT BUỘC THÊM DÒNG NÀY ĐỂ GITHUB PAGES NHẬN DIỆN
})