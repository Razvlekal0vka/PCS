from . import db_session
from .users import User
from flask import abort, jsonify
from flask_restful import Resource
from .users_parser import parser


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify('gggg')

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListReource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify('llll')

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname = args["surname"],
            name = args["name"],
            age = args["age"],
            position = args["position"],
            speciality = args["speciality"],
            address = args["address"],
            email = args["email"],
            hashed_password = args["hashed_password"]
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
