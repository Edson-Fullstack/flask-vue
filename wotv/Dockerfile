# Use the official Python image.
# curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
#alias python=python3
#which python3
#sudo ln -s /usr/bin/python3 /usr/bin/python
#source $HOME/.poetry/env
# https://hub.docker.com/_/python
#docker build .
FROM python:3.7

# Copy local code to the container image.
ENV APP_HOME /app

WORKDIR $APP_HOME
COPY . .

RUN chmod 444 app.py
RUN chmod 444 requirements.txt
# Install production dependencies.
RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
