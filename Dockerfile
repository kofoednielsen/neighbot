FROM python:3.8

# Install pipenv
RUN pip install pipenv

# install python deps
RUN mkdir /tmp/deps
COPY ./Pipfile /tmp/deps/Pipfile
COPY ./Pipfile.lock /tmp/deps/Pipfile.lock
WORKDIR /tmp/deps
RUN pipenv install --deploy --system


COPY ./neighbot /app
WORKDIR /app

# -k argument fixes Quart problem
CMD hypercorn --bind 0.0.0.0:80 bot:app
