from functools import wraps
from flask import request, jsonify  # ← precisa importar
import os

API_KEY = os.getenv('API_KEY')

def autentication(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        chave = request.headers.get("Authorization")
        if chave != API_KEY:
            return jsonify({"erro":"Acesso Negado : chave invalida ou ausente"}), 401
        return f(*args, **kwargs)
    return decorated