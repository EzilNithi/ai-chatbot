from app import db, Student, FAQ, app

with app.app_context():  # ✅ Fix: Set up the application context
    # Check if the student already exists
    existing_student = Student.query.filter_by(email="ezilnithi8@gmail.com").first()
    if not existing_student:
        student = Student(
            name="Ezhilnithi R",
            register_number="CB22S611349",
            email="ezilnithi8@gmail.com",
            exam_percentage=81,
            attendance_percentage=96,
            caste="BC"
        )
        db.session.add(student)

    # Check if FAQ data already exists
    existing_faq1 = FAQ.query.filter_by(question="What is my exam percentage?").first()
    existing_faq2 = FAQ.query.filter_by(question="What is my attendance percentage?").first()

    if not existing_faq1:
        faq1 = FAQ(question="What is my exam percentage?", answer="Your exam percentage is 81%.")
        db.session.add(faq1)

    if not existing_faq2:
        faq2 = FAQ(question="What is my attendance percentage?", answer="Your attendance percentage is 96%.")
        db.session.add(faq2)

    db.session.commit()
    print("Sample data added successfully (or already exists)!")
