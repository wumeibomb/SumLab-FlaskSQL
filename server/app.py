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
@app.route("/flop", methods = ["POST"])
def add_workout():
    data = request.get_json()
    #to create an entity with sql alchemy, instantiate an object of the piece of data you are creating

    id = data["id"]
    date = data["date"]
    duration_minutes = data["duration_minutes"]
    notes = data["notes"]

    new_workout = Workout(id = id, date = date, duration_minutes = duration_minutes, notes = notes)

    #to create a new entity in the db:
    db.session.add(new_workout)
    #db.session.commit()

    output = {
        "message": "Added new workout!",
        "data": new_workout.dict()
    }

    return jsonify(output)



if __name__ == '__main__':
    app.run(port=5555, debug=True)