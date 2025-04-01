import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 配置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 获取 Token
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("请设置环境变量 TELEGRAM_BOT_TOKEN")

# 处理 /start 命令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
👋 欢迎使用星語开户工具机器人！

我可以：
• 回答您的问题
• 进行简单的对话
• 提供帮助信息

发送 /help 查看所有可用命令！
"""
    await update.message.reply_text(welcome_text)

# 处理 /help 命令
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 机器人使用指南：

基础命令：
/start - 开始使用机器人
/pd - 频道
/help - 帮助
/about - 关于

发送这些关键词，看看我会如何回复！
"""
    await update.message.reply_text(help_text)

# 处理 /pd 命令
async def channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    channel_text = """
📢 欢迎加入我们的频道！

频道名称：专业开户
频道链接：https://t.me/njnbyyds
订阅人数：985+

频道特色：
• 专门分享开户工具
• 绝对无广告
• 最强资源搜索工具

🔍 搜索工具：https://t.me/nbsearch

欢迎订阅！
"""
    await update.message.reply_text(channel_text)

# 处理 /about 命令
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """
🤖 关于我

版本：1.0.0
作者：星語
电报频道：https://t.me/njnbyyds

功能特点：
• 自动回复系统
• 频道管理
• 资源搜索
• 友好的交互界面

官方频道：@njnbyyds
搜索工具：@nbsearch

如果您有任何建议或问题，欢迎随时反馈！
"""
    await update.message.reply_text(about_text)

# 处理 /zf 命令
async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_photo(photo=open('1.png', 'rb'))
    except Exception as e:
        await update.message.reply_text("抱歉，发送图片时出现错误。")
        logging.error(f"发送图片时出错: {str(e)}")

# 处理普通消息
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    
    # 关键词回复
    if any(word in user_message for word in ["你好", "hello", "hi"]):
        await update.message.reply_text("👋 你好！很高兴见到你！\n有什么我可以帮你的吗？")
    elif "频道" in user_message:
        await update.message.reply_text("📢 欢迎访问我们的频道：https://t.me/njnbyyds")
    elif "工具" in user_message or "搜索" in user_message:
        await update.message.reply_text("🔍 推荐使用我们的搜索工具：https://t.me/nbsearch")
    elif "帮助" in user_message:
        await update.message.reply_text("💡 需要帮助吗？\n发送 /help 查看所有可用命令！")
    else:
        await update.message.reply_text("✨ 收到你的消息了！\n如果需要了解更多，可以：\n1. 发送 /help 查看命令\n2. 访问频道 @njnbyyds\n3. 使用搜索 @nbsearch")

def main():
    # 创建应用
    application = Application.builder().token(TOKEN).build()

    # 添加处理程序
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("pd", channel))
    application.add_handler(CommandHandler("zf", send_image))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # 启动机器人
    print("机器人已启动...")
    application.run_polling()

if __name__ == '__main__':
    main() 