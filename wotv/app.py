"""
PEP 8 -- Style Guide for Python Resume
pip8 src
"""
import os
from flask import Flask
from wotv.extensions import configuration
from wotv.views import view, api, nlp#,gpt


#definicoues de preferencias de delimitadores
app = Flask(__name__)
app.jinja_env.block_start_string = "[%"
app.jinja_env.block_end_string = "%]"
app.jinja_env.variable_start_string = "[["
app.jinja_env.variable_end_string = "]]"

#aplicação de extensoes
configuration.init_app(app)

#factory nos modulos do projeto
#gpt.init_app(src)
nlp.init_app(app)
api.init_app(app)
view.init_app(app)

if __name__ == "__main__":
    # rodar src no local host(host='localhost', port=80,debug=True)
    # ter apenas 1 servidor respodendo na porta 80
    # ssl_context='adhoc'
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
