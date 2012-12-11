import os
import sys


BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def add_path(path):
    """Add a path to sys.path ensuring no duplicates are added.

    Also checks for .zip and .egg files in that path so that zip import works
    as expected.
    """
    path = os.path.abspath(path).rstrip(os.sep)

    assert path.startswith(BASE_PATH), path

    if path in sys.path:
        return

    sys.path.insert(0, path)

    for filename in os.listdir(path):
        if filename.endswith((".zip", ".egg", ".egg-info")):
            sys.path.insert(0, os.path.join(path, filename))


def is_production():
    """Does some hacking to try and guess if we are running on a production
    server or just locally for tests or the dev server.
    """
    ss = os.getenv('SERVER_SOFTWARE')

    if ss:
        if ss.startswith('Google App Engine'):
            return True

        if ss.startswith('Devel'):
            return False

    if 'google.appengine.tools' in sys.modules:
        return False

    try:
        from google.appengine import tools
    except ImportError:
        return False

    return True


def setup_environ():
    """ Sets up the environment and paths for Spicolis and the AppEngineSDK (
    if running locally).
    """
    if not is_production():
        LIB_PATH = os.path.join(BASE_PATH, 'libs')

        add_path(LIB_PATH)

        import dev_appserver

        dev_appserver.fix_sys_path()
