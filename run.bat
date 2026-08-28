@echo off
title Okul Ders Programi Hazirlama Sistemi
echo ========================================================
echo   Okul Ders Programi Hazirlama Sistemi Baslatiliyor...
echo ========================================================
echo.
echo Tarayici aciliyor...
start http://127.0.0.1:8000
echo.
.\venv\Scripts\uvicorn.exe main:app --reload --host 127.0.0.1 --port 8000
pause
