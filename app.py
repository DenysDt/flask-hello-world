from flask import Flask, jsonify, request, render_template
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
        client = pymongo.MongoClient("mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
        mydb = client["mydatabase"]
        myusers = mydb["users"]
        mydata = mydb["data"]

        data_retrieve = mydata.find_one({"_id": "0"})
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
        client = pymongo.MongoClient("mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
        mydb = client["mydatabase"]
        myposts = mydb["posts"]
        myusers = mydb["users"]
        mydata = mydb["data"]

        data_retrieve = mydata.find_one({"_id": "0"})
        try:
            user = request.args.get('user')
            contents = request.args.get('contents')
            postID = int(data_retrieve["postID"])
            userpass = request.args.get('password')
            if myusers.find_one({"name": {"$eq": user}}):
                user_retrieve = myusers.find_one({"name": user})
                if userpass == user_retrieve["pass"]:
                    myposts.insert_one({"_id": postID, "contents": contents, "user": user})
                    postID += 1
                    mydata.update_one({"_id": "0"}, {"$set": {"postID": str(postID)}})
                    return jsonify({"message": "success"})
                else:
                    return jsonify({"message": "!pass"})
            else:
                return jsonify({"message": "!user"})

        except Exception as e:
            print(f"ERROR: {e}")
            return jsonify({"message": "error"})

    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201

class freejob(Resource):

    def get(self):
        return "The fuck u expect🙏🙏🙏  Bro's getting scammed so easily🤞❌❌"

    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201



class preBattleShipsRequest(Resource):

    def get(self):
        client = pymongo.MongoClient("mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
        mydb = client["mydatabase"]
        mybattles = client["battles"]

        #data_retrieve = mydata.find_one({"_id": "0"})
        try:
            ships = request.args.get('ships')
            battleid = request.args.get("battleid")
            playerid = request.args.get("playerid")
            amount = ships.count(",")
            x = ships.partition(",")
            xlen = len(x[0])
            if xlen != 2:
                print(f"Error! Square {x[0]} doesn't exist!")
                return jsonify({"message": "error"})
            else:
                if x[0][0] == "A" or x[0][0] == "B" or x[0][0] == "C" or x[0][0] == "D":
                    if x[0][1] == "1" or x[0][1] == "2" or x[0][1] == "3" or x[0][1] == "4":
                        ...
                    else:
                        print(f"Error! Square {x[0]} doesn't exist!")
                        return jsonify({"message": "error"})
                else:
                    print(f"Error! Square {x[0]} doesn't exist!")
                    return jsonify({"message": "error"})

            

            for loop in range(amount):
                x = x[2].partition(",")
                xlen = len(x[0])
                if xlen != 2:
                    print(f"Error! Square {x[0]} doesn't exist!")
                    return jsonify({"message": "error"})
                else:
                    if x[0][0] == "A" or x[0][0] == "B" or x[0][0] == "C" or x[0][0] == "D":
                        if x[0][1] == "1" or x[0][1] == "2" or x[0][1] == "3" or x[0][1] == "4":
                            ...
                        else:
                            print(f"Error! Square {x[0]} doesn't exist!")
                            return jsonify({"message": "error"})
                    else:
                        print(f"Error! Square {x[0]} doesn't exist!")
                        return jsonify({"message": "error"})

                if true:
                    ...
                mybattles.update_one({"_id": battleid}, {"$set": {x[0]: str(postID)}})

            return jsonify({"message": "success"})


        except Exception as e:
            print(f"ERROR: {e}")
            return jsonify({"message": "error"})

    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201




@app.route("/")
def index():
    return render_template("aperture.html")


api.add_resource(health, "/health")
#api.add_resource(postsearch, '/post')
#api.add_resource(usercreate, "/signup")
#api.add_resource(login, "/login")
#api.add_resource(postcreate, "/postcreate")
#api.add_resource(freejob, "/freejob")


