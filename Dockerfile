FROM jupyter/scipy-notebook
LABEL maintainer="Minoru Otani <otani@ccs.tsukuba.ac.jp>"

USER root
RUN apt-get update -y \
    && apt-get upgrade -y

RUN apt-get install -y -q --no-install-recommends \
    wget \
    git \
    vim \
    curl \
    make \
    cmake \
    povray \
    povray-includes \
    && curl -sL https://deb.nodesource.com/setup_14.x |bash - \
    && apt-get install -y nodejs \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf \
       /var/lib/apt/lists/* \
       /var/cache/apt/* \
       /usr/local/src/* \
       /tmp/*

# install python library
RUN pip install --upgrade pip \
    && pip install --upgrade jupyterlab \
    && pip install --no-cache-dir \
    ase \
    nglview \
    ipywidgets \
    && rm -rf ~/.cache/pip

# install jupyterlab extentions
RUN jupyter labextension install @axlair/jupyterlab_vim

WORKDIR /workdir
