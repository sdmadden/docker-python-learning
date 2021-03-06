FROM ubuntu:20.04
LABEL maintainer="sdmadden"

RUN apt-get update -y && apt-get install -y python3-pip python-dev

EXPOSE 5000

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

ENTRYPOINT flask run --host=0.0.0.0
