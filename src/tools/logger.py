import os
import collections
import logging
from pythonjsonlogger import jsonlogger

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['service_name'] = os.getenv('SRV', 'DUMMY')

def prepare_logger(logger, config):
    
    log_format = config.get('log_format')
    log_level = config.get('log_level')
    log_path = config.get('log_path')

    formatter = logging.Formatter(f'[{os.getpid()}] {log_format}')
    handler = logging.FileHandler(log_path) if log_path else logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)

    formatter = CustomJsonFormatter(f'%(service_name)s - %(process)d - {log_format}')
    json_log_path = config.get('json_log_path')
    json_handler = logging.FileHandler(json_log_path) if json_log_path else logging.StreamHandler()
    json_handler.setFormatter(formatter)

    logger.addHandler(json_handler)
