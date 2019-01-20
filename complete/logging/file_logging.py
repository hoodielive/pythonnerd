#!/usr/bin/env python

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d %(message)s]',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger('test_logger')

logger.info('This will not show up.')
logger.warning('This will.')
logger.debug('This is a debug message.')
logger.critical('A critical error has occurred.')
