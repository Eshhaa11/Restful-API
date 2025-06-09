from flask import Flask, request

from flask_restful import Resource, Api

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api = Api(app)

users = {}

class UsersList(Resource):

    def get(self):

        return users

    def post(self):
        users_id = len(users) + 1

        users[users_id] = request.json['users_name']


        return {users_id: users[users_id]}, 201

api.add_resource(UsersList, '/users')

if __name__ == '__main__':

    app.run(debug=True)