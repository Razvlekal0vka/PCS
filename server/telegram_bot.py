import logging

from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters

letters_ru = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЫыЭэЮюЯя'
letters_en = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
letters_sy = '_-ъь[]|/.,<>?&'
letters_nu = '0123456789'

dialogues_ru = {
    'start': "Привет! Я PCSbot, я могу помочь вам с регистрацией и её подтверждением. Также вы сможете востановить"
             " через меня пароль от своей учетной записи, загружать и скачавать файлы, предоставлять доступ к ним и "
             "смотреть древо своих данных",
    'help_command': '/help - выведет вам все доступные команды',
    'entrance_to_account_command': '/entrance_to_account - вход в аккаунт',
    'registration_command': '/registration - регистрация нового аккаунта',
    'password_recovery_command': '/password_recovery - восстановление пароля',
    'account_deleting_command': '/account_deleting - удаление аккаунта',
    'ru_command': '/ru - выбор русского языка',
    'en_command': '/en - choice of English',
}

dialogues_en = {
    'start': "Hey! I am PCSbot, I can help you with registration and confirmation. You can also restore"
             " through me the password from your account, upload and download files, provide access to them and "
             "view your data tree",
    'help_command': '/help - will give you all available commands',
    'entrance_to_account_command': '/entrance_to_account - entrance to account',
    'registration_command': '/registration - registering a new account',
    'password_recovery_command': '/password_recovery - password recovery',
    'account_deleting_command': '/account_deleting - account deleting',
    'ru_command': '/ru - выбор русского языка',
    'en_command': '/en - choice of English',
}

dialogues = {'ru': dialogues_ru,
             'en': dialogues_en
             }

language = 'en'

reply_keyboard = [['/entrance_to_account'],
                  ['/registration'],
                  ['/password_recovery'],
                  ['/account_deleting'],
                  ['/ru'],
                  ['/en'],
                  ['/help'],
                  ]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING
)

logger = logging.getLogger(__name__)

TOKEN = '5227264432:AAHDTKHFiy2fE5Mx1y_UF6e-NqlBbQloDU0'


def echo(update, context):
    # update.message.reply_text(update.message.text)
    print(update.message.text)


def start(update, context):
    update.message.reply_text(dialogues[language]['start'])
    update.message.reply_text(dialogues[language]['help_command'], reply_markup=markup)


def help(update, context):
    update.message.reply_text(dialogues[language]['entrance_to_account_command'])
    update.message.reply_text(dialogues[language]['registration_command'])
    update.message.reply_text(dialogues[language]['password_recovery_command'])
    update.message.reply_text(dialogues[language]['account_deleting_command'])
    update.message.reply_text(dialogues[language]['ru_command'])
    update.message.reply_text(dialogues[language]['en_command'])
    update.message.reply_text(dialogues[language]['help_command'])


def en(update, context):
    global language
    language = 'en'


def ru(update, context):
    global language
    language = 'ru'

def entrance_to_account(update, context):
    update.message.reply_text('Entrance to Account')

def registration(update, context):
    update.message.reply_text('registration')


def password_recovery(update, context):
    update.message.reply_text('password_recovery')
    update.message.reply_text('Не работает')
    update.message.reply_text('Does not work')


def account_deleting(update, context):
    update.message.reply_text('account_deleting')
    update.message.reply_text('Не работает')
    update.message.reply_text('Does not work')


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("entrance_to_account", entrance_to_account))
    dp.add_handler(CommandHandler("registration", registration))
    dp.add_handler(CommandHandler("password_recovery", password_recovery))
    dp.add_handler(CommandHandler("account_deleting", account_deleting))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("en", en))
    dp.add_handler(CommandHandler("ru", ru))

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
