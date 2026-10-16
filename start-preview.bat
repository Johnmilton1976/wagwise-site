@echo off
REM 本地一键预览宠物站（Windows）。双击运行，浏览器自动打开 http://127.0.0.1:8787/
cd /d "%~dp0public"
start "" "http://127.0.0.1:8787/"
python -m http.server 8787 --bind 127.0.0.1
