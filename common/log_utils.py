import logging


def config_logging(log_level=logging.INFO, log_path=None):
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
