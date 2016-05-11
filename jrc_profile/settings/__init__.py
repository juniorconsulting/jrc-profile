from jrc_profile.settings.base import *

try:
    from jrc_profile.settings.local import *
except ImportError:
    print("Could not load local settings file: jrc_profile.settings.local")
