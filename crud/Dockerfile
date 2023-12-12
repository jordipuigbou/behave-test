FROM python:3.12.1-slim-bullseye
# Test
COPY ./requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

COPY ./backend.py /root/backend.py
COPY ./endpoints /root/endpoints
COPY ./endpoints_tests /root/endpoints_tests

WORKDIR /root

EXPOSE 8888
