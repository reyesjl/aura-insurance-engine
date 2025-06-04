# Use latest Node LTS image
FROM node:18

# Set working directory
WORKDIR /app

# Install deps separately to leverage Docker layer caching
COPY package*.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Expose Vite's dev server port
EXPOSE 5173

# Run Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]