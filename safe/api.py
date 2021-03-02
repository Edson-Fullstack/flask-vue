from flask_restful import Resource, Api 

class API(Resource):
    def get(self,database,parameters=None):
        return {database: parameters } 
    
    def post(self,database):
        return {database:'post'}