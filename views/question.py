from flask import Blueprint, render_template
from decorators import login_required

question = Blueprint('question', __name__)


@question.route('/question')
@login_required
def index():
    return render_template('question/index.html')
