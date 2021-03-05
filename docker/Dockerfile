FROM ubuntu:18.04

LABEL maintainer="Denis Juma kwanusud@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3 python3-dev python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /kanairo-sms/requirements.txt

WORKDIR /kanairo-sms

RUN python3 -m pip install -U pip
RUN python3 -m pip install -U setuptools

RUN pip3 install -r requirements.txt

COPY . /kanairo-sms

EXPOSE 5000


CMD [ "python3", "manage.py", "db", "init" ]
CMD [ "python3", "manage.py", "db", "migrate" ]
CMD [ "python3", "manage.py", "db", "upgrade" ]
CMD [ "python3", "manage.py", "runserver" ]