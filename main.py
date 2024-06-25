import logging

from app.app import create_app

app = create_app()


if __name__ == '__main__':
    logging.debug('DEBUG日志')
    logging.info('INFO日志')
    logging.warning('WARNING日志')
    app.run()
