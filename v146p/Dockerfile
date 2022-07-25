FROM scimulate/code_aster:14.6

# Install Prerequisites
# Source: https://hitoricae.com/2020/10/31/code_aster-14-6-parallel-version-with-petsc/
RUN apt-get update && apt-get install -y \
    gfortran \
    g++ \
    python-dev \
    python-numpy \
    liblapack-dev \
    libblas-dev \
    tcl \
    tk \
    zlib1g-dev \
    bison \
    flex \
    checkinstall \
    openmpi-bin \
    libx11-dev \
    cmake \
    grace \
    gettext \
    libboost-all-dev \
    swig \
    libsuperlu-dev

WORKDIR /tmp
RUN wget https://www.code-aster.org/FICHIERS/aster-full-src-14.6.0-1.noarch.tar.gz
RUN tar xzvf aster*
WORKDIR /tmp/aster-full-src-14.6.0
RUN python3 setup.py install --noprompt

# Compile OpenBLAS
WORKDIR /tmp
RUN wget https://github.com/xianyi/OpenBLAS/archive/refs/tags/v0.2.20.tar.gz
RUN tar xzvf v0.2.20.tar.gz
WORKDIR /tmp/OpenBLAS-0.2.20
RUN make TARGET=NEHALEM
RUN make NO_AFFINITY=1 USE_OPENMP=1
RUN make PREFIX=/opt/OpenBLAS install
RUN echo /opt/OpenBLAS/lib | sudo tee -a /etc/ld.so.conf.d/openblas.conf
RUN ldconfig
