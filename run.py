from datetime import datetime, timezone, timedelta
from flask import Flask, jsonify, request
import logging
from factory import db
import jwt

app = Flask(__name__)
db.init_app(app)

@app.route("/", methods=["GET"])
def home():
    return {"msg": "Cuida!"}, 200

@app.route("/login", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            'exp': datetime.now(timezone.utc) + timedelta(minutes=1)
        },
        key="access-key",
        algorithm="HS256"
    )
    
    return jsonify({'token': token}), 200

@app.route("/secret", methods=["POST"])
def secret():
    raw_token = request.headers.get("Authorization")
    try:
        token_valid = jwt.decode(raw_token, key="access-key", algorithms="HS256")
        return {'msg': "Deu bom!"}
    except Exception as err:
        logging.error(f"ERROR AO DECODIFICAR TOKEN: {type(err)} - {err}")
        return {"error": f"{err}"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)