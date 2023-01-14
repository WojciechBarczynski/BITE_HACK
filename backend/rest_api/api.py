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
from backend.database_facade.users import get_users_df, get_user_info
from handle_answer import handle_user_answer
import datetime

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
  response = jsonify(userid=str(login_user((request.form.get('username')))))
  return response

user_question_send_time = {}

@app.route('/question', methods=['GET'])
def get_question():
    if request.method == 'GET':
        user_id = int(request.args.get('userid'))
        task_df = get_tasks_df()
        recommended_task_id = Recommend.get_recommendations(
            user_id=user_id,
            user_df=get_users_df(),
            sol_df=get_solutions_df(),
            task_df=task_df
        )
        recommended_task_url =  task_df.loc[task_df['id'] == recommended_task_id].question_link.values[0]
        user_question_send_time[user_id] = datetime.datetime.now()
        return jsonify(taskid=recommended_task_id, taskurl=recommended_task_url)
        
    else :
        raise "Question method request unsupported"

@app.route('/userinfo', methods=['GET'])
def get_question():
    if request.method == 'GET':
        user_id = int(request.args.get('userid'))
        (user_name, user_rating) = get_user_info(user_id)
        return jsonify(username=user_name, userrating=user_rating)
    else :
        raise "User info method request unsupported"

@app.route('/answer', methods=['POST'])
def handle_answer():
    if request.method != 'POST':
        raise "Incorrect POST on answer"
    user_id=int(request.form.get('userid'))
    task_id=int(request.form.get('taskid'))
    answer=float(request.form.get('answer'))
    work_time_seconds = (datetime.datetime.now() - user_question_send_time.get(user_id)).total_seconds()
    (result, correct_answer, solution_url, user_rating_delta) = handle_user_answer(user_id, task_id, answer, work_time_seconds)
    return jsonify(result=result, answer=correct_answer, link=solution_url, pointdelta=user_rating_delta)


if __name__ == '__main__':
   app.run(debug = True)