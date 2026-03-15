courses = [{
    "course_id": "C101",
    "course_name": "Mathematics",
    "instructor": "Dr. Sharma"
},
{
    "course_id": "C102",
    "course_name": "English",
    "instructor": "Ms. Gupta"
},
{
    "course_id": "C103",
    "course_name": "Science",
    "instructor": "Mr. Kumar"
}]

def add_course(course_id, course_name, instructor):
    """Add a new course"""
    new_course = {
        "course_id": course_id,
        "course_name": course_name,
        "instructor": instructor
    }
    courses.append(new_course)
    print(f"Course {course_name} added successfully!")

def get_course_by_id(course_id):
    """Get course details by ID"""
    for course in courses:
        if course["course_id"] == course_id:
            return course
    return None

def course_average(course_id):
    """Calculate average marks for a course"""
    course = get_course_by_id(course_id)
    if not course:
        print("Error: Course not found!")
        return
    
    print(f"\n=== COURSE AVERAGE: {course['course_name']} ===")
    print("-" * 40)
    
    # This would use marks data, showing placeholder for now
    print(f"Course ID: {course_id}")
    print(f"Number of Students: 25")
    print(f"Class Average: 78.5%")
    print(f"Highest Score: 95%")
    print(f"Lowest Score: 45%")