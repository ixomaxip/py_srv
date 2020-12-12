import os
from tools.env_tool import get_env
import platform


debug = get_env("DEBUG", bool, False)
port = get_env("PORT", int, 80)
hostname = platform.node()
