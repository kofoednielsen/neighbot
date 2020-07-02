from flask import Flask, request
from loguru import logger
import pika


app = Flask(__name__)


connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="twilio-parse")


@app.route("/sms")
def sms():
    """ Receive http request and job for parsing """
    logger.info('Received sms, making twilio-parse job')
    channel.basic_publish(exchange="",
                          routing_key="twilio-parse",
                          body=request.args)
    return "thank you", 200
