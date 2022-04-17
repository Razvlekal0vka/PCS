from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from analysis_and_control_of_user_data.analysis_and_control_of_user_data import new_user

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['JSON_AS_ASCII'] = False

login_manager = LoginManager()
login_manager.init_app(app)

api.add_resource(new_user, '/api/user_verification/new_user')


def main():
    app.run()


if __name__ == '__main__':
    main()
