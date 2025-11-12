from flask import Flask, jsonify, request
import json
from decorator import autentication

app = Flask(__name__)

#Arquivos
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

#Endpoint Inicial
@app.route('/')
def home():
    return jsonify({"mensagem":"API da Revenda - Status : OK"})

@app.route('/clientes')
@autentication
def get_clientes():
    return jsonify(dados.get('clientes', []))

@app.route('/pedidos')
@autentication
def get_pedidos():
    return jsonify(dados.get('pedidos', []))

@app.route('/visitas')
@autentication
def get_visitas():
    return jsonify(dados.get('visitas', []))


if __name__ == "__main__":
    app.run(debug=True)