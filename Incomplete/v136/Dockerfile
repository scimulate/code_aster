FROM ubuntu:20.04

# Install Prerequisite Packages
RUN apt-get update && apt-get install -y \
    bison \
    cmake \
    flex \
    g++ \
    gcc \
    gfortran \
    grace \
    libboost-numpy-dev \
    libboost-python-dev \
    libopenblas-dev \
    make \
    python2.7 \
    python2.7-dev \
    python2.7-numpy \
    tk \
    wget \
    vim \
    zlib1g-dev
    
# Download, Extract, & Compile Source Code
WORKDIR /tmp
RUN wget https://www.code-aster.org/FICHIERS/aster-full-src-13.6.0-1.noarch.tar.gz
RUN tar xzvf aster*
WORKDIR /tmp/aster-full-src-13.6.0
RUN python2 setup.py install --noprompt

# Setup Folder for Volume Mount
RUN mkdir /analysis
WORKDIR /analysis
