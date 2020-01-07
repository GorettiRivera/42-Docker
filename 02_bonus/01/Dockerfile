FROM golang:alpine as builder

RUN mkdir /build 

ADD . /build/

WORKDIR /build 

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-extldflags "-static"' -o main .

FROM scratch

COPY --from=builder /build/main /app/

WORKDIR /app

CMD ["./main"]


## ------ Usage --------
# docker build -t bonus01 .
# docker run -it bonus01

# reference: https://www.cloudreach.com/en/insights/blog/containerize-this-how-to-build-golang-dockerfiles/