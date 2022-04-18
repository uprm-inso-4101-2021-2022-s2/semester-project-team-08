from flask import jsonify
from model.providers import ProvidersDAO


class Providers:

    def build_attr_dict(self, pid, pname, pemail, ppass, ploc):
        result = {}
        result['pid'] = pid
        result['pname'] = pname
        result['pemail'] = pemail
        result['ppass'] = ppass
        result['ploc'] = ploc
        return result

    def build_map_dict(self, row):
        result = {}
        result["pid"] = row[0]
        result["pname"] = row[1]
        result["pemail"] = row[2]
        result["ppass"] = row[3]
        result["ploc"] = row[3]
        return result

    # Provider management methods go here:

    #1 - Inserts new provider to providers table with parameters given by client
    def addNewProvider(self, json):
        pname = json['name']
        pemail = json['email']
        ppass = json['pass']
        ploc = json['loc']
        dao = ProvidersDAO()
        pid = dao.addNewProvider(pname, pemail, ppass, ploc)
        result = self.build_attr_dict(pid, pname, pemail, ppass, ploc)
        return jsonify(result), 201

    #2 - Gets all providers currently registered in providers table
    def getAllProviders(self):
        dao = ProvidersDAO()
        provider_l = dao.getAllProviders()
        result_l = []
        for row in provider_l:
            obj = self.build_map_dict(row)
            result_l.append(obj)
        return jsonify(result_l), 200

    #3 - Gets a specific provider by specifying their provider id (u_id)
    def getProviderById(self, pid):
        dao = ProvidersDAO()
        provider_tup = dao.getProviderById(pid)
        if not provider_tup:  # means that is null if true and not null if false
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(provider_tup)
        return jsonify(result), 200

    #4 - Updates an existing provider's information
    def updateProviderById(self, json):
        pname = json['name']
        pemail = json['email']
        ppass = json['pass']
        ploc = json['loc']
        pid = json['pid']
        dao = ProvidersDAO()
        updated_provider = dao.updateProviderById(pid, pname, pemail, ppass, ploc)
        result = self.build_attr_dict(pid, pname, pemail, ppass, ploc)
        return jsonify(result), 200

    #5 - Deletes an existing provider from the providers table
    def deleteProviderById(self, pid):
        dao = ProvidersDAO()
        result = dao.deleteProviderById(pid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404