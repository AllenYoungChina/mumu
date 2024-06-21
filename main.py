import logging

from app.app import create_app
from common import setup_logging

app = create_app()
setup_logging()


if __name__ == '__main__':
    logging.debug('DEBUG日志')
    logging.info('INFO日志')
    logging.warning('WARNING日志')
    app.run()
