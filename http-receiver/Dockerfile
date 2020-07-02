FROM python:3.8-alpine
RUN pip install flask==1.1.2 pika==1.1.0 gunicorn==20.0.4 loguru==0.5.1
COPY ./http_receiver.py /http_receiver.py
CMD ["gunicorn", "http_receiver:app"]
