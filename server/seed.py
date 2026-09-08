from app import app
from models import *
import datetime

with app.app_context():
    #reset data and add new example
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    workA =  Workout(id= 10, date = datetime.datetime(2026, 3, 15), duration_minutes = 15, notes = "WORK!")
    workB =  Workout(id= 11, date = datetime.datetime(2026, 3, 12), duration_minutes = 10, notes = "WORKING!")

    db.session.add_all([workA,workB])
    db.session.commit()

    exeA =  Exercise(id= 10, name = "Jay", category = "Glutes", equipment_needed = False)
    exeB =  Exercise(id= 11, name = "Jake", category = "Biceps", equipment_needed = True)

    db.session.add_all([exeA, exeB])
    db.session.commit()
    
    W_E_1 = WorkoutExercise(id = 1, workouts = workA, reps = 3, sets = 2, duration_seconds = 30)
    W_E_2 = WorkoutExercise(id = 2, exercises = exeA, reps = 2, sets = 4, duration_seconds = 25)


    #adds to the db:
    db.session.add_all([W_E_1, W_E_2])
    db.session.commit()