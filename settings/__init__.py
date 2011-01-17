import sys
from settings.defaults import *

if 'manage.py' not in sys.argv[0] or sys.argv[1] != 'configure':
    try:
        from settings.environment import *
    except ImportError:
        raise RuntimeError("Your environment settings are not configured. " +
            "Please manually create settings/environment.py or auto-generate " +
            "with ./manage.py configure.")
