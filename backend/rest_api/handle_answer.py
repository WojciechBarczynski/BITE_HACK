import sys
import os
dir = os.path.dirname(__file__)
filepath = os.path.join(dir, '../..')
sys.path.insert(0, filepath)

from backend.database_facade.users import get_users_df, update_user_rating
from backend.database_facade.tasks import get_tasks_df, update_task_rating, get_solution_url
from backend.database_facade.solutions import post_solution
from backend.rating.update import UpdateData
import math

def handle_user_answer(user_id, task_id, user_answer, work_time):
    users_df = get_users_df()
    tasks_df = get_tasks_df()
    correct_answer = float(tasks_df.loc[tasks_df['id'] == task_id].answer.values[0])
    
    is_correct = is_answer_correct(user_answer, correct_answer)
    
    (updated_user_rating, updated_task_rating, user_point_delta) = \
        UpdateData.update_rating(
            user_id=user_id,
            task_id=task_id,
            is_ok=is_correct,
            user_df=users_df,
            task_df=tasks_df
        )

    update_user_rating(user_id, updated_user_rating)
    update_task_rating(user_id, updated_task_rating)
    post_solution(user_id, task_id, work_time, user_answer, int(is_correct))
    solution_url = get_solution_url(task_id)
    
    return (int(is_correct), correct_answer, solution_url, user_point_delta)
    

def is_answer_correct(user_answer, correct_answer):
    return math.isclose(user_answer, correct_answer, rel_tol=0.001)
    
    
    
