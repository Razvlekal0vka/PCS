from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', required=True)
parser.add_argument('password', required=True)
parser.add_argument('friend_username', required=True)
parser.add_argument('name_data', required=True)
