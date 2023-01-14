from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sys
import os
dir = os.path.dirname(__file__)
filepath = os.path.join(dir, '../..')
sys.path.insert(0, filepath)

from backend.rest_api.user_login import login_user
from backend.rating.recommend import Recommend
from backend.database_facade.tasks import get_tasks_df
from backend.database_facade.solutions import get_solutions_df
from backend.database_facade.users import get_users_df

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
  response = jsonify(userid=str(login_user((request.form.get('username')))))
  return response
    
@app.route('/question', methods=['GET'])
def get_question():
    if request.method == 'GET':
        user_id = request.form.get('userid')
        task_df = get_tasks_df()
        recommended_task_id = Recommend.get_recommendations(
            user_id=int(user_id),
            user_df=get_users_df(),
            sol_df=get_solutions_df(),
            task_df=task_df
        )
        recommended_task_url =  task_df.loc[task_df['id'] == recommended_task_id].question_link.values[0]
        return jsonify(taskid=recommended_task_id, taskurl=recommended_task_url)
        
    else :
        raise "Question method request unsupported"
    

if __name__ == '__main__':
   app.run(debug = True)