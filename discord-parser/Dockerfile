FROM python:3.8-alpine
RUN pip install pika==1.1.0 loguru==0.5.1
COPY ./discord-parser.py /discord-parser.py
CMD ["python", "discord-parser.py"]
