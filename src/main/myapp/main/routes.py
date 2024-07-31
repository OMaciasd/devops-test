from flask import Blueprint, render_template

blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index() -> str:
    return render_template('index.html')
