from app import create_app,db
from app.models import User
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand



@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
if __name__ == '__main__':
    manager.run()