from flask import Blueprint, jsonify, request, make_response

user = Blueprint('user', __name__)


@user.route("/api/v1/user/add", methods=['POST'])
def add_user():
    # print(request.form)
    # print(request.form.get('token'))
    # print(request.form.get('username'))
    # print(request.form.get('password'))
    # print(request.method)
    token = request.form.get('token')
    if (token is None):
        result = {
            'status': False,
            'message': 'token is null',
            'data': None
        }
        return jsonify(result)
    username = request.form.get('username')
    password = request.form.get('password')
    if (username == '江景' and password == '123456'):
        info = {
            'token': token,
            'status': True,
            'message': 'auth success',
            'data': {
                'username': username,
                'password': password
            }
        }
    else:
        info = {
            'token': token,
            'status': False,
            'message': 'auth failed',
            'data': None
        }
    return jsonify(info)


@user.route('/api/v1/user/delete')
def delete_user():
    users = [
        {'_id': 1, 'name': '张三', 'age': 19},
        {'_id': 2, 'name': '李四', 'age': 17},
        {'_id': 3, 'name': '黄五', 'age': 24},
        {'_id': 4, 'name': '赵六', 'age': 16}
    ]
    del users[2]
    return jsonify(users)


@user.route('/api/v1/user/get')
def get_user():
    users = [
        {'_id': 1, 'name': '张三', 'age': 19},
        {'_id': 2, 'name': '李四', 'age': 17},
        {'_id': 3, 'name': '黄五', 'age': 24},
        {'_id': 4, 'name': '赵六', 'age': 16}
    ]
    return jsonify(users)
