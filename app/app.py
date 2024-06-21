from flask import Flask


def create_app():
    """工厂函数，创建并配置Flask应用实例"""
    app = Flask(
        __name__, template_folder='../template',
        static_url_path='/', static_folder='../resource'
    )

    return app
