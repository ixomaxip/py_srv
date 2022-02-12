import os
import sys
import logging
from pythonjsonlogger import jsonlogger

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['service_name'] = os.getenv('SRV', 'DUMMY')

def prepare_logger(logger, config):
    
    log_format = config.get('log_format')
    log_level = config.get('log_level')

    json_log_path = config.get('json_log_path')
    formatter = CustomJsonFormatter(f'%(service_name)s - {log_format}')
    json_handler = logging.FileHandler(json_log_path) if json_log_path else logging.StreamHandler()
    json_handler.setFormatter(formatter)
    logger.addHandler(json_handler)

    if json_log_path is not None:
        formatter = logging.Formatter(f'{log_format}')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    logger.setLevel(log_level)

