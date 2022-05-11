import csv

from flask import Flask
from flask_login import LoginManager
from flask_restful import Api

from analysis_and_control_of_user_data.new_user import new_user
from analysis_and_control_of_user_data.adding_an_activation_code import adding_an_activation_code
from analysis_and_control_of_user_data.account_login import account_login
from analysis_and_control_of_user_data.check_available_functions import check_available_functions
from analysis_and_control_of_user_data.user_id import user_id

from analysis_and_control_of_user_data.new_file import new_file
from analysis_and_control_of_user_data.change_file import change_file
from analysis_and_control_of_user_data.delete_file import delete_file

from analysis_and_control_of_user_data.telegram_id import telegram_id

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['JSON_AS_ASCII'] = False

login_manager = LoginManager()
login_manager.init_app(app)

api.add_resource(new_user, '/api/user_verification/new_user')
api.add_resource(adding_an_activation_code, '/api/user_verification/adding_an_activation_code')
api.add_resource(account_login, '/api/user_verification/account_login')
api.add_resource(check_available_functions, '/api/user_verification/check_available_functions')
api.add_resource(user_id, '/api/user_verification/user_id')

api.add_resource(new_file, '/api/user_file/new_file')
api.add_resource(change_file, '/api/user_file/change_file')
api.add_resource(delete_file, '/api/user_file/delete_file')

api.add_resource(telegram_id, '/api/telegram/telegram_id')


def main():
    app.run(port=8081, host='127.0.0.1')


if __name__ == '__main__':
    main()
