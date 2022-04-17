from flask import jsonify
from flask_restful import Resource
from sqlalchemy.testing.pickleable import User
from users_parser import parser


class new_user(Resource):
    def post(self):
        args = parser.parse_args()
        user = User(
            name=args["name"],
            username=args["username"],
            password=args["password"],
            speciality=args["phone"],
            address=args["mail"],
            email=args["activation_code"]
        )
        print(user)
        return jsonify('account created successfully')
