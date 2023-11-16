FROM python:3.10.13-slim-bullseye

COPY ./requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

COPY ./petstore /root/petstore
COPY ./test.py /root/test.py
