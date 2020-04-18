import os
from tools.env_tool import get_env


debug = get_env("DEBUG", bool, False)
port = get_env("PORT", int, 80)


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self