# Dockerfile

# ベースイメージの指定
FROM python:3.8-slim

# 作業ディレクトリの設定
WORKDIR /app

# ソースコードをコピー
COPY . /app

# Pythonスクリプトの実行
CMD ["python", "main.py"]
