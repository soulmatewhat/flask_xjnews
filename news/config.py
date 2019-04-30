import logging

import redis


class Config(object):
    """
    配置信息
    """
    SECRET_KEY = 'EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA'
    DEBUG=True
    #数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    #flask的session配置
    SESSION_TYPE = 'redis'#指定session保存到redis中
    SESSION_USE_SIGNER = True    #让cookie 中的session_id被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)# redis实例
    PERMANENT_SESSION_LIFETIME = 86400#session 有效期 单位秒


class DevelopementConfig(Config):
    """开发环境配置类
    如果开发环境的配置和父类一致，可以直接pass
    """
    DEBUG = True

    # 开发环境的日志等级为调试模式
    LOGGING_LEVEL = logging.DEBUG

class ProductionConfig(Config):
    """生产环境配置类
    实际开发中，需要额外配置生产环境下的数据库和其他的信息
    """
    DEBUG = False

    # 生产环境的日志等级为调试模式
    LOGGING_LEVEL = logging.WARNING

#定义配置字典
configs = {
    "dev":DevelopementConfig,
    "prod":ProductionConfig
}