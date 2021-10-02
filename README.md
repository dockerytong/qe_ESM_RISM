# Quantum ESPRESSO(ESM/ESM-RISM)を用いた表面・界面シミュレーションのチュートリアル

密度汎関数法(density functional theory: DFT)を用いた電子状態計算プログラム([Qunatum ESPRESSO](https://www.quantum-espresso.org))を使ったチュートリアル用の資料です。[有効遮蔽媒質(effective screening medium: ESM)法](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.73.115407)を用いた固体表面の計算と、ESM法と古典溶液理論である相互作用点モデル(reference interaction site model: RISM)を組み合わせた[ESM-RISM法](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.96.115429)を用いた固液界面シミュレーション技術の習得を目的としています。

## このチュートリアルで身につくシミュレーション技術
- ESM法を用いたスラブモデルの電子状態計算
  - 表面の仕事関数が直接計算できます。
  - GaNやNaClなどの極性表面や水分子などの極性分子を補正なしに扱うことができます。
- 表面に電圧を印加した状態での電子状態計算
  - ゲート電極やSTM tipの様に表面の片側に電極を置いた状態や、キャパシターの中にスラブを挿入した状態の計算ができます。
  - 表面電荷を一定にした計算や、印加電圧を一定にした計算ができます。
  - 電圧を印加した状態で表面に吸着した分子の構造変化や化学反応のシミュレーションが行えます。

- 固体と液体の界面(固液界面)の電子状態計算
  - DFTで扱う電極とRISMで扱う電解液の界面を計算できます。これにより電気二重層をモデリングすることが可能となります。
  - 様々な塩や混合溶媒を扱うことができ、pHをコントロールすることも可能です。
  - 電解液中のイオンの電極への脱挿入反応のシミュレーションができます。これにより脱溶媒和の様子も観察できます。
  - 金属表面に吸着した分子の酸化還元反応のシミュレーションが行えます。
  - 固液界面における触媒反応や電池、腐食・防食を対象とした電気化学反応のシミュレーションを行うことが可能です。

## チュートリアルの実施方法
チュートリアルの実施方法には二つあります。一つ目の方法はGoogle Colaboratoryを使う方法です。チュートリアルの各章にあるGoogle Colaboratoryのバッジをクリックすると、jupyter notebookでチュートリアルを実施可能です。二つ目は、Docker imageを作成して、ご自分のマシンでコンテナを立ち上げる方法です。Docker imageを作成する場合は下の**準備**を参照して下さい。このDocker imageは[Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/)のjupyter/scipy-notebookをベースにしております。興味のある方は、[こちら](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html)をご覧になり、各コマンドや環境変数をご確認下さい。

## 準備
### Dockerイメージを手元で作成する
プロジェクトをクローンする
```bash
git clone https://github.com/minoru-otani/qe_tutorial_JP.git
```
qe_tutorial_JPディレクトリに入り、docker imageを作成する。
```bash
cd qe_tutorial_JP
docker build -t jupyterlab:latest .
```
### Jupyterlabを立ち上げる
- tokenあり
```bash
docker run --rm \
           -p 8888:8888 \
           -e GRANT_SUDO=yes \
           -e NB_USER=$USER \
           --user root \
           -e JUPYTER_ENABLE_LAB=yes \
           --name jupyterlab \
           -v $PWD/notebook:/workdir \
           jupyterlab:latest \
           start.sh jupyter lab
```
- tokenなし（セキュリティー的に問題あり）
```bash
docker run --rm \
           -p 8888:8888 \
           -e GRANT_SUDO=yes \
           -e NB_USER=$USER \
           --user root \
           -e JUPYTER_ENABLE_LAB=yes \
           --name jupyterlab \
           -v $PWD/notebook:/workdir \
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

### 第2章 [SciPy](https://scipy.org)を使ってみる
### 第3章 Jupyterlab上で[ASE](https://wiki.fysik.dtu.dk/ase/)を使ってみる
| |タイトル |nbviewer|Open in Colab |
|---|---|---|---|
|2-1 |ASEの使い方 |[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/minoru-otani/qe_devenv_JP/blob/main/notebook/02ASE.ipynb) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minoru-otani/qe_devenv_JP/blob/main/notebook/02ASE.ipynb)|

### 第4章 Google ColaboratoryでESM計算をやってみる
[Yuki Nagaiさんのページ](https://cometscome.github.io/DFT/build/)を参考にGoogle Colaboratoryを使ってQuantum ESPRESSO(QE)が使ってみます。QEのコンパイル方法は[このページ](https://cometscome.github.io/DFT/build/Fast/fast/#Google-Colaboratoryを使って第一原理計算)を参考にしています。Google Colaboratoryを使っても、ローカルにjupyterlabを立ち上げてもどちらでもプログラムを実施することができます。
| |タイトル |nbviewer|Open in Colab |
|---|---|---|---|
|3-1 |Quantum ESPRESSOを用意する |[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/minoru-otani/qe_devenv_JP/blob/main/notebook/03colab_qe.ipynb) |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minoru-otani/qe_devenv_JP/blob/main/notebook/03colab_qe.ipynb)|
