# Use a smaller, more efficient image for the final runtime environment
FROM node:lts-alpine AS runtime

WORKDIR /app

# Copy the production build artifacts from the build stage
# COPY --from=build /app/build ./build

# Install serve (or your preferred static file server)
RUN npm install -g serve

# Expose the port your app will listen on
EXPOSE 8080

ENV HOST=0.0.0.0
ENV PORT=8080

# Run the production build
# CMD ["serve", "-s", "build"]
CMD ["npm", "run", "dev"]


