from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
import pymongo
import uuid

app = Flask(__name__)

api = Api(app)

client = pymongo.MongoClient(
    "mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
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
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


class usercreate(Resource):
    def get(self):
        client = pymongo.MongoClient(
            "mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
        mydb = client["mydatabase"]
        myusers = mydb["users"]
        mydata = mydb["data"]

        data_retrieve = mydata.find_one({"_id": "0"})
        try:
            user = request.args.get('user')
            password = request.args.get('password')
            userID = int(data_retrieve["userID"])
            myusers.insert_one(
                {"_id": userID, "name": user, "pass": password, "desc": "bio", "mod": False, "rep": 5, "ban": False,
                 "admin": False, "namecol": "white", "test": "False"})
            userID += 1
            mydata.update_one({"_id": "0"}, {"$set": {"userID": str(userID)}})
            return jsonify({"message": "success"})
        except Exception as e:
            print(f"ERROR: {e}")
            return jsonify({"message": "error"})

    def post(self):
        data = request.get_json()  # status code
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
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


class health(Resource):

    def get(self):
        return "Hello!"

    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


class postcreate(Resource):

    def get(self):
        client = pymongo.MongoClient(
            "mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
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
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


class freejob(Resource):

    def get(self):
        return "The fuck u expect🙏🙏🙏  Bro's getting scammed so easily🤞❌❌"

    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


class preBattleShipsRequest(Resource):

    def get(self):
        client = pymongo.MongoClient("mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
        mydb = client["mydatabase"]
        mybattles = mydb["battles"]

        # data_retrieve = mydata.find_one({"_id": "0"})
        try:
            ships = request.args.get('ships')
            battleid = request.args.get("battleid")
            playerid = request.args.get("playerid")
            squares_info = mybattles.find_one({"_id": battleid})
            amount = ships.count(",")
            x = ships.partition(",")
            if mybattles.find_one({"squares": {"$eq": x[0]}}):
                if squares_info["squares"][x[0]][playerid] == "false":
                    mybattles.update_one({"_id": battleid}, {"$set": {x[0]: {playerid: "true"}}})
            else:
                return jsonify({"message": "error"})

            for loop in range(amount):
                x = x[2].partition(",")

                if mybattles.find_one({"squares": {"$eq": x[0]}}):
                    if squares_info["squares"][x[0]][playerid] == "false":
                        mybattles.update_one({"_id": battleid}, {"$set": {x[0]: {"EnemyShip": "true"}}})
                else:
                    return jsonify({"message": "error"})


            return jsonify({"message": "success"})


        except Exception as e:
            print(f"ERROR: {e}")
            return jsonify({"message": "error"})

    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


class battlejoin(Resource):

    def get(self):
        client = pymongo.MongoClient("mongodb+srv://DenysDt:bGbPB4bFVK3L8MU@cluster0.1xcwxnh.mongodb.net/?retryWrites=true&w=majority")
        mydb = client["mydatabase"]
        mybattles = mydb["battles"]


        battleid = request.args.get("battleid")
        if mybattles.find_one({"_id": {"$eq": battleid}}):
            battle_data = mybattles.find_one({"_id": battleid})
            if battle_data["players"] >= 2:
                return jsonify({"message": "!full"})
            else:
                if battle_data["players"] == 0:
                    userid_gen = str(uuid.uuid4())
                    players_count = battle_data["players"]
                    players_count += 1
                    mydata.update_one({"_id": battleid}, {"$set": {"players": players_count}})
                    mydata.update_one({"_id": battleid}, {"$set": {"player1": userid_gen}})
                    return jsonify({"message": "success", "gen_userid": userid_gen})
                elif battle_data["players"] == 1:
                    userid_gen = str(uuid.uuid4())
                    players_count = battle_data["players"]
                    players_count += 1
                    mydata.update_one({"_id": battleid}, {"$set": {"players": players_count}})
                    mydata.update_one({"_id": battleid}, {"$set": {"player2": userid_gen}})
                    return jsonify({"message": "success", "gen_userid": userid_gen})

                else:
                    return jsonify({"message": "!full"})


        else:
            return jsonify({"message": "!code"})


    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201



@app.route("/")
def index():
    return render_template("aperture.html")


api.add_resource(health, "/health")
# api.add_resource(postsearch, '/post')
# api.add_resource(usercreate, "/signup")
# api.add_resource(login, "/login")
# api.add_resource(postcreate, "/postcreate")
# api.add_resource(freejob, "/freejob")
api.add_resource(battlejoin, "/battlejoin")
api.add_resource(preBattleShipsRequest, "/battleshipsreq")
