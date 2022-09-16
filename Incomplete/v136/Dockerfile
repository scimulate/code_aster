FROM ubuntu:18.04

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
    python \
    python-dev \
    python-numpy \
    python3 \
    python3-dev \
    python3-numpy \
    tk \
    wget \
    vim \
    zlib1g-dev
    
# Download, Extract, & Compile Source Code
WORKDIR /tmp
RUN wget https://www.code-aster.org/FICHIERS/aster-full-src-13.6.0-1.noarch.tar.gz
RUN tar xzvf aster*
WORKDIR /tmp/aster-full-src-13.6.0
RUN python setup.py install --noprompt

# Setup Folder for Volume Mount
RUN mkdir /analysis
WORKDIR /analysis
