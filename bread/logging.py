import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug('Adding user %s to group %s', user.name, new_group)

if not user.is_current():
    logging.warning('User %s owes membership dues', user.name)
