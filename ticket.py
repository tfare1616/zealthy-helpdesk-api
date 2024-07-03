from db import db
from app import app

with app.app_context():
    db.create_all()


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    description = db.Column(db.String(500))
    subject = db.Column(db.String(80))
    status = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.name} - {self.email} - {self.description}"


ticket = Ticket
