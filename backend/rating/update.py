import pandas as pd
from trueSkills import TrueSkills

DB_CONST = 60

class UpdateData:
    @staticmethod
    def update_rating(
        user_id,
        task_id,
        sol_id,
        is_ok,
        user_df,
        task_df,
        sol_df):
        time = 1
        expectedTime = 1
        user_rating = user_df[user_df.id == user_id].rating.tolist()[0] / DB_CONST
        task_rating = task_df[task_df.id == task_id].rating.tolist()[0] / DB_CONST

        new_user_rating = TrueSkills().update(user_rating, task_rating, is_ok, time, expectedTime)
        diff = int(DB_CONST * (new_user_rating - user_rating))
        user_rating = int(DB_CONST * user_rating + diff)
        task_rating = int(DB_CONST * task_rating - diff)
        return user_rating, task_rating, diff


user_df = pd.DataFrame({'id': [1, 2, 3], 'rating': [2000, 1000, 3000]})
task_df = pd.DataFrame({'id': [1, 2, 3], 'rating': [1500, 700, 2800]})
sol_df = pd.DataFrame({'id': [], 'user_id': [], 'task_id': []})

for i in range(len(user_df)):
    for j in range(len(task_df)):
        print(UpdateData.update_rating(
            user_df.iloc[i].id,
            task_df.iloc[j].id,
            0,
            True,
            user_df,
            task_df,
            sol_df
        ))
