from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from marshmallow import Schema, fields, ValidationError, validates_schema


db = SQLAlchemy()

#models:
#relational databases, store, create and discover relationships
#Select, From, Where, Group By, Having, Order By

#simple assosciation table for thee exercise and workout relations

class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    equipment_needed = db.Column(db.Boolean)

    #connecting to workouts table 
    workouts_exe = db.relationship("WorkoutExercise", back_populates = 'exercises', cascade = 'all, delete-orphan')

    def __repr__(self):
        return f"<exercise {self.id}, {self.name}, {self.category}, {self.equipment_needed}>" #what it do?

 
    #helper methods??? becomes a dictionary for viewing.
    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "equipment_needed": self.equipment_needed
        }


class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.String(200))

    #workout one to many workexes
    #workout one has many exercises based on workout exercises.

    #first argument should be the class not the table
    workouts_exe = db.relationship('WorkoutExercise', back_populates = 'workouts', cascade = 'all, delete-orphan')

    def __repr__(self): #returns a printable representation of an object 
        return f"<Workout {self.id}, {self.date}, {self.duration_minutes}, {self.notes}"

    def dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "duration_minutes": self.duration_minutes,
            "notes": self.notes
        }

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercise'

    id = db.Column(db.Integer, primary_key = True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    #maps the foreign key containing model to have a relationship with the exercise and workout tables/models
    exercises = db.relationship('Exercise', back_populates = 'workouts_exe')
    workouts = db.relationship('Workout', back_populates = 'workouts_exe')
    
    def dict(self):
        return {
            "id": self.id,
            "workout_id": self.workout_id,
            "exercise_id":self.exercise_id,
            "reps": self.reps,
            "sets": self.sets,
            "duration_seconds":self.duration_seconds
        }

    def __repr__(self):
        return f"<WorkoutExercise {self.id}, {self.workout_id}, {self.exercise_id}, {self.reps}, {self.sets}, {self.duration_seconds}>"

class Work_Exer_Schema(Schema):
    id = fields.Int(dump_only = True) #dump_only meaning it won't be deserialized
    workout_id = fields.Int(dump_only = True)
    exercise_id = fields.Int(dump_only = True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()
    workout = fields.Nested(lambda: WorkoutSchema(exclude=("workout_exercise",)))
    exercise = fields.Nested(lambda: ExerciseSchema(exclude=("workout_exercise",))) #tuple???

    @validates_schema
    def validate_reps_sets(self, data, **kwargs):
        if data["reps"] == 0:
            raise ValidationError("reps have to be 1 or more")

        if data["sets"] == 0:
            raise ValidationError("sets have to be 1 or more")

        
class WorkoutSchema(Schema):
    id = fields.Int(dump_only = True)
    date = fields.String()
    duration_minutes = fields.Int()
    notes = fields.String()
    work_exe = fields.List(fields.Nested(Work_Exer_Schema(exclude=("workout", "exercise"))))

    @validates_schema
    def validate_date(self, data, **kwargs):
        if data["date"] == '':
            raise ValidationError("date cannot be empty, format : YYYY/MM/DD")

#I don't understand the usage of marshamallw schema's if we have already created a dict funtion in the classes 


class ExerciseSchema(Schema):
    id = fields.Int(dump_only= True)
    name = fields.String()
    category = fields.String()
    equipment_needed = fields.Bool()
    work_exe = fields.List(fields.Nested(Work_Exer_Schema(exclude=("workout", "exercise"))))

