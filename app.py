# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

GITHUB_INSTALL_URL = "https://github.com/apps/benthic-automation-test/installations/new"

@app.route('/')
def index():
    return f"<h1>Github Apps with Flask</h1></br> <a href='{GITHUB_INSTALL_URL}'>Install app</a>"

@app.route('/git-providers/1/events/', methods=['POST'])
def events():
    json_data = request.get_json()
    print(json_data)
    return jsonify({'message': 'success'}), 200

if __name__ == "__main__":
    app.run()

