from config.config import connect


class UsersDAO:
    def __init__(self):
        connect(self)

    # Methods to create/manage users go here

    #1 - Query to add a new user to the users table with a json
    def addNewUser(self, uname, uemail, upass, uloc):
        cursor = self.conn.cursor()
        query = "insert into users (uname, uemail, upass, uloc) values (%s, %s, %s, %s) returning uid;"
        cursor.execute(query, (uname, uemail, upass, uloc))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    #2 - Query to get a json representation of all users registered in db
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, uname, uemail, upass, uloc from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #3 - Query to search for a specific row in the users table by u_id (user id)
    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, uname, uemail, upass, uloc from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    #4 - Query to update an existing user's information on the users table when given a json
    def updateUserById(self, uid, uname, uemail, upass, uloc):
        cursor = self.conn.cursor()
        query = "update users set uname = %s, uemail=%s, upass=%s, uloc=%s where uid=%s;"
        cursor.execute(query, (uname, uemail, upass, uid, uloc))
        self.conn.commit()
        return True

    #5 - Query to delete a user, with a specified u_id, from the users table
    def deleteUserById(self, uid):
        cursor = self.conn.cursor()
        query = "delete from users where uid = %s;"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return True