# __init__.py
from flask import Flask
from HelloWorld.blueprints.main import main_bp


def create_app():
    app = Flask('HelloWorld')
    app.register_blueprint(main_bp)

    return app


