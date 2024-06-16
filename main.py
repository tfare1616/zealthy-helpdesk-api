from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    description = db.Column(db.String(500))
    subject = db.Column(db.String(80))
    status = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.name} - {self.email} - {self.description}"


@app.route('/')
def index():
    return 'test'


@app.route('/tickets')
def get_tickets():
    tickets = Ticket.query.all()
    ticket_data = []

    for ticket in tickets:
        data = {'name': ticket.name,
                'description': ticket.description,
                'status': ticket.status,
                'email': ticket.email,
                'subject': ticket.subject
                }
        ticket_data.append(data)

    return {'Tickets': ticket_data}
