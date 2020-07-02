FROM python:3.8-alpine


RUN pip install flask==1.1.2
RUN pip install pika==1.1.0
RUN pip install gunicorn==20.0.4
RUN pip install loguru==0.5.1

ENV FLASK_APP = http-receiver.py

CMD ["gunicorn", "http-receiver:app"]

