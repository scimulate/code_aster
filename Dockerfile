FROM debian:buster

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
    python3 \
    python3-dev \
    python3-numpy \
    tk \
    wget \
    zlib1g-dev
    
# Download, Extract, & Compile Source Code
WORKDIR /tmp
RUN wget https://www.code-aster.org/FICHIERS/aster-full-src-14.6.0-1.noarch.tar.gz
RUN tar xzvf aster*
WORKDIR /tmp/aster-full-src-14.6.0
RUN python3 setup.py install --noprompt

# Cleanup
WORKDIR /tmp
RUN rm rm -rf aster-full-src-14.6.0

# Setup Folder for Volume Mount
RUN mkdir /analysis
