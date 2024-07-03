from flask_cors import CORS
from app import app
from db import db

cors = CORS(app)


with app.app_context():
    db.create_all()

