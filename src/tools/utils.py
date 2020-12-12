import os
import logging
import _io, io

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def get_logger(name: str, stdout: _io.TextIOWrapper, debug_level=False) -> logging.Logger:
    log = logging.getLogger(name)

    h = logging.StreamHandler(stream=stdout)
    h.setFormatter(logging.Formatter('%(message)s'))
    h.flush = stdout.flush
    log.addHandler(h)
    if debug_level:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    return log
