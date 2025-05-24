from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymongo

app = Flask(__name__)

api = Api(app)

client = pymongo.MongoClient("mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
mydb = client["mydatabase"]
myposts = mydb["posts"]
myusers = mydb["users"]
mydata = mydb["data"]

data_retrieve = mydata.find_one({"_id": "0"})
postID = int(data_retrieve["postID"])
userID = int(data_retrieve["userID"])

class postsearch(Resource):

    def get(self):
        postid = request.args.get('postid')
        found_post = myposts.find_one({"_id": int(postid)})
        return jsonify(found_post)

    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201


class usercreate(Resource):
    
    def newUser(nickname, password, description, isMod, rep, isBanned, isAdmin, nameColour, isTest):
        global userID
        myusers.insert_one({"_id": userID, "name": nickname, "pass": password, "desc": description, "mod": isMod, "rep": rep, "ban": isBanned, "admin": isAdmin, "namecol": nameColour, "test": isTest})
        userID += 1
        mydata.update_one({"_id": "0"}, {"$set": {"userID": str(userID)}})
    def get(self):
        try:
            nickname = request.args.get('user')
            password = request.args.get('pass')
            newUser(nickname, password, "nothing", False, 5, False, False, "white", False)
            return jsonify({"message": "success"})
        except Exception as e:
            return jsonify({"message": "error"})
    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
api.add_resource(postsearch, '/post')
api.add_resource(usercreate, "/user")
