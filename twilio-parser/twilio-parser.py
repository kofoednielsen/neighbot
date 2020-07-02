import pika


connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="discord-parse")


def twilio_parse(args):
    sms_message = args['Body']
    sender = args['From']
    channel.basic_publish(exchange="",
                          routing_key="discord-parse",
                          body=(sender, sms_message))


channel.basic_consume("twilio-parse", twilio_parse)
channel.start_consuming()
