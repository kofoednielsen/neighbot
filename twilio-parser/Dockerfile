FROM python:3.8-alpine
RUN pip install pika==1.1.0
COPY ./twilio-parser.py /twilio-parser.py
CMD ["python", "twilio-parser.py"]

