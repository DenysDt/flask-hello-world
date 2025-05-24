from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymongo

app = Flask(__name__)

api = Api(app)

client = pymongo.MongoClient("mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/")
mydb = client["mydatabase"]
myposts = mydb["posts"]

class Hello(Resource):

    def get(self):
        postid = request.args.get('postid')
        found_post = myposts.find_one({"_id": postid})
        return jsonify(found_post)

    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
api.add_resource(Hello, '/')
