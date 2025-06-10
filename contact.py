from flask import Flask, request

from flask_restful import Resource, Api

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api = Api(app)

contacts = {}

class ContactsList(Resource):
    def get(self):
        return contacts
    
    def post(self):

        contact_id = len(contacts) + 1

        contacts[contact_id] = request.json['contact']

        return {contact_id: contacts[contact_id]}, 201
    
class ContactsResource(Resource):
    def get(self, contact_id):

        return {contact_id: contacts[contact_id]}
    
    def put(self, contact_id):
    
        contacts[contact_id] = request.json['contact']

        return {contact_id: contacts[contact_id]}
    
    def delete(self, contact_id):

        del contacts[contact_id]

        return '', 204
    
api.add_resource(ContactsList, '/contacts')
api.add_resource(ContactsResource, '/contacts/<int:contact_id>')

if __name__ == '__main__':

        app.run(debug=True)


