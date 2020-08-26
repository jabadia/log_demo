import logging

from common import log_utils
from lib1 import useful_module

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    log_utils.config_logging()
    logger.debug('this is other main - debug message')
    logger.info('this is other main - info message')
    useful_module.useful_function()
