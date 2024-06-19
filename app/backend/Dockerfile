FROM python:3.10-slim-bullseye

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    python3 \
    python3-pip
RUN pip3 install --upgrade pip==23.3.1 \
    && pip3 install setuptools

# set working directory
WORKDIR /app

COPY requirements.txt .
COPY ./app .

# for flask web server
EXPOSE 8081

# install required libraries
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# This is the runtime command for the container
CMD ["fastapi", "run", "src", "--port", "8081"]
