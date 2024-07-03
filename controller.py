

def get_tickets(Ticket):
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