FROM jupyter/scipy-notebook
LABEL maintainer="Minoru Otani <otani@ccs.tsukuba.ac.jp>"

USER root
RUN apt-get update -y \
    && apt-get upgrade -y

RUN apt-get install -y -q --no-install-recommends \
    gcc \
    gfortran \
    liblapack-dev \
    libblas-dev \
    mpi \
    openmpi-bin \
    openmpi-common \
    openssh-server \
    openssh-client \
    libopenmpi-dev \
    libfftw3-3 libfftw3-bin libfftw3-dev libfftw3-doc \
    wget \
    git \
    vim \
    curl \
    make \
    cmake \
    povray \
    povray-includes \
    texlive-extra-utils \
    && curl -sL https://deb.nodesource.com/setup_14.x |bash - \
    && apt-get install -y nodejs \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf \
       /var/lib/apt/lists/* \
       /var/cache/apt/* \
       /usr/local/src/* \
       /tmp/*
USER $NB_USER

# install python library
RUN pip install --upgrade pip \
    && pip install --upgrade jupyterlab \
    && pip install --no-cache-dir \
    nglview \
    ipywidgets \
    requests \
    jupyterlab_vim \
#    ase \
    && pip install git+https://gitlab.com/minoru-otani/ase.git@qe_rism \
    && rm -rf ~/.cache/pip

# install jupyterlab extentions
#RUN jupyter labextension install @axlair/jupyterlab_vim

# copy files
WORKDIR $HOME/notebook
COPY notebook .

USER root
RUN chown -R $NB_USER:$NB_GID $PWD
USER $NB_USER

# fix permissions
RUN fix-permissions /home/$NB_USER

WORKDIR $HOME
USER $NB_UID
