import pymysql
import pandas as pd

class SolutionEntry:
    def __init__(self, id, task_id, user_id, work_time_seconds, user_answer, is_correct):
        self.id = id
        self.task_id = task_id
        self.user_id = user_id
        self.work_time_seconds = work_time_seconds
        self.user_answer = user_answer
        self.is_correct = bool(is_correct)
        
def get_solutions_df():
    connection = pymysql.connect(
        host="mysql.agh.edu.pl", 
        user="swoznia2",
        password="rMBsvPsTJQ8etui0",
        database="swoznia2"
        )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM solutions")
            database_output = cursor.fetchall()
    finally:
        connection.close()
    
    solutions_list = []
    for database_entry in list(database_output):
        solutions_list.append(SolutionEntry(*database_entry))
    
    return pd.DataFrame.from_records(solution.__dict__ for solution in solutions_list)

print(get_solutions_df())