@echo off
setlocal ENABLEDELAYEDEXPANSION
cd /d "%~dp0\.."

REM Create venv if missing
if not exist ".venv" (
  echo Creating virtual environment...
  py -3 -m venv .venv
)

REM Activate venv
call ".venv\Scripts\activate.bat"

REM Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Run game
python -m src.game.main
