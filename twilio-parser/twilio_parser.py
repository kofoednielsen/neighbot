from loguru import logger
import json
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="discord-parse")


def twilio_parse(hocus, pocus, cats, args_bytes: bytes):
    args = json.loads(args_bytes.decode("utf-8"))
    logger.info("Parsed twilio-parse job and published discord-parse job")
    sms_message = args['Body']
    sender = args['From']
    body = json.dumps((sender, sms_message)).encode("utf-8")
    channel.basic_publish(exchange="",
                          routing_key="discord-parse",
                          body=body)


channel.basic_consume("twilio-parse", twilio_parse)
channel.start_consuming()
