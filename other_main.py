import logging

from common import log_utils, settings
from lib1 import useful_module

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    log_utils.config_logging(logging.WARN, settings.LOG_PATH)
    logging.getLogger('lib1.useful_module').setLevel(logging.DEBUG)
    logger.debug('this is other main - debug message')
    logger.info('this is other main - info message')
    useful_module.useful_function()
