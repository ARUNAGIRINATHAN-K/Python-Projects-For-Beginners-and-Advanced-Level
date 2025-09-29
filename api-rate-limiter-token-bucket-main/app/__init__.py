from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes
    from app.routes import app as routes_app
    app.register_blueprint(routes_app)

    return app
