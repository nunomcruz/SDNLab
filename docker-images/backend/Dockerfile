FROM alpine:latest
RUN apk add --update python3 py3-pip py3-flask py3-flask-cors
RUN apk add bash
COPY app.py /usr/src/app/
EXPOSE 5000
CMD python3 /usr/src/app/app.py &
