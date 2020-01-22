"""
    app/__init__.py
"""

from flask import Flask

def create_app():
    """
        create_app
    """
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        """
            Hello World :)
        """
        return "Hello World!"

    return app
