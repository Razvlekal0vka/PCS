import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

reply_keyboard = [['/address', '/phone'],
                  ['/site', '/work_time']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

letters_ru = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЫыЭэЮюЯя'
letters_en = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
letters_sy = '_-ъь[]|/.,<>?&'
letters_nu = '0123456789'

dialogues_ru = {
    'start': "Привет! Я PCSbot, я могу помочь вам с регистрацией и её подтверждением. Также вы сможете востановить"
             " через меня пароль от своей учетной записи, загружать и скачавать файлы, предоставлять доступ к ним и "
             "смотреть древо своих данных",
    'help_command': '/help - выведет вам все доступные команды',
    'registration_command': '/registration - регистрация нового аккаунта',
    'password_recovery_command': '/password_recovery - восстановление пароля',
    'account_deleting_command': '/account_deleting - удаление аккаунта',
                }

dialogues_eu = {
    'start': "Hey! I am PCSbot, I can help you with registration and confirmation. You can also restore"
             " through me the password from your account, upload and download files, provide access to them and "
             "view your data tree",
    'help_command': '/help - will give you all available commands',
    'registration_command': '/registration - registering a new account',
    'password_recovery_command': '/password_recovery - password recovery',
    'account_deleting_command': '/account_deleting - account deleting',
                }

dialogues = {'ru': dialogues_ru,
             'en': dialogues_eu
             }

language = 'ue'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING
)

logger = logging.getLogger(__name__)

TOKEN = '5227264432:AAHDTKHFiy2fE5Mx1y_UF6e-NqlBbQloDU0'


def help(update, context):
    update.message.reply_text(
        "Я бот справочник.")


def address(update, context):
    update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16")


def phone(update, context):
    update.message.reply_text("Телефон: +7(495)776-3030")


def site(update, context):
    update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")


def work_time(update, context):
    update.message.reply_text(
        "Время работы: круглосуточно.")

def start(update, context):
    update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )
def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("address", address))
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("work_time", work_time))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("close", close_keyboard))
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
