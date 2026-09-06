from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import date


db = SQLAlchemy()

#models:
#relational databases, store, create and discover relationships
#Select, From, Where, Group By, Having, Order By

#joining tables for many to many don't need to be models
Workout_Exercise = db.Table(
    'WorkoutExercise',
    db.Column("id", db.Integer, primary_key = True),
        db.Column("workout_id", db.Integer, db.ForeignKey("Workout.id")),
        db.Column("exercise_id", db.Integer, db.ForeignKey("Exercise.id")),
    db.Column("reps", db.Integer),
    db.Column("sets", db.Integer),
    db.Column("duration_seconds", db.Integer)
)


class Exercise(db.Model):
    __tablename__ = 'Exercise'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    equipment_needed = db.Column(db.Boolean)

    test_relations_E = db.relationship('Workout', secondary = Workout_Exercise, back_populates = 'Exercise')

    def __repr__(self):
        return f"<Exercise {self.id}, {self.name}, {self.category}, {self.equipment_needed}>" #what it do?

 
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
    date = db.Column(db.String, default = date.today().strftime("%d/%m/%Y"))
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.String(200))

    test_relations_W = db.relationship('Exercise', secondary = Workout_Exercise, back_populates = 'Workout')

    def __repr__(self):
        return f"<Workout {self.id}, {self.date}, {self.duration_minutes}, {self.notes}"

    def dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "duration_minutes": self.duration_minutes,
            "notes": self.notes
        }

