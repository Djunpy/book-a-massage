FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps  \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
RUN apk del .tmp-build-deps
RUN mkdir /app
COPY ./django_website  /app/
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt


