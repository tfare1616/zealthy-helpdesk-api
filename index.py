from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'application/json'
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
@cross_origin()
def get_tickets():
    tickets = Ticket.query.all()
    ticket_data = []

    for ticket in tickets:
        data = {'name': ticket.name,
                'description': ticket.description,
                'status': ticket.status,
                'email': ticket.email,
                'subject': ticket.subject,
                'id': ticket.id
                }
        ticket_data.append(data)

    return {'Tickets': ticket_data}


@app.route('/submitTickets', methods=['POST'])
@cross_origin()
def submit_tickets():
    ticket = Ticket(name=request.json['name'], email=request.json['email'], description=request.json['description'], status=request.json['status'], subject=request.json['subject'])
    db.session.add(ticket)
    db.session.commit()
    return Response("{'error':'false'}", status=200, mimetype='application/json')


@app.route('/editTickets', methods=['PUT'])
@cross_origin()
def edit_tickets():
    ticket = Ticket.query.get(request.json['id'])
    ticket.status = request.json['status']
    db.session.commit()
    return Response("{'error':'false'}", status=200, mimetype='application/json')


@app.route('/deleteTickets', methods=['PUT'])
@cross_origin()
def delete_tickets():
    ticket = Ticket.query.get(request.json['id'])
    db.session.delete(ticket)
    db.session.commit()
    return Response("{'error':'false'}", status=200, mimetype='application/json')