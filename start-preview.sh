#!/bin/sh
# 本地一键预览宠物站（macOS / Linux）。运行： sh start-preview.sh
cd "$(dirname "$0")/public"
python3 -m http.server 8787 --bind 127.0.0.1
echo "预览地址： http://127.0.0.1:8787/"
