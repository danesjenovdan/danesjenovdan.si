# ---------------------------------- WARNING ----------------------------------
# This file is primarily for development use with docker-compose
# See Dockerfile in repository root for production and k8s use
# ---------------------------------- WARNING ----------------------------------
FROM node:26-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY postcss.config.js tailwind.config.js ./

CMD ["npm", "run", "build"]
