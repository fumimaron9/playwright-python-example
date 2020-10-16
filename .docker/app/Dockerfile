FROM ubuntu:bionic

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    language-pack-ja-base \
    language-pack-ja \
    curl

RUN locale-gen ja_JP.UTF-8

RUN apt-get install -y python3.8
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN apt-get install -y \
    python3-pip \
    python3-distutils
RUN python get-pip.py
RUN pip install -U setuptools

RUN apt-get install -y \
    libwoff1 \
    libopus0 \
    libwebp6 \
    libwebpdemux2 \
    libenchant1c2a \
    libgudev-1.0-0 \
    libsecret-1-0 \
    libhyphen0 \
    libgdk-pixbuf2.0-0 \
    libegl1 \
    libnotify4 \
    libxslt1.1 \
    libevent-2.1-6 \
    libgles2 \
    libvpx5 \
    libnss3 \
    libxss1 \
    libasound2

RUN apt-get install -y \
    libdbus-glib-1-2 \
    libxt6 \
    gstreamer1.0-libav \
    libharfbuzz-bin \
    libharfbuzz-icu0 \
    libgstreamer-gl1.0 \
    libgstreamer-plugins-bad1.0

RUN pip install --quiet \
    playwright \
    pytest \
    pytest-asyncio \
    pytest-xdist
RUN python -m playwright install

ENV PYTHONPYCACHEPREFIX=/usr/src/__pycache__

ENV SHELL bash
ENV LANG en_US.UTF-8
ENV TZ Asia/Tokyo
