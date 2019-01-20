#!/usr/bin/env python3
import logging

# will not work in repl but will in pycharm
logging.basicConfig(level=logging.DEBUG) # if this is the default logging level
# or
# logging.basicConfig(format='%(asctime) %(levelname)s:%(message)s', level=logging.DEBUG) <- better formatting
# logging.basicConfig(format='%(asctime) %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)

logger = logging.getLogger('test_logger')

logger.info('This will not show up.')
logger.warning('This will!')

"""DEBUG INFO WARNING ERROR CRITICAL"""
