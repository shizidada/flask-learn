from flask import Blueprint, render_template

viewer = Blueprint('viewer', __name__)


@viewer.route('/viewer')
def index():
    return render_template('viewer/index.html')


@viewer.route('/zoomify')
def zoomify():
    return render_template('viewer/index2.html')


@viewer.route('/pagination')
def pagination():
    return render_template('viewer/index3.html')
