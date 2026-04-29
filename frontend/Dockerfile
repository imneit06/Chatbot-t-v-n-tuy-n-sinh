# Sử dụng môi trường Node.js siêu nhẹ
FROM node:20-slim

WORKDIR /app

# Copy file cấu hình và cài đặt thư viện
COPY package.json package-lock.json* ./
RUN npm install

# Copy toàn bộ code Frontend vào
COPY . .

# Mở cổng 5173
EXPOSE 5173

# Khởi chạy Vite và cho phép truy cập từ mạng bên ngoài (host)
CMD ["npm", "run", "dev", "--", "--host"]