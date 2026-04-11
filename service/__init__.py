from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Apply security headers using Talisman
    talisman = Talisman(app)

    return app
