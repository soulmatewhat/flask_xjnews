from news.info import create_app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager


# 创建 app，并传入配置模式：dev(开发) / prod(生产)
app = create_app('dev')
#Flask-script
manager = Manager(app)
#数据库迁移
Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    #如果pycharm启动需要配置runserver
    manager.run()