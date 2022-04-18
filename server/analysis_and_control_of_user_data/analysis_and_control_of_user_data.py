from flask import jsonify
from flask_restful import Resource
from .users_parser import parser


class new_user(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        return jsonify('account created successfully')
