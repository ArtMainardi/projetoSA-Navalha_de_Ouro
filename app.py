from flask import Flask, render_template

from agendamentos import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", quantidadeAgendamentos=len(listar_agendamentos()))

@app.route("/agendamentos")
def agendamentos():
    return render_template("agendamentos.html", agendamentos=listar_agendamentos())

@app.route("/agendamento/status/<status>")
def status_listar(status):
    return render_template("status.html", agendamentos=listar_por_status(status))

@app.route("/agendamento/<int:id>")
def agendamento_buscar(id):
    return render_template("detalhe.html", agendamento=buscar_agendamento(id))

if __name__ == "__main__":
    app.run(debug=True)
