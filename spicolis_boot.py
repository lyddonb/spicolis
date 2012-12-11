import os

from google.appengine.ext.webapp.util import run_wsgi_app

from spicolis import create_application

# TODO: add jinja html compresession
# TODO: check for appstats
# TODO: check for dev for debugging

config = getattr(os, 'app_config', 'settings')

app = create_application()


def main():
    run_wsgi_app(app)


if __name__ == "__main__":
    main()
