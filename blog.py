from flask import Flask, request

from flask_restful import Resource, Api

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

