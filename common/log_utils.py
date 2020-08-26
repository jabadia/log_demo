import logging
from . import settings


def config_logging():
    log_level = settings.LOG_LEVEL
    log_path = settings.LOG_PATH

    file_formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(message)s [%(pathname)s:%(lineno)d]')
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(file_formatter)

    console_formatter = logging.Formatter('%(levelname)-8s %(message)s [%(pathname)s:%(lineno)d]')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

