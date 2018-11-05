from raven import Client
DSN ='http://35f120ea839746c0b2e2f3c867cf7fd6:d2e2b3ba9e2244ee9cedabba9c1b3b4c@192.168.0.127:9000/2'
# client = Client(DSN)
import logging
from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging
handler = SentryHandler(DSN)
handler.setLevel(logging.INFO)
setup_logging(handler)

import logging
if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger = logging.Logger(__file__)
    logger.info('info message' , extra={'stack': True})
    import requests
    logger.error('error message',extra={'stack': True})
    logger.critical('critical message',extra={'stack': True})
