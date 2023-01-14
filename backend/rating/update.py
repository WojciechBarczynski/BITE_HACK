import sys
import os
dir = os.path.dirname(__file__)
filepath = os.path.join(dir, '../..')
sys.path.insert(0, filepath)

import pandas as pd
from backend.rating.trueSkills import TrueSkills

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
        return user_rating, task_rating, diff
