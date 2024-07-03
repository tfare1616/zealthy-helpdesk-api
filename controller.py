# from flask import request, Response
# from flask_cors import CORS, cross_origin
# import app
# from db import db
# from ticket import Ticket
#
#
# @app.route('/tickets')
# @cross_origin()
# def get_tickets():
#     tickets = Ticket.query.all()
#     ticket_data = []
#
#     for ticket in tickets:
#         data = {'name': ticket.name,
#                 'description': ticket.description,
#                 'status': ticket.status,
#                 'email': ticket.email,
#                 'subject': ticket.subject,
#                 'id': ticket.id
#                 }
#         ticket_data.append(data)
#
#     return {'Tickets': ticket_data}
#
#
# @app.route('/submitTickets', methods=['POST'])
# @cross_origin()
# def submit_tickets():
#     ticket = Ticket(name=request.json['name'], email=request.json['email'], description=request.json['description'], status=request.json['status'], subject=request.json['subject'])
#     db.session.add(ticket)
#     db.session.commit()
#     return Response("{'error':'false'}", status=200, mimetype='application/json')
#
#
# @app.route('/editTickets', methods=['PUT'])
# @cross_origin()
# def edit_tickets():
#     ticket = Ticket.query.get(request.json['id'])
#     ticket.status = request.json['status']
#     db.session.commit()
#     print('to: ' + ticket.email)
#     print('re status change to ' + ticket.subject)
#     print('Your ticket is now marked as ' + ticket.status)
#     return Response("{'error':'false'}", status=200, mimetype='application/json')
#
#
# @app.route('/deleteTickets', methods=['PUT'])
# @cross_origin()
# def delete_tickets():
#     ticket = Ticket.query.get(request.json['id'])
#     db.session.delete(ticket)
#     db.session.commit()
#     return Response("{'error':'false'}", status=200, mimetype='application/json')
#
#
# @app.route('/requestComments', methods=['PUT'])
# @cross_origin()
# def request_comments():
#     ticket = Ticket.query.get(request.json['id'])
#     db.session.commit()
#     print('to: ' + ticket.email)
#     print('re additional information has been requested on ' + ticket.subject)
#     print(request.json['comment'])
#     return Response("{'error':'false'}", status=200, mimetype='application/json')