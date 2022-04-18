from config.config import connect


class ProvidersDAO:
    def __init__(self):
        connect(self)

    # Methods to create/manage providers go here

    #1 - Query to add a new provider to the providers table with a json
    def addNewProvider(self, pname, pemail, ppass, ploc):
        cursor = self.conn.cursor()
        query = "insert into providers (pname, pemail, ppass, ploc) values (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (pname, pemail, ppass, ploc))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    #2 - Query to get a json representation of all providerps registered in db
    def getAllProviders(self):
        cursor = self.conn.cursor()
        query = "select pid, pname, pemail, ppass, ploc from providers;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #3 - Query to search for a specific row in the providers table by u_id (provider id)
    def getProviderById(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pemail, ppass, ploc from providers where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    #4 - Query to update an existing provider's information on the providers table when given a json
    def updateProviderById(self, pid, pname, pemail, ppass, ploc):
        cursor = self.conn.cursor()
        query = "update providers set pname = %s, pemail=%s, ppass=%s, ploc=%s where pid=%s;"
        cursor.execute(query, (pname, pemail, ppass, pid, ploc))
        self.conn.commit()
        return True

    #5 - Query to delete a provider, with a specified u_id, from the providers table
    def deleteProviderById(self, pid):
        cursor = self.conn.cursor()
        query = "delete from providers where pid = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return True