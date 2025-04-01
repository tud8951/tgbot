@echo off
setlocal

:: 设置环境变量
set TELEGRAM_BOT_TOKEN=7547449008:AAHtmGozLFRi1XBgZRIsfhbm40ebMoFhBqk

:: 创建日志目录
if not exist "logs" mkdir logs

:: 设置日志文件名（使用当前日期）
set log_file=logs\bot_%date:~0,4%%date:~5,2%%date:~8,2%.log

:: 启动机器人并记录日志
echo 正在启动机器人... >> %log_file%
echo 启动时间: %date% %time% >> %log_file%
echo. >> %log_file%

:loop
python telegram_bot.py >> %log_file% 2>&1
echo. >> %log_file%
echo 机器人意外停止，5秒后重新启动... >> %log_file%
echo 重启时间: %date% %time% >> %log_file%
timeout /t 5 /nobreak
goto loop 