FROM scimulate/code_aster:14.6

# Install Prerequisites
# Source: https://hitoricae.com/2020/10/31/code_aster-14-6-parallel-version-with-petsc/

# Source: https://github.com/FIPE-System/code_aster-paralell_installlation

# Step 1: Compile OpenBLAS
WORKDIR /tmp
RUN wget https://github.com/xianyi/OpenBLAS/archive/refs/tags/v0.2.20.tar.gz
RUN tar xzvf v0.2.20.tar.gz
WORKDIR /tmp/OpenBLAS-0.2.20
RUN make NO_AFFINITY=1 USE_OPENMP=1
RUN make PREFIX=/opt/OpenBLAS install



#RUN make TARGET=NEHALEM
#RUN make TARGET=HASWELL NO_AFFINITY=1 USE_OPENMP=1
#RUN make PREFIX=/opt/OpenBLAS install
#RUN echo /opt/OpenBLAS/lib | sudo tee -a /etc/ld.so.conf.d/openblas.conf
#RUN ldconfig
