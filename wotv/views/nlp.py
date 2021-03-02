
from flask_restful import Resource, Api
from flask import jsonify





class Nlp(Resource):

    def get(self):

        return jsonify({'result'})

def init_app(app):
    nlp = Api(app)
    nlp.add_resource(Nlp, "/nlp", methods=['VIEW', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                     endpoint='nlp')
    return nlp
