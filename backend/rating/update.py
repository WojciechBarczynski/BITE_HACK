import pandas as pd
from backend.rating.trueSkills import TrueSkills

DB_CONST = 60

class UpdateData:
    @staticmethod
    def update_rating(
        user_id,
        task_id,
        is_ok,
        user_df,
        task_df,
        sol_df):
        print(sol_df)
        print(task_df)
        time = sol_df[sol_df.user_id == user_id]
        time = time[time.task_id == task_id].time.tolist()[0]
        expectedTime = sol_df[sol_df.task_id == task_id].time.tolist()
        if len(expectedTime) > 0:
            expectedTime = round(sum(expectedTime) / len(expectedTime), 2)
        else:
            expectedTime = 120

        user_rating = user_df[user_df.id == user_id].rating.tolist()[0] / DB_CONST
        task_rating = task_df[task_df.id == task_id].rating.tolist()[0] / DB_CONST
        new_user_rating = TrueSkills().update(user_rating, task_rating, is_ok, time, expectedTime)

        diff = int(DB_CONST * (new_user_rating - user_rating))
        user_rating = int(DB_CONST * user_rating + diff)
        task_rating = int(DB_CONST * task_rating - diff)
        return user_rating, task_rating, diff
