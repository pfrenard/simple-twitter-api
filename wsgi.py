"""
    wsgi.py
"""

from app import create_app

APPLICATION = create_app()
if __name__ == '__main__':
    APPLICATION.run(debug=True)
