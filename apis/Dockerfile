FROM python:3.12.3-slim-bullseye

COPY ./requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

COPY ./petstore /root/petstore
COPY ./test.py /root/test.py
COPY ./pytest.ini /root/pytest.ini

RUN mkdir -p /root/_output/reports
