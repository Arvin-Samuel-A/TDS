# Use a base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN npm install

# Expose the application port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]

