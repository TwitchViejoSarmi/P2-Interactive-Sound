@echo off
setlocal ENABLEDELAYEDEXPANSION
cd /d "%~dp0\.."
if not exist ".venv" (
  echo No virtual environment found. Creating one now...
  py -3 -m venv .venv
)
call ".venv\Scripts\activate.bat"
python -m src.game.main
