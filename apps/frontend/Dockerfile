# Dockerfile for frontend Next.js application
FROM node:18-alpine AS deps
WORKDIR /app

# Install dependencies
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install --frozen-lockfile

# Build the application
FROM node:18-alpine AS builder
WORKDIR /app
#RUN npm install -g pnpm
COPY . .
RUN pnpm build

# Production image
FROM node:18-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production

# Copy built files and dependencies
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules

# Expose app port and start
EXPOSE 3000
CMD ["pnpm", "start"]
