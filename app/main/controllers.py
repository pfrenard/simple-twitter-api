"""
    app/main/controllers.py
"""
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/hello')
def home():
    """
        home
    """
    return "Goodbye"
