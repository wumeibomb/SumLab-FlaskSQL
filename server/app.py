from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from models import * 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)
db.init_app(app)

#routes:

#this is to create a row...
@app.route("/workouts", methods = ["GET", "POST"])
def add_workout():
    #querying to retrieve data
    
    if request.method == "POST":
        data = request.get_json()
        #to create an entity with sql alchemy, instantiate an object of the piece of data you are creating

        id = data["id"]
        date = data["date"]
        duration_minutes = data["duration_minutes"]
        notes = data["notes"]

        new_workout = Workout(id = id, date = date, duration_minutes = duration_minutes, notes = notes)

    #to create a new entity in the db:
        db.session.add(new_workout)
        db.session.commit()

        output = {
            "message": "Added new workout!",
           "data": new_workout.dict()
        }   

        return jsonify(output)

    retrieval = db.session.scalars(db.select(Workout)).all()
    print(retrieval)

    get_data = {
        "message": "Successful data retrieval",
        "data": [eachW.dict() for eachW in retrieval]
    }
    return jsonify(get_data)

@app.route("/workouts/<int:identity>", methods = ["GET", "DELETE"])
def retrieve_workout(identity):
    #data = request.get_json()

    workouts = db.session.execute(db.select(Workout).where(Workout.id == identity))
    print(workouts)

    get_data = {
        "message": "Data Retrieved successfully",
        "data": [each.dict() for each in workouts.scalars()]
        }
    print("IDENTIFIER", get_data)
    return jsonify(get_data)


@app.route("/exercises", methods=["GET", "POST"])
def add_Exercise():
    data = request.get_json()

    id = data["id"]
    name = data["name"]
    category = data["category"]
    equipment_needed = data["equipment_needed"]

    new_exercise = Exercise(id = id, name = name, category = category, equipment_needed = equipment_needed)

    db.session.add(new_exercise)
    db.session.commit()

    output = {
        "message": "Added new exercise!",
        "data": new_exercise.dict()
    }

    return jsonify(output)

@app.route("/exercises/<id>", methods = ["GET", "POST"])
def retrieve_exercise():
    pass

@app.route("/workouts/<workout_id>/exercises/<exercise_id>/workout_exercise", methods = ["POST"])
def add_exercise_to_workout():
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)