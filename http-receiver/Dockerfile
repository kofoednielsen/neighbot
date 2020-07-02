FROM python:3.8-alpine


RUN pip install flask==1.1.2
RUN pip install gunicorn==20.0.4

ENV FLASK_APP = http-receiver.py

CMD ["gunicorn", "http-receiver:app"]

