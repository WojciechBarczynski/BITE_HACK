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
        time = sol_df[sol_df.user_id == user_id]
        time = time[time.task_id == task_id].time.tolist()[0]
        expectedTime = sol_df[sol_df.task_id == task_id].time.tolist()
        if len(expectedTime) > 0:
            expectedTime = round(sum(expectedTime) / len(expectedTime), 2)
        else:
            expectedTime = 120
        print(time, expectedTime)
        user_rating = user_df[user_df.id == user_id].rating.tolist()[0] / DB_CONST
        task_rating = task_df[task_df.id == task_id].rating.tolist()[0] / DB_CONST

        new_user_rating = TrueSkills().update(user_rating, task_rating, is_ok, time, expectedTime)

        print(new_user_rating, 
            TrueSkills().update(user_rating, task_rating, is_ok, expectedTime, expectedTime))
        diff = int(DB_CONST * (new_user_rating - user_rating))
        user_rating = int(DB_CONST * user_rating + diff)
        task_rating = int(DB_CONST * task_rating - diff)
        return user_rating, task_rating, diff


user_df = pd.DataFrame({'id': [1, 2, 3], 'rating': [2000, 1000, 3000]})
task_df = pd.DataFrame({'id': [1, 2, 3], 'rating': [1500, 700, 2800]})
sol_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9], 
    'user_id': [1, 2, 3, 1, 2, 3, 1, 2, 3], 
    'task_id': [1, 1, 1, 2, 2, 2, 3, 3, 3], 
    'time': [13, 26, 38, 41, 52, 73, 81, 92, 103]})

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
