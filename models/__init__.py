from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    # Configure the DB here or in app.py
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'db': "sqlite:///clothing_.sqlite"
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clothing_.sqlite'

    db.init_app(app)
    app.logger.info('Initialized models')