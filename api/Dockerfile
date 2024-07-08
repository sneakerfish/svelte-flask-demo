FROM python:3.10.13-alpine3.19

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP manage.py

# install dependencies
RUN apk add --no-cache mariadb-dev build-base
RUN apk update && apk add --no-cache bash \
        alsa-lib \
        cairo \
        cups-libs \
        dbus-libs \
        eudev-libs \
        expat-dev \
        flac \
        gdk-pixbuf \
        glib \
        libgcc \
        libjpeg-turbo \
        libpng \
        libwebp \
        libx11 \
        libxcomposite \
        libxdamage \
        libffi-dev \
        libxext \
        libxfixes \
        tzdata \
        libexif \
        udev \
        xvfb \
        zlib-dev \
        chromium \
        chromium-chromedriver
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


# copy project
COPY . /usr/src/app/

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]


