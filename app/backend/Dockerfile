FROM python:3.12
#-slim-bullseye

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    python3 \
    python3-pip 
    #\
    #gcc \
    #postgresql
RUN pip3 install --upgrade pip==23.3.1 \
    && pip3 install setuptools

# set working directory
WORKDIR /backend

COPY requirements.txt .

# install required libraries
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app

# for flask web server
EXPOSE 8081

# This is the runtime command for the container
#CMD ["fastapi", "run", "app", "--port", "8081"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]
