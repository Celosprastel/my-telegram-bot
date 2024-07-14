from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from datetime import datetime
import os

# Token API yang Anda dapatkan dari BotFather
API_TOKEN = os.getenv('7034834556:AAFe5FCxDjpFmn4kUdovibag9wOt4MozTyo')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Halo! Saya bot yang menarik. Apa yang bisa saya bantu?')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Berikut adalah perintah yang tersedia:\n'
                              '/start - Mulai percakapan dengan bot\n'
                              '/help - Tampilkan pesan bantuan\n'
                              '/info - Berikan informasi tentang bot\n'
                              '/echo - Ulangi pesan pengguna\n'
                              '/time - Tampilkan waktu saat ini')

def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Saya adalah bot Telegram yang dibuat untuk membantu dan menghibur Anda!')

def echo(update: Update, context: CallbackContext) -> None:
    user_message = ' '.join(context.args)
    update.message.reply_text(f'Anda mengatakan: {user_message}')

def time(update: Update, context: CallbackContext) -> None:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update.message.reply_text(f'Waktu saat ini: {now}')

def main() -> None:
    # Buat Application
    application = ApplicationBuilder().token(API_TOKEN).build()

    # Tambahkan handler untuk perintah /start, /help, /info, /echo, dan /time
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("time", time))

    # Mulai bot
    application.run_polling()

if __name__ == '__main__':
    main()
