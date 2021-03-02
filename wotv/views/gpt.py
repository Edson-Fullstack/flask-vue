
from flask_restful import Resource, Api
from flask import jsonify
#from gpt2_client import GPT2Client

#gpt2 = GPT2Client('117M')  # This could also be `345M`, `774M`, or `1558M`. Rename `save_dir` to anything.
#gpt2.load_model(force_download=False)  # Use cached versions if available

class Gpt(Resource):

    def get(self):

        prompts = [
            "RPG"
        ]
        text = ""
        #text = gpt2.generate_batch_from_prompts(prompts)  # returns an array of generated text
        return jsonify({'result': text})

def init_app(app):
    gpt = Api(app)
    gpt.add_resource(Gpt, "/gpt", methods=['VIEW', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                     endpoint='gpt')
    return gpt
