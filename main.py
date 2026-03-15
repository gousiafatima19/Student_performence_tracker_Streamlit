import streamlit as st
from students import add_student, get_top_performers
from courses import add_course, course_average
from marks import record_marks, calculate_gpa, generate_report_card
from attendance import record_attendance, attendance_summary
st.title("STUDENT PERFORMANCE TRACKER")
menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add New student",
        "Add New course",
        "Record marks",
        "Record Attendance",
        "Calculate GPA",
        "Generate Report Card",
        "View Top Performers",
        "View Course-Wise Averages",
        "View Attendance Summary"
    ]
)


if menu == "Add New student":
    st.subheader("Add New Student")
    student_id = st.text_input("Student ID")
    student_name = st.text_input("Student Name")
    grade = st.text_input("Grade")
    if st.button("Add Student"):
        add_student(student_id, student_name, grade)
elif menu == "Add New course":
    st.subheader("Add New Course")
    course_id = st.text_input("Course ID")
    course_name = st.text_input("Course Name")
    instructor = st.text_input("Instructor")
    if st.button("Add Course"):
        add_course(course_id, course_name, instructor)
elif menu == "Record marks":
    st.subheader("Record Marks")
    student_id = st.text_input("Student ID")
    course_id = st.text_input("Course ID")
    marks_obtained = st.number_input("Marks (0-100)", min_value=0, max_value=100)
    if st.button("Record Marks"):
        record_marks(student_id, course_id, marks_obtained)
elif menu == "Record Attendance":
    st.subheader("Record Attendance")
    student_id = st.text_input("Student ID")
    course_id = st.text_input("Course ID")
    present = st.selectbox("Present?", ["Yes", "No"])
    if st.button("Record Attendance"):
        record_attendance(student_id, course_id, present == "Yes")
elif menu == "Calculate GPA":
    st.subheader("Calculate GPA")
    student_id = st.text_input("Student ID")
    if st.button("Calculate GPA"):
        calculate_gpa(student_id)
elif menu == "Generate Report Card":
    st.subheader("Generate Report Card")
    student_id = st.text_input("Student ID")
    if st.button("Generate Report Card"):
        generate_report_card(student_id)
elif menu == "View Top Performers":
    st.subheader("View Top Performers")
    grade = st.text_input("Enter Grade (e.g., 9, 10)")
    count = st.number_input("Number of top performers to view", min_value=1)
    if st.button("View Top Performers"):
        get_top_performers(grade, count)
elif menu == "View Course-Wise Averages":
    st.subheader("View Course-Wise Averages")
    course_id = st.text_input("Enter Course ID")
    if st.button("View Course Averages"):
        course_average(course_id)
elif menu == "View Attendance Summary":
    st.subheader("View Attendance Summary")
    student_id = st.text_input("Enter Student ID")
    if st.button("View Attendance Summary"):
        attendance_summary(student_id)
