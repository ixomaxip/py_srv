import os
import json
import logging
import platform
import traceback
from omegaconf import OmegaConf, DictConfig

from tools.logger import prepare_logger

class SrvConfig(DictConfig):

    def __init__(self):
        super().__init__({})
        self.hostname = platform.node()
        default_logging = DictConfig({
            'json_log_path': None,
            'log_level': 'DEBUG',
            'log_format': '%(asctime)s - %(levelname)s - %(message)s'
        })
        
        yaml_options = self._read_yaml()

        sub_options1 = DictConfig({})
        sub_options2 = DictConfig({})

        self.logging = OmegaConf.merge(default_logging, yaml_options.logging)
        self.bind_host = yaml_options.get('bind_host', '127.0.0.1')
        self.bind_port = yaml_options.get('bind_port', 80)
        
        self.sub_options1 = OmegaConf.merge(sub_options1, yaml_options.sub_options1)
        self.sub_options2 = OmegaConf.merge(sub_options2, yaml_options.sub_options2)

    def _read_yaml(self):
        path = os.path.dirname(os.path.realpath(__file__))
        config_filename = os.path.join(path, 'config.yaml')
        try:
            yaml_options = OmegaConf.load(config_filename)
        except Exception as err:
            traceback.print_exc()
            yaml_options = DictConfig({'logging': {}})

        return yaml_options

    def __str__(self):
        return json.dumps(OmegaConf.to_container(self), indent=4)

    def to_dict(self):
        return OmegaConf.to_container(self)

config = SrvConfig()

logger = logging.getLogger()
prepare_logger(logger, config.logging)
