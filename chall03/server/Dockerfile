FROM golang:latest

LABEL maintainer="Jordane Gengo <jordane@hive.fi>"
WORKDIR /app
COPY . .
RUN go build -o main .
EXPOSE 8080
CMD ["./main"]
