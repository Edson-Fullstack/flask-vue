"""
PEP 8 -- Style Guide for Python Resume
pip8 src
"""
import os
from flask import Flask, render_template, url_for, request, send_file, jsonify
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api 
#from api import API
app = Flask(__name__)

app.debug=True
app.jinja_env.block_start_string = "[%"
app.jinja_env.block_end_string = "%]"
app.jinja_env.variable_start_string = "[["
app.jinja_env.variable_end_string = "]]"

app.config['TITLE']='Game Database'

Bootstrap(app)
#api = Api(src)


#api.add_resource(API,"/api/<string:database>","/api/<string:database>/<parameters>",endpoint = 'api')

# home page
@app.route("/")
def index():
    target = os.environ.get('TARGET', 'World')
    language = request.accept_languages.best_match(['en', 'pt'])
    if language == 'pt' or language == 'en':
        test="paralelepipedo"
        graph = {
            "devops": 100,
            "label0": "Dev-Ops",
            "design": 90,
            "label1": "Design",
            "frontend":80,
            "label2": "Frontend",
            "backend": 70,
            "label3": "Backend",
            "tests": 60,
            "label4": "Tests",
            "security": 50,
            "label5": "Security"
        }
        total = {'devops': round(
            sum(graph['devops'].values())/len(graph['devops']), 2),
            'design': round(
            sum(graph['design'].values())/len(graph['design']), 2),
            'frontend': round(
            sum(graph['frontend'].values())/len(graph['frontend']), 2),
            'backend': round(
            sum(graph['backend'].values())/len(graph['backend']), 2),
            'tests': round(
            sum(graph['tests'].values())/len(graph['tests']), 2),
            'security': round(
            sum(graph['security'].values())/len(graph['security']), 2),
        }

        label = ['Contato', 'Habilidades', 'Experiencia', 'Educação']
        info = {"sname": "Edson",
                "fone": "(32)998087750",
                "email": "edson.fullstack@gmail.com",
                "linkedin": "linkedin.com/in/bendavis78",
                "name": "Edson Coelho dos Santos", "desc": "Eu sou foda demais",
                "image": "/static/images/perfil.png",
                "objetivo": "ras para gerar valor para os clientes.",
                "formacao": ["""Graduação em Ciência da Computação pela Universidade Federal de
            São João del Rei(UFSJ) contendo uma carga horária de 3600 horas de
            curso e um total de 360 horas de estágio distribuídos em 2 anos co
            mo bolsista no Núcleo de Tecnologia da Informação da UFSJ, sendo o
            trabalho final de curso aplicado utilizando-se de metodologias de
            Inteligência Artificial para refinamento de informação.""", """Curso profissional técnico
            em Informática nível médio(introdução a informática, Autoria e Design para internet, Redes
            de computadores, Lógica de programação, Introdução aos Sistemas Operacionais, Técnicas de Programação,
            Banco de Dados, Programação para WEB I e II, Tópicos Avançados de Programação, Desenho-CAD, Projetos de Sistemas).
            Centro de Educação Profissional Tiradentes[CENEP](carga horária de 1350 horas), conclusão em 2012."""],
                "proficional": ["""2016-2017 : Fundação de Apoio A Universidade Federal de São João del Rei
            Cargo: Programador de Sistemas
            Principais atividades: correções e melhorias no sistema de controle interno, manutenção de equipamento, consultoria sobre equipamentos e tecnologias relacionadas a computação.
            """, """2013-2015 : Núcleo de Tecnologia da Informação(Ntinf) da Universidade Federal de São João del-Rei
            Cargo: Auxiliar em Desenvolvimento de Sistemas de Informação
            Principais atividades: atividades inerentes à área de Desenvolvimento de Sistemas de Informação, conforme Termo de compromisso e Responsabilidade de Bolsa de Laboratório.
            """]}
    else:
        label = ['Contact:', 'Skills:', 'Experience:', 'Education:']
        info = {'name': 'Edson Coelho dos Santos', 'desc': 'Pra ingles ver',
                'image': 'https://secure.meetupstatic.com/photos/member/d/9/d/c/member_266755772.jpeg'}
    return render_template('index.html', label=label, info=info, graph=graph, total=total,test=test) # locals()


@app.route("/pdf")
def pdf():
    pdf = ''
    return send_file(pdf)



if __name__ == "__main__":
        # rodar src no local host(host='localhost', port=80,debug=True)
        # ter apenas 1 servidor respodendo na porta 80
        # ssl_context='adhoc'
    app.run(debug=True, host='localhost', port=int(os.environ.get('PORT', 8080)))
