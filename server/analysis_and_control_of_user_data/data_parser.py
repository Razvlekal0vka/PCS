from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', required=True)
parser.add_argument('password', required=True)
parser.add_argument('friend_username', required=True)
parser.add_argument('new_file', required=True)
parser.add_argument('delete_file', required=True)
parser.add_argument('accessible_file', required=True)
