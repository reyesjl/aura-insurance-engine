# Stage 1: Build the app
FROM node:18 AS builder

# Set working directory
WORKDIR /app

# Install deps separately to leverage Docker layer caching
COPY package*.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Build the app
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy built app from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Run Nginx
CMD ["nginx", "-g", "daemon off;"]