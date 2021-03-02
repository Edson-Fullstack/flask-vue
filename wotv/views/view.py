from flask import render_template, url_for, request, send_file, jsonify, Blueprint

def init_app(app):
    # home page
    @app.route("/")
    def index():
        i = 1000
        return render_template('index.html',teste="teste") # locals()

    @app.route("/image/<path>")
    def image(path):
        pdf="." + path
        # if path != null:
        #pdf = './static/wotv-ffbe-dump/img/units/FF14boss.png'
        return send_file(pdf)#, as_attachment=True) 
    
    @app.route("/docs/<path>")
    def gdocs(path):
        gdocs = path
        return send_file(gdocs, as_attachment=True) 

        
    @app.route("/<table>")
    def database(table):
        return table
