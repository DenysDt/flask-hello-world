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
    def get(self):
        try:
            user = request.args.get('user')
            password = request.args.get('password')
            userID = int(data_retrieve["userID"])
            myusers.insert_one({"_id": userID, "name": user, "pass": password, "desc": "bio", "mod": False, "rep": 5, "ban": False, "admin": False, "namecol": "white", "test": "False"})
            userID += 1
            mydata.update_one({"_id": "0"}, {"$set": {"userID": str(userID)}})
            return jsonify({"message": "success"})
        except Exception as e:
            print(f"ERROR: {e}")
            return jsonify({"message": "error"})
    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201


class login(Resource):

    def get(self):
        user = request.args.get('user')
        password = request.args.get('password')
        if myusers.find_one({"name": {"$eq": user}}):
            user_retrieve = myusers.find_one({"name": user})
            if password == user_retrieve["pass"]:
                return jsonify(user_retrieve)
            else:
                return jsonify({"message": "!pass"})
        else:
            return jsonify({"message": "!user"})
            

    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201

class health(Resource):

    def get(self):
        return "Hello!"

    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201


class postcreate(Resource):

    def get(self):
        try:
            user = request.args.get('user')
            contents = request.args.get('contents')
            postID = int(data_retrieve["postID"])
            myposts.insert_one({"_id": postID, "contents": contents, "user": user})
            postID += 1
            mydata.update_one({"_id": "0"}, {"$set": {"postID": str(postID)}})
            return jsonify({"message": "success"})

        except Exception as e:
            print(f"ERROR: {e}")
            return jsonify({"message": "error"})

    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201



api.add_resource(postsearch, '/post')
api.add_resource(usercreate, "/signup")
api.add_resource(login, "/login")
api.add_resource(health, "/health")

