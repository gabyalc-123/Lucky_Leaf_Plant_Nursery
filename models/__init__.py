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
        from .users import Users
        from .products import Products
        from .planttypes import PlantTypes
        from .orders import Orders
        from .orderItems import OrderItems
        from .careInstructions import CareInstructions
        db.create_all()
        db.session.commit()
        app.logger.debug('All tables are created')

