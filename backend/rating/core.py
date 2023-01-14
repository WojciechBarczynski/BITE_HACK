from trueSkills import TrueSkills

model = TrueSkills()
player_rating = 25
task_rating = 25
outcome = 1
print(model.update(player_rating, task_rating, outcome))

