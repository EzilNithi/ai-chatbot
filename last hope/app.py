from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

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

# FAQ Table
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)

# API to fetch student details
@app.route('/student/<register_number>', methods=['GET'])
def get_student(register_number):
    student = Student.query.filter_by(register_number=register_number).first()
    if student:
        return jsonify({
            "name": student.name,
            "exam_percentage": student.exam_percentage,
            "attendance_percentage": student.attendance_percentage,
            "caste": student.caste
        })
    return jsonify({"error": "Student not found"}), 404

# API to get chatbot response (FAQ)
@app.route('/faq', methods=['POST'])
def get_faq():
    data = request.json
    question = data.get('question', "").lower()
    faq = FAQ.query.filter(FAQ.question.like(f"%{question}%")).first()
    
    if faq:
        return jsonify({"answer": faq.answer})
    return jsonify({"answer": "Sorry, I don't have an answer for that."})

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route for chatbot response (Fixed)
@app.route("/chatbot", methods=["GET"])
def chatbot():
    query = request.args.get("query", "").lower()

    # Search for the question in the database
    faq = FAQ.query.filter(FAQ.question.like(f"%{query}%")).first()

    if faq:
        return jsonify({"response": faq.answer})
    return jsonify({"response": "Sorry, I don't understand."})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
