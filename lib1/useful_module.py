import logging

logger = logging.getLogger(__name__)


def useful_function():
    logger.debug('this is a debug message')
    logger.info('this is a info message')
    logger.warn('this is a warn message')
    logger.error('this is a serious error message')
