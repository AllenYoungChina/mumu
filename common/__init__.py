import logging
from logging.handlers import RotatingFileHandler

from app.config.config import config
from app.settings import env


def setup_logging():
    # 设置日志等级
    logging.basicConfig(level=config[env].LOG_LEVEL)
    # 创建日志记录器
    file_log_handler = RotatingFileHandler('log/logs.log', maxBytes=1024*1024*30, backupCount=10,
                                           encoding='utf-8')
    # 创建日志记录格式
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d %(message)s')
    file_log_handler.setFormatter(formatter)

    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


setup_logging()
