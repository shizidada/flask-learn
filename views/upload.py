import os

from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, jsonify

upload = Blueprint('upload', __name__)


@upload.route("/upload", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('upload/index.html')
    else:
        print(request.files)
        # print(type())
        print(os.path.dirname(__file__))
        f = request.files['file']
        base_path = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(base_path, 'uploads', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        context = {}
        try:
            f.save(upload_path)
            context['file_name'] = f.filename
            context['upload_path'] = upload_path
            return jsonify(context)
        except FileNotFoundError as e:
            context['error'] = e.strerror
            return jsonify(context)
