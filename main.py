import os
import logging

from common import log_utils, settings
from lib1 import useful_module

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)-8s %(message)s [%(pathname)s:%(lineno)d]',
        level=settings.LOG_LEVEL,
        handlers=[  # salida a consola y a fichero
            logging.StreamHandler(),
            logging.FileHandler(log_utils.get_log_path(settings.LOG_FOLDER, __file__))
        ]
    )
    logger.debug('main debug message')
    logger.info('main info message')
    useful_module.useful_function()
