import json
from flask import Flask, render_template, request
import feature.account
import selection

app = Flask(__name__)

@app.route("/signup", methods=['POST'])
def register():
    data = json.loads(request.get_data(as_text=True))
    answer=feature.account.register(data['username'],data['password'])
    return answer

@app.route("/login", methods=['POST','GET'])
def login():
    data = json.loads(request.get_data(as_text=True))
    answer=feature.account.login(data['username'],data['password'])
    return answer

@app.route("/select", methods=["GET"])
def select():
    data = json.loads(request.get_data(as_text=True))
    result = selection.generate_result(data)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    app.run(debug=True)