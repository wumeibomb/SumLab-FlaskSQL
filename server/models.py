from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates


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


class Workout(db.Model):
    __tablename__ = 'Workout'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Datetime)


class WorkoutExercise(db.Model):
    __tablename__ = 'WorkoutExercise'

    id = db.Column(primary_key = True)
    workout_id = db.Column(foreign_key = True)
    exercide_id = db.Column(foreign_key = True)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)
