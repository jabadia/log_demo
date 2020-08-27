import os
import logging


def get_log_path(log_folder, main_file):
    return os.path.join(log_folder, os.path.basename(main_file).replace('.py', '.log'))


def config_logging(log_level=logging.INFO, log_path=None):
    log_folder = os.path.dirname(log_path)
    os.makedirs(log_folder, exist_ok=True)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    console_formatter = logging.Formatter('%(levelname)-8s %(message)s [%(pathname)s:%(lineno)d]')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)

    if log_path:
        file_formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(message)s [%(pathname)s:%(lineno)d]')
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)
