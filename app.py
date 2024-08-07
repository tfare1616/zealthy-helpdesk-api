import os
from flask import Flask


POSTRESQL_URL = os.environ.get('API_URL')


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'application/json'
app.config['SQLALCHEMY_DATABASE_URI'] = POSTRESQL_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
