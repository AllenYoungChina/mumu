from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from app.settings import env
from app.config.config import config


def db_connection():
    # 创建连接引擎，用于连接数据库
    engine = create_engine(url=config[env].db_url, echo=config[env].echo)
    # 打开数据库连接会话
    session = sessionmaker(bind=engine)
    # 保证线程安全
    db_session = scoped_session(session)
    # 获取基类
    Base = declarative_base()
    return engine, db_session, Base
