import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='log',
                filemode='w')
def debug(msg):
    logging.debug(msg)


def info(msg):
    logging.info(msg)
