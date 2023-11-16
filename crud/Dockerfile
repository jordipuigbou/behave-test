FROM python:3.12.0-slim-bullseye

COPY ./requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

COPY ./backend.py /root/backend.py
COPY ./endpoints /root/endpoints
WORKDIR /root

EXPOSE 8888