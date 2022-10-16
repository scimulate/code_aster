FROM ubuntu:18.04
LABEL maintainer "Samuel Jacobs <samjacobs@scimulate.com>"

# Install Prerequisite Packages
RUN apt-get update && apt-get install -y \
    bison \
    cmake \
    flex \
    g++ \
    gcc \
    gfortran \
    grace \
    libboost-numpy1.65-dev \
    libboost-python1.65-dev \
    libopenblas-dev \
    make \
    python3 \
    python3-dev \
    python3-numpy \
    tk \
    wget \
    zlib1g-dev
    
# Download, Extract, & Compile Source Code
WORKDIR /tmp
RUN wget https://code-aster.org/FICHIERS/aster-full-src-14.6.0-1.noarch.tar.gz
RUN tar xzvf aster*
WORKDIR /tmp/aster-full-src-14.6.0

RUN pwd

ENV LANG C.UTF-8
RUN python3 setup.py install --noprompt

# Setup Folder for Volume Mount
RUN mkdir /analysis
WORKDIR /analysis
