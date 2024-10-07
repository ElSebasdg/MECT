FROM golang:1.21 AS build

# Set working directory
WORKDIR /app

# Install dependencies
COPY go.mod go.sum ./
RUN go mod download

# Copy source
COPY *.go ./


# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /mqtt_influx_bridge

# Run
CMD ["/mqtt_influx_bridge"]

FROM gcr.io/distroless/base-debian11 AS release

WORKDIR /

COPY --from=build /mqtt_influx_bridge /mqtt_influx_bridge

CMD ["/mqtt_influx_bridge"]