from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college_chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Student Table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    register_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    exam_percentage = db.Column(db.Float, nullable=False)
    attendance_percentage = db.Column(db.Float, nullable=False)
    caste = db.Column(db.String(20), nullable=False)

# Staff Table
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    register_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# FAQ Table
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)

# Create tables in the database
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database and tables created successfully!")
