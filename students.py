students = [{
    "student_id": "S101",
    "name": "Rahul Sharma",
    "grade": "9"
},
{
    "student_id": "S102",
    "name": "Riya Mehta",
    "grade": "9"
},
{
    "student_id": "S103",
    "name": "Arjun Singh",
    "grade": "10"
}]

def add_student(student_id, name, grade):
    """Add a new student"""
    new_student = {
        "student_id": student_id,
        "name": name,
        "grade": grade
    }
    students.append(new_student)
    print(f"Student {name} added successfully!")

def get_student_by_id(student_id):
    """Get student details by ID"""
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None

def get_top_performers(grade, count):
    """View top performers in a grade"""
    print(f"\n=== TOP {count} PERFORMERS IN GRADE {grade} ===")
    print("-" * 40)
    
    # This would normally use marks data, showing placeholder for now
    print("1. Riya Mehta (S102) - GPA: 8.7")
    print("2. Rahul Sharma (S101) - GPA: 8.2")
    print("3. Priya Patel (S104) - GPA: 7.9")