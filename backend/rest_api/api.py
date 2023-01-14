from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sys
import os
dir = os.path.dirname(__file__)
filepath = os.path.join(dir, '../..')
sys.path.insert(0, filepath)

from backend.rest_api.user_login import login_user

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    response = jsonify(userid=str(login_user((request.form.get('username')))))
    return response
     

if __name__ == '__main__':
   app.run(debug = True)