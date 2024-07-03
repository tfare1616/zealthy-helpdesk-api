import os
from flask import Flask


POSTRESQL_URL = os.environ.get('API_URL')


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'application/json'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://neondb_owner:4qi5PguEWhol@ep-bitter-feather-a5gxsums.us-east-2.aws.neon.tech/neondb?sslmode=require'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
