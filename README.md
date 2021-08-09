# Quantum ESPRESSO(ESM/ESM-RISM)を用いた表面・界面シミュレーションのチュートリアル

**学部2年生用のセミナー資料です。第一原理計算全般の知識・技術習得を目的としておりません。**

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
