# Build stage
FROM rust:latest AS builder

WORKDIR /app

# accept the build argument
ARG DATABASE_URL

ENV DATABASE_URL=$DATABASE_URL

COPY . . 

RUN cargo build --release

# Production stage
FROM debian:latest

WORKDIR /usr/local/bin

COPY --from=builder /app/target/release/troti_api .

CMD ["./troti_api"]