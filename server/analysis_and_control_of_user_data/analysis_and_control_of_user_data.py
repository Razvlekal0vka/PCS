from flask import jsonify
from flask_restful import Resource
from sqlalchemy.testing.pickleable import User
from users_parser import parser


class new_user(Resource):
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args["surname"],
            name=args["name"],
            age=args["age"],
            position=args["position"],
            speciality=args["speciality"],
            address=args["address"],
            email=args["email"],
            hashed_password=args["hashed_password"]
        )
        session.add(user)
        session.commit()
        return jsonify('account created successfully')
