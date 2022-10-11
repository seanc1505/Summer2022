from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from flask_mail import Mail
# from webui.config import Config

# db = SQLAlchemy()
# bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'
# mail = Mail()


# def create_app(config_class=Config):
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '33f1ae20b4a0d78c4d3eb6ecdce3fb1a'
    # app.config.from_object(Config)

    # db.init_app(app)
    # bcrypt.init_app(app)
    # login_manager.init_app(app)
    # mail.init_app(app)

    # from webui.users.routes import users
    # from webui.posts.routes import posts
    from webui.main.routes import main
    # from webui.errors.handlers import errors
    # app.register_blueprint(users)
    # app.register_blueprint(posts)
    app.register_blueprint(main)
    # app.register_blueprint(errors)

    return app