WORKDIR /app
COPY docker-compose.yml
RUN docker-compose up