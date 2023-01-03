FROM ubuntu:20.04

RUN apt-get update -y && apt-get install gcc python wget -y
RUN wget https://go.dev/dl/go1.19.4.linux-amd64.tar.gz
RUN tar -C /tmp -xzf go1.19.4.linux-amd64.tar.gz 

COPY stackoverflow.go stackoverflow.go
COPY go.mod go.mod
RUN /tmp/go/bin/go build -o stackoverflow.so -buildmode=c-shared github.com/sjeandeaux/stackoverflow/go-how-to-deal-with-memory-leaks-while-returning-a-cstring
COPY stackoverflow.py stackoverflow.py

CMD ["python", "stackoverflow.py"]
