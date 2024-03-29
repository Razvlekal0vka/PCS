from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('name', required=True)
parser.add_argument('username', required=True)
parser.add_argument('password', required=True)
parser.add_argument('phone', required=True)
parser.add_argument('email', required=True)
parser.add_argument('activation_code', required=True)
