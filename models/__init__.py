from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    # Configure the DB here or in app.py
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'db': "sqlite:///luckyleafplants_.sqlite"
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luckleafplants_.sqlite'

    db.init_app(app)
    app.logger.info('Initialized models')

    with app.app_context():
        from .Users import Users
        from .Products import Products
        from .PlantTypes import PlantTypes
        from .Orders import Orders
        from .OrderItems import OrderItems

