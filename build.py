import argparse
import logging

from webassets import Environment
from webassets.script import CommandLineEnvironment


BASE_PATH = ""


def watch():
    env = _set_env()
    log = _load_logger()
    CommandLineEnvironment(env, log).watch()


def _set_env(debug=True, cache=False):
    env = Environment(BASE_PATH)

    if debug:
        env.manifest = False

    env.cache = cache

    return env


def _load_logger():
    # Setup a logger
    log = logging.getLogger('webassets')
    log.addHandler(logging.StreamHandler())
    log.setLevel(logging.DEBUG)
    return log


def run():
    parser = argparse.ArgumentParser(description="Build or watch assets")
    parser.add_argument(
        'build', default='watch', help="Build type to be run.")

    args = parser.parse_args()

    build = BUILDS.get(args.build)

    assert build

    build()


BUILDS = {
    'watch': watch,
    #'prod': prod
}


if __name__ == "__main__":
    run()
