import warnings
warnings.simplefilter(action="ignore")

class Recommend:
    @staticmethod
    def get_user_solutions(solutions_df, user_id):
        records = solutions_df[solutions_df.user_id == user_id]
        return records['id'].tolist()

    @staticmethod
    def get_recommendations(user_id, user_df, sol_df, task_df):
        user_rating = user_df[user_df.id == user_id].rating.tolist()[0]
        solved_tasks = sol_df[sol_df.user_id == user_id]
        unsolved_tasks = task_df[~task_df.id.isin(solved_tasks.task_id)]
        unsolved_tasks['rating'] = unsolved_tasks['rating'].apply(lambda x: x - user_rating)
        unsolved_tasks['rating'] = unsolved_tasks['rating'].apply(lambda x: abs(x))
        unsolved_tasks = unsolved_tasks.sort_values(by=['rating'])
        return unsolved_tasks.head(1).id.tolist()[0]
        


       

