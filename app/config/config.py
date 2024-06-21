class Config:
    """全局通用配置"""
    db_url = 'mysql+pymysql://admin:123456@localhost/mumu'


class TestConfig(Config):
    """测试配置"""
    echo = True  # SQLAlchemy配置，是否在命令行打印SQL语句


class ProdConfig(Config):
    """生产配置"""
    echo = False  # SQLAlchemy配置，是否在命令行打印SQL语句


config = {
    'test': TestConfig,
    'prod': ProdConfig
}
