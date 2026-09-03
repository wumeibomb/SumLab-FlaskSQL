from app import app
from models import *

with app.app_context():
    #reset data and add new example
    db.session.query(Workout).delete()
    db.session.query(Exercise).delete()

    workouts = [
        Workout(id= 10, date = 30/8/2026, duration_minutes = 15, notes = "WORK!"),
        Workout(id= 11, date = 30/8/2026, duration_minutes = 10, notes = "WORKING!")
    ]

    exercises = [
        Exercise(id= 10, name = "Jay", category = "Glutes", equipment_needed = False),
        Exercise(id= 11, name = "Jake", category = "Biceps", equipment_needed = True)
    ]

    #adds to the db:
    db.session.add_all(workouts + exercises)
    db.session.commit()