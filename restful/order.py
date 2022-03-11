from flask import request

from flask_restful import Resource


class Order(Resource):
    def get(self, order_id, order_name):
        print(request.args)
        print('-' * 100)
        print(request.form)
        context = {
            'order_id': order_id,
            'order_name': order_name
        }
        return {**context}

    def post(self, order_id, order_name):
        print(request.args)
        print('-' * 100)
        print(request.form)
        print('post', order_id, order_name)
