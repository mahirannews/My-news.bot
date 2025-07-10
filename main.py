from telegram import Update
from telegram.ext import Application, CommandHandler, M>
from telegram.ext import filters  # توجه: filters با حر>

TOKEN = "7732978264:AAHukDeppuz2WoRN3Kq3e2zI-SXSILJVhWE"

async def start(update: Update, context: ContextTypes.D>
    await update.message.reply_text('👋 سلام! به ربات م>

async def echo(update: Update, context: ContextTypes.DE>
    await update.message.reply_text(f'شما نوشتید: {upda>

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filt>

    print("✅ ربات فعال شد! برای توقف Ctrl+C را بزنید.")
    app.run_polling()

if __name__ == '__main__':
    main ()
