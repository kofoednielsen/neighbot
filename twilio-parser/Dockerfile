FROM python:3.8-alpine
RUN pip install pika==1.1.0
COPY ./twilio_parser.py /twilio_parser.py
CMD ["python", "twilio_parser.py"]
