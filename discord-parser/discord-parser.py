import pika


connection = pika.BlockingConnection(pika.ConnectionParameters("amqp"))
channel = connection.channel()
channel.queue_declare(queue="discord-bot")


def discord_parse(needed_stuff):
    channel.basic_publish(exchange="",
                          routing_key="discord-parse",
                          body=f"**{needed_stuff[0]}** {needed_stuff[1]}")


channel.basic_consume("discord-parse", discord_parse)
channel.start_consuming()
