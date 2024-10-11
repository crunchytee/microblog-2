from flask_bootstrap import Bootstrap5
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.posts import Posts

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"
posts = Posts("posts.json")

from app import routes, models