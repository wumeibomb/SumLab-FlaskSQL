from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import datetime


db = SQLAlchemy()

#models:
#relational databases, store, create and discover relationships
#Select, From, Where, Group By, Having, Order By


class Exercise(db.Model):
    __tablename__ = 'Exercise'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    equipment_needed = db.Column(db.Boolean)

    #helper methods??? becomes a dictionary for viewing.
    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "equipment_needed": self.equipment_needed
        }


class Workout(db.Model):
    __tablename__ = 'Workout'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = datetime.date.today())
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.String(200))

    def dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "duration_minutes": self.duration_minutes,
            "notes": self.notes
        }

class WorkoutExercise(db.Model):
    __tablename__ = 'WorkoutExercise'

    id = db.Column(db.Integer, primary_key = True)
    workout_id = db.Column(db.Integer, db.ForeignKey('Workout.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('Exercise.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    def dict(self):
        return {
            "id": self.id,
            "workout_id": self.workout_id,
            "exercise_id":self.exercise_id,
            "reps": self.reps,
            "sets": self.sets,
            "duration_seconds":self.duration_seconds
        }
