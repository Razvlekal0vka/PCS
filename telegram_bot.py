import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING
)

logger = logging.getLogger(__name__)

TOKEN = '5227264432:AAHDTKHFiy2fE5Mx1y_UF6e-NqlBbQloDU0'


def echo(update, context):
    update.message.reply_text(update.message.text)


def start(update, context):
    update.message.reply_text(
        "Привет! Я PCSbot, я могу помочь вам с регистрацией и её подтверждением. Также вы сможете востановить через"
        " меня пароль от своей учетной записи, загружать и скачавать файлы, предоставлять доступ к ним и смотреть"
        " древо своих данных")
    update.message.reply_text('/help - выведет вам все доступные команды')


def help(update, context):
    update.message.reply_text('/registration - регистрация нового аккаунта')
    update.message.reply_text('/password_recovery - восстановление пароля')
    update.message.reply_text('/account_deleting - удаление аккаунта')
    update.message.reply_text('/help - выведет вам все доступные команды')


def registration(update, context):
    update.message.reply_text('registration')


def password_recovery(update, context):
    update.message.reply_text('password_recovery')


def account_deleting(update, context):
    update.message.reply_text('account_deleting')


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("registration", registration))
    dp.add_handler(CommandHandler("password_recovery", password_recovery))
    dp.add_handler(CommandHandler("account_deleting", account_deleting))
    dp.add_handler(CommandHandler("help", help))

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
