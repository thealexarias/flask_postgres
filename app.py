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

@app.route("/students", methods=["GET"])
def students():
    result = []
    all_studs = Students.query.all()
    for stud in all_studs:
        serialzed = student_serializer(stud)
        result.append(serialzed)
    return jsonify(result)

@app.route("/old_students", methods=["GET"])
def old_students():
    result = []
    all_students = Students.query.all()
    for stud in all_students:
        if stud.age>20:
            serialized = student_serializer(stud)
            result.append(serialized)
    return jsonify(result)



@app.route("/young_students", methods=["GET"])
def young_students():
    result = []
    all_students = Students.query.all()
    for stud in all_students:
        if stud.age>20:
            serialized = student_serializer(stud)
            result.append(serialized)
    return jsonify(result)


@app.route("/advance_students", methods=["GET"])
def advance_students():
    result = []
    all_students = Students.query.all()
    for stud in all_students:
        if stud.age>20:
            serialized = student_serializer(stud)
            result.append(serialized)
    return jsonify(result)


@app.route("/student_names", methods=["GET"])
def student_names():
    result = []
    all_students = Students.query.all()
    for stud in all_students:
        if stud.age>20:
            serialized = student_serializer(stud)
            result.append(serialized)
    return jsonify(result)


@app.route("/student_ages", methods=["GET"])
def student_ages():
    result = []
    all_students = Students.query.all()
    for stud in all_students:
        if stud.age>20:
            serialized = student_serializer(stud)
            result.append(serialized)
    return jsonify(result)




if __name__ == "__main__":
    app.run(debug= True, port=8000)