from flask import Flask, request, jsonify
import sys
import os
dir = os.path.dirname(__file__)
filepath = os.path.join(dir, '../..')
sys.path.insert(0, filepath)

from backend.rest_api.user_login import login_user

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    return jsonify(userid=str(login_user((request.args.get('username')))))
     

if __name__ == '__main__':
   app.run(debug = True)