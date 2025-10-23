from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg:///student_flask"
    )

db = SQLAlchemy(app)

@app.route('/')
def homepage():
    return "<h1>Hello</h1>"

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

def student_serializer(stud: Students) -> dict:
    return{
        'id': stud.id,
        'first_name': stud.first_name,
        'last_name': stud.last_name,
        'age': stud.age,
        'grade': stud.grade
        }

@app.route("/students")
def students():
    result = []
    all_studs = Students.query.all()
    for stud in all_studs:
        serialzed = student_serializer(stud)
        result.append(serialzed)
    return jsonify(result)




if __name__ == "__main__":
    app.run(debug= True)