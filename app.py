import os

from flask import Flask
from dotenv import load_dotenv
from extensions import mail, login_manager, db
from models.member import Member, member_role, Role
from models.projects import VidEditProject
from models.tool import Tools
from routes.main import main
from routes.account import account
from routes.manager import manager


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///writart.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)
db.init_app(app)
login_manager.init_app(app)


app.register_blueprint(main, url_prefix='/')
app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(manager, url_prefix='/manager')


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(member_id):
    return db.get_or_404(Member, member_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)