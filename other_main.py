import os
import logging

from common import log_utils, settings
from lib1 import useful_module

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    log_utils.config_logging(settings.LOG_LEVEL, log_utils.get_log_path(settings.LOG_FOLDER, __file__))

    # si quiero, puedo cambiar el nivel de logs de una parte de la aplicación
    logging.getLogger('lib1').setLevel(logging.INFO)

    logger.debug('this is other main - debug message')
    logger.info('this is other main - info message')
    useful_module.useful_function()
