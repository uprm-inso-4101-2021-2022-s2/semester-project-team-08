import os
import sys

from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from controller.users import Users
from controller.providers import Providers

app = Flask(__name__)
CORS(app)


# @app.route("/")
# def foo():
#     return render_template("public/index.html")

# User management routes go here:
@app.route("/", methods=["GET", "POST"])
def landing():
    if request.method == "POST":
        req = request.form
        utype = req.get('user_type')
        if utype == "1":
            Users().addNewUser(req)
        elif utype == "2":
            Providers().addNewProvider(req)

        return redirect(request.url)
    return render_template("public/index.html")

# User management routes go here:
@app.route("/profile/users", methods=["GET", "POST"])
def handleUser():
    if request.method == "POST":
        #Adds a new user with name, email and password inputed via a json
        return Users().addNewUser(request.json)
    elif request.method == "GET":
        #Gets a json representation of all users currently in table: users
        return Users().getAllUsers()
    else:
        return jsonify("Method not allowed"), 405

@app.route("/profile/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def handleUsersById(uid):
    if request.method == "GET":
        #Gets a specific user by matching them with a given uid
        return Users().getUserById(uid)
    elif request.method == "PUT":
        #Updates an existing users information by giving a json file with uname, uemail, upassword, uid, and uloc
        return Users().updateUserById(request.json)
    elif request.method == "DELETE":
        #Given a uid, Deletes a specified user with a matching uid
        return Users().deleteUserById(uid)
    else:
        return jsonify("Method not allowed"), 405



if __name__ == "__main__":
    app.run(debug=True)
