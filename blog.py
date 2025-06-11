from flask import Flask, request

from flask_restful import Resource, Api

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api = Api(app)

blogs = {}

class BlogList(Resource):
    def get(self):
        return blogs
    
    def post(self):

        blog_id = len(blogs) + 1

        blogs[blog_id] = request.json['blog_title']

        return {blog_id: blogs[blog_id]}, 201
    
class BlogResource(Resource):
    def get(self, blog_id):

        return {blog_id: blogs[blog_id]}
    
    def put(self, todo_id):

        blogs[blog_id] = request.json['blog_title']

        return {blog_id: blogs[blog_id]}
    
    def delete(self, blog_id):

        del blogs[blog_id]

        return '', 204
    
api.add_resource(BlogList, '/blogs')
api.add_resource(BlogResource, '/blog/<int:blog_id>')

if __name__ == '__main__':

    app.run(debug=True)

