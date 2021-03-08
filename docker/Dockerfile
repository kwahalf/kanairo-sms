FROM python:3.6.9-slim-buster

LABEL maintainer="Denis Juma kwanusud@gmail.com"

ENV BUILD_DEPS="build-essential" \
    APP_DEPS="curl libpq-dev"

COPY ./requirements.txt /kanairo-sms/requirements.txt

WORKDIR /kanairo-sms

RUN apt-get update \
  && apt-get install -y ${BUILD_DEPS} ${APP_DEPS} --no-install-recommends \
  && pip install -r requirements.txt --compile --no-cache-dir \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/doc && rm -rf /usr/share/man \
  && apt-get purge -y --auto-remove ${BUILD_DEPS} \
  && apt-get clean


COPY . /kanairo-sms


EXPOSE 5000

WORKDIR /kanairo-sms

RUN chmod u+x entry_point.sh
RUN chmod u+x celery_entrypoint.sh
CMD ["./entry_point.sh"]
