# Teste de criação imagem docker
from flask import Flask
app = Flask(__name__)

mensagem = ""

with open('entrada/texto.txt', 'r') as file:
    for v in file.readlines():
        mensagem += v
        mensagem += " ------------- "


@app.route("/")
def hello():
    return mensagem


if __name__ == "__main__":
    app.run(host='0.0.0.0')

