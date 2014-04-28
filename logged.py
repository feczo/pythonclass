import logging

logger = logging.getLogger('add_app')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('/tmp/add_app_error.log')
formatter = logging.Formatter(
    '%(process)d %(asctime)s'
    '%(pathname)s:%(lineno)d %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def add(a, b=0):
    try:
        return a+b
    except TypeError:
        logger.debug('different types to add ( %s %s, %s %s )' %
                     (a, type(a), b, type(b)))

if __name__ == '__main__':
    print add(3, 4)
    print add(4, 'b')
