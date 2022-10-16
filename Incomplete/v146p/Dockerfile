FROM scimulate/code_aster:14.6
LABEL maintainer "Samuel Jacobs <samjacobs@scimulate.com>"

# Remove base installation. Reinstall with GNU_without_MATH
RUN rm -rf /opt/aster
WORKDIR /tmp/aster-full-src-14.6.0
RUN sed -i "s:PREFER_COMPILER\ =\ 'GNU':PREFER_COMPILER\ =\'GNU_without_MATH'\nMATHLIB=\ '/usr/lib/x86_64-linux-gnu/libopenblas.a':g" setup.cfg
RUN python3 setup.py install --noprompt

WORKDIR /tmp/aster-full-src-14.6.0/SRC
RUN tar xzvf aster*
WORKDIR /tmp/aster-full-src-14.6.0/SRC/aster-14.6.0

COPY docker_std.py /tmp/aster-full-src-14.6.0/SRC/aster-14.6.0/wafcfg
COPY docker_mpi.py /tmp/aster-full-src-14.6.0/SRC/aster-14.6.0/wafcfg

RUN apt-get update && apt-get install -y \
    libblacs* \
    libmumps* \
    libparmetis* \
    libscalapack* \
    libpetsc* \
    libptscotch* \
    libsuperlu*
    
    #RUN apt-get update && apt-get install -y \
#    libscalapack-*-dev \
#    libparmetis-dev \
#    libptscotch-dev \
#    libmumps-dev \
#    libpetsc*dev \
#    libsuperlu-dev

RUN export PYTHONPATH=/opt/aster/lib/python3.6/site-packages/:$PYTHONPATH && \
    ./waf_mpi configure --use-config=docker_mpi --prefix=/opt/aster/14.6p #&& \
    #./waf install -p










#RUN apt-get update && apt-get install -y *blacs*


    
#RUN apt-get update && apt-get install -y \
#    *blacs*dev
    
#RUN export PYTHONPATH=/opt/aster/lib/python3.6/site-packages/:$PYTHONPATH && \
#    ./waf_mpi configure --use-config=docker_mpi --prefix=/opt/aster/14.6p && \
#    ./waf_mpi install -p

# Install Prerequisites
#RUN apt-get update && apt-get install -y \
#    bison \
#    cmake \
#    flex \
#    g++ \
#    gcc \
#    gfortran \
#    grace \
#    libboost-numpy1.65-dev \
#    libboost-python1.65-dev \
#    libopenblas-dev \
#    make \
#    python3 \
#    python3-dev \
#    python3-numpy \
#    tk \
#    wget \
#    zlib1g-dev
    
# Download, Extract, & Compile Source Code
#WORKDIR /tmp
#RUN wget https://code-aster.org/FICHIERS/aster-full-src-14.6.0-1.noarch.tar.gz
#RUN tar xzvf aster*
#WORKDIR /tmp/aster-full-src-14.6.0

#R

#ENV LANG C.UTF-8
#RUN python3 setup.py install --noprompt



#RUN apt-get install -y nano




#RUN ./waf configure --use-config-dir=/opt/aster/14.6/share/aster --use-config=linux_mpi --prefix=/opt/aster/14.6p
#RUN ./waf install -p --jobs=1

#sudo apt-get install  gfortran g++ python-dev python-numpy liblapack-dev libblas-dev tcl tk zlib1g-dev bison flex checkinstall openmpi-bin libx11-dev cmake grace gettext libboost-all-dev swig

# Source: https://hitoricae.com/2020/10/31/code_aster-14-6-parallel-version-with-petsc/

# Source: https://github.com/FIPE-System/code_aster-paralell_installlation

# Step 1: Compile OpenBLAS
#WORKDIR /tmp
#RUN wget https://github.com/xianyi/OpenBLAS/archive/refs/tags/v0.2.20.tar.gz
#RUN tar xzvf v0.2.20.tar.gz
#WORKDIR /tmp/OpenBLAS-0.2.20
#RUN make DYNAMIC_ARCH=1 NO_AFFINITY=1 USE_OPENMP=1 NUM_THREADS=32 && \
#    make PREFIX=/opt/OpenBLAS install

#make DYNAMIC_ARCH=1 NO_AFFINITY=1 NUM_THREADS=32 \
#make install

#RUN make TARGET=NEHALEM
#RUN make TARGET=HASWELL NO_AFFINITY=1 USE_OPENMP=1
#RUN make PREFIX=/opt/OpenBLAS install
#RUN echo /opt/OpenBLAS/lib | sudo tee -a /etc/ld.so.conf.d/openblas.conf
#RUN ldconfig
