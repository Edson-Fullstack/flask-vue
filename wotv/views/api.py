import flask
from flask import jsonify, request
from flask_restful import Resource, Api
from dynaconf import settings
import dataset
from stuf import stuf
from sqlalchemy.sql import text
from psycopg2 import OperationalError, errorcodes, errors


def configure():
    db = dataset.connect(settings.POSTGRES_URI, row_type=stuf)
    if isinstance(db.tables,list) > 0:
        return db

#process will die if the string connection is wrong
db = configure()


class Appi(Resource):
    def access(tabela):
        if db['apis'].count(tables=tabela) > 0:
            return True

    def anti_injection(params):
        words = ["$", "*", "SELECT", "DROP"]
        for w in words:
            params = params.replace(w, "")
        return params

    def view(self, database):
        """ver campos da tabela"""
        result = []
        result.append("indexes:" + str(db[database]._indexes))
        for dado in db[database].table.columns.values():
            result.append(dado.key + ":" + str(dado.type))
        return result

    def get(self, database):
        """Return list and 1 element fitered by string query"""
        result = []
        print(request.headers)
        if Appi.access(database):
            params = Appi.anti_injection(request.query_string.decode("utf-8"))
            if params is None or params == '':
                response = flask.Response()
                response.headers['Autorization'] = ''
                for row in db[database].all():
                    result.append(row)

                return jsonify(result)
            else:
                statment = params.replace("&", " AND ").replace("%22", "").replace("%27", "'").replace("|",
                                                                                                       " OR ").replace(
                    "%20", " ")
                try:
                    for row in db[database].find(text(statment)):
                        result.append(row)
                    return jsonify(result)
                except:
                    return "{errors:" + str(500) + "," + "Invalid Statment:" + statment + "}", 500

    def post(self, database):
        """Add one element"""
        data = dict(request.get_json(force=True))
        print(data)
        result = db[database].insert(data)
        return {result: data}

    def patch(self, database):
        """Update"""
        params = self.anti_injection(request.query_string.decode("utf-8"))
        statment = params.replace("&", " AND ").replace("%22", "").replace("%27", "'").replace("|", " OR ").replace(
            "%20", " ")
        data = dict(request.get_json(force=True))
        results = []
        if statment != "":
            result = db[database].update(data, keys=statment.split("=")[0])
            for row in db[database].find(text(statment)):
                results.append(row)
        return {result: results}

    def put(self, database):
        """Upsert """
        params = Appi.anti_injection(request.query_string.decode("utf-8"))
        statment = params.replace("&", " AND ").replace("%22", "").replace("%27", "'").replace("|", " OR ").replace(
            "%20", " ")
        data = dict(request.get_json(force=True))
        print(request.headers)
        results = []
        response = flask.Response()
        response.headers['Authorization'] = 'a'
        if statment == "":
            result = db[database].upsert(data, keys=['name'])
            for row in db[database].find(text(statment)):
                results.append(row)
            return {result: results}
        response.data=''
        return response

    def delete(self, database):
        """Delete a item"""
        params = self.anti_injection(request.query_string.decode("utf-8"))
        statment = params.replace("&", " AND ").replace("%22", "").replace("%27", "'").replace("|", " OR ").replace(
            "%20", " ")
        data = dict(request.get_json(force=True))
        results = []
        if statment != "":
            for row in db[database].find(text(statment)):
                results.append(row)
            result = db[database].delete(text(statment))
        return {result: results}


def init_app(app):
    api = Api(app)
    api.add_resource(Appi, "/api/<string:database>", methods=['VIEW', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                     endpoint='api')
    return api
