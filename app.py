from flask import Flask
from flask import jsonify, make_response, session, url_for, redirect, g

from exts import db
from models import UserModel

# use flask_restful
from flask_restful import Api

# / 首页
from views.home import home
from views.login import login
from views.register import register
from views.question import question

from views.viewer import viewer

from views.upload import upload

# restful

# use flask_restful
from restful.order import Order

# config
import config

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)

# use blueprint return view template
# 模块划分 blueprint 蓝图
app.register_blueprint(home)
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(question)

app.register_blueprint(viewer)
app.register_blueprint(upload)

'''
use flask_restful lib
'''

# 实例化
api = Api(app)
api.add_resource(Order, '/api/v1/order/<order_id>/<order_name>')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found ', 'reason': str(error)}), 404)


@app.context_processor
def context_processor():
    if hasattr(g, 'user'):
        return {"user": g.user}
    else:
        return {}


@app.before_request
def before_request():
    user_id = session.get('id')
    if user_id:
        user = UserModel.query.get(user_id)
        g.user = user


if __name__ == '__main__':
    app.run()
