from flask import jsonify
from model.users import UsersDAO


class Users:

    def build_attr_dict(self, uid, uname, uemail, upass, uloc):
        result = {}
        result['uid'] = uid
        result['uname'] = uname
        result['uemail'] = uemail
        result['upass'] = upass
        result['uloc'] = uloc
        return result

    def build_map_dict(self, row):
        result = {}
        result["uid"] = row[0]
        result["uname"] = row[1]
        result["uemail"] = row[2]
        result["upass"] = row[3]
        result["uloc"] = row[3]
        return result

    # User management methods go here:

    #1 - Inserts new user to users table with parameters given by client
    def addNewUser(self, json):
        uname = json['uname']
        uemail = json['uemail']
        upass = json['upass']
        uloc = json['uloc']
        dao = UsersDAO()
        uid = dao.addNewUser(uname, uemail, upass, uloc)
        result = self.build_attr_dict(uid, uname, uemail, upass, uloc)
        return jsonify(result), 201

    #2 - Gets all users currently registered in users table
    def getAllUsers(self):
        dao = UsersDAO()
        user_l = dao.getAllUsers()
        result_l = []
        for row in user_l:
            obj = self.build_map_dict(row)
            result_l.append(obj)
        return jsonify(result_l), 200

    #3 - Gets a specific user by specifying their user id (u_id)
    def getUserById(self, uid):
        dao = UsersDAO()
        user_tup = dao.getUserById(uid)
        if not user_tup:  # means that is null if true and not null if false
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(user_tup)
        return jsonify(result), 200

    #4 - Updates an existing user's information
    def updateUserById(self, json):
        uname = json['uname']
        uemail = json['uemail']
        upass = json['upass']
        uloc = json['uloc']
        uid = json['uid']
        dao = UsersDAO()
        updated_user = dao.updateUserById(uid, uname, uemail, upass, uloc)
        result = self.build_attr_dict(uid, uname, uemail, upass, uloc)
        return jsonify(result), 200

    #5 - Deletes an existing user from the users table
    def deleteUserById(self, uid):
        dao = UsersDAO()
        result = dao.deleteUserById(uid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404