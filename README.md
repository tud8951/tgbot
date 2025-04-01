# Telegram 开户工具机器人

这是一个基于 Python 开发的 Telegram 机器人，主要用于提供开户相关的工具和信息服务。

## 功能特点

- 🤖 自动回复系统
- 📢 频道管理
- 🔍 资源搜索
- 💬 智能对话
- 📸 图片发送功能

## 主要命令

- `/start` - 开始使用机器人
- `/help` - 显示帮助信息
- `/about` - 关于机器人
- `/pd` - 查看频道信息
- `/zf` - 发送图片

## 安装说明

1. 克隆项目到本地
2. 创建并激活虚拟环境（推荐）：
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 配置说明

1. 在 Telegram 上找到 [@BotFather](https://t.me/botfather)，创建新的机器人并获取 Token
2. 设置环境变量 `TELEGRAM_BOT_TOKEN`：
   - Windows: 在系统环境变量中添加
   - 或直接在运行脚本中设置

## 运行方法

1. 直接运行：
   ```bash
   python telegram_bot.py
   ```
2. 使用批处理文件（Windows）：
   - 双击 `run_bot.bat` 或 `start_bot.bat`

## 技术栈

- Python 3.x
- python-telegram-bot 20.7

## 作者信息

- 作者：星語
- 电报频道：[@njnbyyds](https://t.me/njnbyyds)
- 搜索工具：[@nbsearch](https://t.me/nbsearch)

## 赞助
![](https://bigjackson.top/tgbot/1.png)

## 许可证

MIT License