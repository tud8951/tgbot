@echo off
:loop
python telegram_bot.py
timeout /t 5
goto loop 