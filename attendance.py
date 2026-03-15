from students import get_student_by_id
from courses import get_course_by_id

attendance = [{
    "student_id": "S102",
    "course_id": "C101",
    "present": True
},
{
    "student_id": "S102",
    "course_id": "C102",
    "present": True
},
{
    "student_id": "S101",
    "course_id": "C101",
    "present": True
}]

def record_attendance(student_id, course_id, present):
    """Record attendance for a student in a course"""
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
    
    # Record attendance
    new_attendance = {
        "student_id": student_id,
        "course_id": course_id,
        "present": present
    }
    attendance.append(new_attendance)
    
    status = "present" if present else "absent"
    print(f"Attendance recorded for {student['name']} in {course['course_name']}: {status}")

def attendance_summary(student_id):
    """View attendance summary for a student"""
    student = get_student_by_id(student_id)
    if not student:
        print("Error: Student not found!")
        return
    
    # Get attendance records
    student_attendance = [a for a in attendance if a["student_id"] == student_id]
    
    if len(student_attendance) == 0:
        print(f"No attendance records found for {student['name']}")
        return
    
    # Calculate attendance percentage
    total = len(student_attendance)
    present = len([a for a in student_attendance if a["present"]])
    percentage = (present / total) * 100 if total > 0 else 0
    
    print(f"\n=== ATTENDANCE SUMMARY FOR {student['name']} ===")
    print(f"Student ID: {student_id}")
    print(f"Grade: {student['grade']}")
    print(f"Total Classes: {total}")
    print(f"Classes Present: {present}")
    print(f"Classes Absent: {total - present}")
    print(f"Attendance Percentage: {percentage:.1f}%")
    
    # Course-wise breakdown
    print("\nCourse-wise Attendance:")
    courses_attended = {}
    for a in student_attendance:
        course_id = a["course_id"]
        if course_id not in courses_attended:
            courses_attended[course_id] = {"total": 0, "present": 0}
        courses_attended[course_id]["total"] += 1
        if a["present"]:
            courses_attended[course_id]["present"] += 1
    
    for course_id, stats in courses_attended.items():
        course = get_course_by_id(course_id)
        if course:
            course_percentage = (stats["present"] / stats["total"]) * 100
            print(f"  {course['course_name']}: {course_percentage:.1f}%")
    
    print("=" * 40)