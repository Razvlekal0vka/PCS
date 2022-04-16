from flask import Flask, jsonify
from flask_restful import abort, Api, Resource
import db_session
from reqparses import parser
from users import User

app = Flask(__name__)
api = Api(app)


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"News {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify({'users': users.to_dict(
            only=('title', 'content', 'user_id', 'is_private'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('title', 'content', 'user.name')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(title=args['title'],
                     content=args['content'],
                     user_id=args['user_id'],
                     is_published=args['is_published'],
                     is_private=args['is_private'])
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})