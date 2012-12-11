from flask import Blueprint, Flask


site = Blueprint('site', __name__)


def create_application(conf=None):
    app = Flask(__name__)

    if conf:
        app.config.from_object(conf)

    # TODO: include babel?
    app.register_blueprint(site)

    return app


@site.route("/")
def home():
    return ''
