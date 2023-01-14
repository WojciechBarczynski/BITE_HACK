import pandas as pd
from trueSkills import TrueSkills

class UpdateData:
    @staticmethod
    def update_rating(
        user_id,
        task_id,
        is_ok,
        user_df,
        task_df):
        user_rating = user_df[user_df.id == user_id].rating.tolist()[0]
        task_rating = task_df[task_df.id == task_id].rating.tolist()[0]
        new_user_rating = TrueSkills().update(user_rating, task_rating, is_ok)
        diff = new_user_rating - user_rating
        user_rating += diff
        task_rating -= diff
        return user_rating, task_rating

user_df = pd.read_csv('user.csv')
task_df = pd.read_csv('task.csv')
u_id = 1
t_id = 10

print(UpdateData.update_rating(u_id, t_id, 1, user_df, task_df))
print(UpdateData.update_rating(u_id, t_id, 0, user_df, task_df))
