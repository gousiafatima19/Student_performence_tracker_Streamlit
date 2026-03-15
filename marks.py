from students import get_student_by_id
from courses import get_course_by_id

marks = [{
    "student_id": "S102",
    "course_id": "C101",
    "marks": 95
},
{
    "student_id": "S102",
    "course_id": "C102",
    "marks": 91
},
{
    "student_id": "S101",
    "course_id": "C101",
    "marks": 85
}]

def record_marks(student_id, course_id, marks_obtained):
    """Record marks for a student in a course"""
    # Check if student exists
    student = get_student_by_id(student_id)
    if not student:
        print("Error: Student not found!")
        return
    
    # Check if course exists
    course = get_course_by_id(course_id)
    if not course:
        print("Error: Course not found!")
        return
    
    # Validate marks
    if marks_obtained < 0 or marks_obtained > 100:
        print("Error: Marks must be between 0 and 100!")
        return
    
    # Check if marks already recorded
    for m in marks:
        if m["student_id"] == student_id and m["course_id"] == course_id:
            m["marks"] = marks_obtained
            print(f"Marks updated for {student['name']} in {course['course_name']}")
            return
    
    # Add new marks record
    new_marks = {
        "student_id": student_id,
        "course_id": course_id,
        "marks": marks_obtained
    }
    marks.append(new_marks)
    print(f"Marks recorded for {student['name']} in {course['course_name']}")

def calculate_gpa(student_id):
    """Calculate GPA for a student"""
    student = get_student_by_id(student_id)
    if not student:
        print("Error: Student not found!")
        return
    
    # Get all marks for student
    student_marks = [m for m in marks if m["student_id"] == student_id]
    
    if len(student_marks) == 0:
        print(f"No marks found for {student['name']}")
        return 0
    
    # Calculate average and convert to GPA (simplified)
    total = sum(m["marks"] for m in student_marks)
    average = total / len(student_marks)
    gpa = (average / 25) + 1  # Simplified conversion (40% = 2.6, 95% = 4.8)
    
    print(f"\n=== GPA CALCULATION FOR {student['name']} ===")
    print(f"Number of Subjects: {len(student_marks)}")
    print(f"Average Marks: {average:.1f}%")
    print(f"GPA: {gpa:.2f}")
    
    return gpa

def generate_report_card(student_id):
    """Generate report card for a student"""
    student = get_student_by_id(student_id)
    if not student:
        print("Error: Student not found!")
        return
    
    # Get marks
    student_marks = [m for m in marks if m["student_id"] == student_id]
    
    if len(student_marks) == 0:
        print(f"No marks found for {student['name']}")
        return
    
    # Calculate GPA
    total = sum(m["marks"] for m in student_marks)
    average = total / len(student_marks)
    gpa = (average / 25) + 1
    
    # Find top subjects
    sorted_marks = sorted(student_marks, key=lambda x: x["marks"], reverse=True)
    
    print("\n=== REPORT CARD ===")
    print(f"Student: {student['name']} ({student['student_id']})")
    print(f"Grade: {student['grade']}")
    print(f"GPA: {gpa:.2f}")
    print(f"Attendance: 92%")  # Placeholder
    print("\nSubject-wise Performance:")
    for m in student_marks[:3]:  # Show top 3
        course = get_course_by_id(m["course_id"])
        if course:
            print(f"  {course['course_name']}: {m['marks']}%")
    
    # Remarks based on GPA
    if gpa >= 4.0:
        remarks = "Excellent progress!"
    elif gpa >= 3.5:
        remarks = "Good performance"
    elif gpa >= 3.0:
        remarks = "Satisfactory"
    else:
        remarks = "Needs improvement"
    
    print(f"\nRemarks: {remarks}")
    print("=" * 40)