import pandas as pd
from backend.rating.trueSkills import TrueSkills

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
        diff = new_user_rating - user_rating
        user_rating += diff
        task_rating -= diff
        return int(DB_CONST * user_rating), int(DB_CONST * task_rating), int(DB_CONST * diff)
