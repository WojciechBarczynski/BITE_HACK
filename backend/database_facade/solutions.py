import pymysql
import pandas as pd

class SolutionEntry:
    def __init__(self, sol_id, task_id, user_id, work_time_seconds, user_answer, is_correct):
        self.id = sol_id
        self.task_id = task_id
        self.user_id = user_id
        self.work_time_seconds = work_time_seconds
        self.user_answer = user_answer
        self.is_correct = bool(is_correct)
    
    def insert_to_db(self):
        connection = pymysql.connect(
        host="mysql.agh.edu.pl", 
        user="swoznia2",
        password="rMBsvPsTJQ8etui0",
        database="swoznia2"
        )
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO solutions (ID, TaskID, UserID, WorkTimeSeconds, UserAnswer, IsCorrect)" + "\n" \
                    + "VALUES (%s, %s, %s, %s, %s, %s)"
                val = (f"{self.id}", f"{self.task_id}", f"{self.user_id}", f"{self.work_time_seconds}", f"{self.user_answer}", f"{self.is_correct}")
                cursor.execute(sql, val)
                connection
            
        finally:
            connection.close()
        
        
def get_solutions_df():
    solutions_list = get_solutions()
    return pd.DataFrame.from_records(solution.__dict__ for solution in solutions_list)

def get_solutions():
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
        
    return solutions_list

def post_solution(user_id, task_id, work_time, user_answer, is_correct):
    connection = pymysql.connect(
        host="mysql.agh.edu.pl", 
        user="swoznia2",
        password="rMBsvPsTJQ8etui0",
        database="swoznia2"
        )
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO solutions (TaskID, UserID, WorkTimeSeconds, UserAnswer, IsCorrect)" \
                + "\n" + "VALUES (%s, %s, %s, %s, %s)"
            val = (f"{user_id}", f"{task_id}", f"{work_time}", f"{user_answer}", f"{is_correct}")
            cursor.execute(sql, val)
            connection.commit()
    finally:
        connection.close()
        