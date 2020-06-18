FROM python:3.8

# install python deps
RUN mkdir /tmp/deps
COPY ./requirements.txt /tmp/deps/requirements.txt
WORKDIR /tmp/deps
RUN pip install -r requirements.txt


COPY ./neighbot /app
WORKDIR /app

# -k argument fixes Quart problem
CMD python3 bot.py

