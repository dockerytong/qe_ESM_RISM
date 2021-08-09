# Quantum ESPRESSO(ESM/ESM-RISM)を用いた表面・界面シミュレーションのチュートリアル

**学部2年生用のセミナー資料です。第一原理計算全般の知識・技術習得を目的としておりません。このDocker imageは[Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/)のjupyter/scipy-notebookをベースにしております。まずは[こちら](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html)をご覧になり、各コマンドや環境変数をご確認下さい。**

## 準備
### Dockerイメージを手元で作成する
```bash
docker build -t jupyterlab:latest .
```
### Jupyterlabを立ち上げる
- tokenあり
```bash
docker run --rm \
           -p 8888:8888 \
           -e GRANT_SUDO=yes \
           --user root \
           -e JUPYTER_ENABLE_LAB=yes \
           --name jupyterlab \
           -v $PWD:/workdir \
           jupyterlab:latest \
           start.sh jupyter lab
```
- tokenなし（セキュリティー的に問題あり）
```bash
docker run --rm \
           -p 8888:8888 \
           -e GRANT_SUDO=yes \
           --user root \
           -e JUPYTER_ENABLE_LAB=yes \
           --name jupyterlab \
           -v $PWD:/workdir \
           jupyterlab:latest \
           start.sh jupyter lab \
           --NotebookApp.token=''
```

### コンテナに接続してbashを立ち上げて作業する
```bash
docker exec -it jupyterlab start.sh
```
## チュートリアル
### 第1章 Matplotlibを使ってグラフを描いてみる
| |タイトル |nbviewer|Open in Colab |
|---|---|---|---|
|1-1 |簡単なプロット |[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/minoru-otani/qe_devenv_JP/blob/main/notebook/01matplotlib.ipynb) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minoru-otani/qe_devenv_JP/blob/main/notebook/01matplotlib.ipynb)|

### 第2章 Jupyterlab上で[ASE](https://wiki.fysik.dtu.dk/ase/)を使ってみる
| |タイトル |nbviewer|Open in Colab |
|---|---|---|---|
|2-1 |ASEの使い方 |[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/minoru-otani/qe_devenv_JP/blob/main/notebook/02ASE.ipynb) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minoru-otani/qe_devenv_JP/blob/main/notebook/02ASE.ipynb)|

