FROM python:3.12.5-slim-bullseye

COPY ./requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

COPY ./features /root/features

WORKDIR /root
