# Flask SQLAlchemy Backend!!
- First, this project is a flask based application that uses SQLAlchemy to create or simulate a database.

## How to utilize:
 - To utilize, clone this repo and enter your IDE and make sure you are in the server folder. 
 - Then type in pipenv shell to enable a virtual environment and the most important step for this app to work is the command pipenv install . This will install the needed dependencies onto your virtual environment allowing the application to work.
 (Ensure that you also have SQL Viewer installed on your IDE or a similar extension to view the database)
 - For testing reasons, the instance folder contains nothing so that you can test the seed.py file yourself using : python seed.py . 

 ## For flask_shell usage:
   If you are planning on testing the relationhips via flask_shell, here is a simple query to use for testing: 

      >>>  workout1 = Workout.query.filter_by(id = 10).first() 
      >>>  workout1.workouts_exe

    This query is simply to retrieve the Workout with id 10 along with the workout_exercises associated with id 10.


## Issues!!!
 - When creating a row of data for the table. The date must be input as a string in the format: "YYYY-MM-DD"
 - Did not find proper use for serialization using the Schema when we could just use the dict function.
