import os

from flask import Flask

from google.appengine.ext.webapp.util import run_wsgi_app

# TODO: register blueprints
# TODO: add jinja html compresession
# TODO: check for appstats
# TODO: check for dev for debuggin

config = getattr(os, 'app_config', 'settings')


def create_application(conf=None):
    app = Flask(__name__)

    if conf:
        app.config.from_object(conf)

    # TODO: include babel?

    return app


app = create_application()


def main():
    run_wsgi_app(app)


if __name__ == "__main__":
    main()
