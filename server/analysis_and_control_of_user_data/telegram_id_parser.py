from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('telegram_id', required=True)
parser.add_argument('pcs_id', required=True)
