import csv

from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from analysis_and_control_of_user_data.new_user import new_user
from analysis_and_control_of_user_data.adding_an_activation_code import adding_an_activation_code
from analysis_and_control_of_user_data.account_login import account_login
from analysis_and_control_of_user_data.check_available_functions import check_available_functions

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


def main():
    app.run()


if __name__ == '__main__':
    main()
