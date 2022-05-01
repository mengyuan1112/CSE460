import json
from flask import Flask, render_template, request

import delete_tconst
import feature.account
import insert
import selection
from flask_cors import CORS

app = Flask(__name__)


@app.route("/signup", methods=['POST'])
def register():
    data = json.loads(request.get_data(as_text=True))
    print(data)
    answer = feature.account.register(data['username'], data['password'])
    print(answer)
    return json.dumps(answer)


@app.route("/login", methods=['POST', 'GET'])
def login():
    data = json.loads(request.get_data(as_text=True))
    answer = feature.account.login(data['username'], data['password'])
    return json.dumps(answer)


@app.route("/update", methods=['POST', 'GET'])
def update():
    data = json.loads(request.get_data(as_text=True))
    answer = feature.account.update(data['username'], data['password'], data['newPassword'])
    return json.dumps(answer)


@app.route("/delete", methods=['POST', 'GET'])
def delete_():
    print("delete")
    data = json.loads(request.get_data(as_text=True))
    #answer = feature.account.delete(data['username'], data['password'])
    tconst = data["tconst"]
    delete_tconst.delete(tconst)
    return "deleted"


@app.route("/select", methods=["POST"])
def select():
    data = json.loads(request.get_data(as_text=True))
    print(data)
    result = selection.generate_result(data)
    print("this is len: " + str(len(result)))
    if len(result) == 0:
        return json.dumps(["No movie satisfy"])
    print(result)
    return json.dumps(result)

@app.route("/insert", methods=["POST"])
def insert_():
    data = json.loads(request.get_data(as_text=True))
    print(data)
    insert.generate_result(data)
    return "inserted"


CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8099)
    app.run(debug=True)
