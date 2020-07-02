FROM python:3.8-alpine
RUN pip install pika==1.1.0 loguru==0.5.1
COPY ./discord_parser.py /discord_parser.py
CMD ["python", "discord_parser.py"]
