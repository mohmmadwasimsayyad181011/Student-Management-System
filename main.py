"""
Student Record and Academic Management System
PRN: 2126UMLM1123

A beginner-friendly command-line project demonstrating Python strings,
lists, tuples, sets, and dictionaries.
"""

students = []


def find_student(roll_no):
    """Return a student dictionary matching roll_no, or None."""
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


def read_marks():
    """Read zero or more comma-separated marks, validating the range 0-100."""
    raw = input("Enter marks separated by commas (or leave blank): ").strip()
    if not raw:
        return []
    try:
        marks = [float(item.strip()) for item in raw.split(",")]
    except ValueError:
        print("Invalid marks. Please enter numbers separated by commas.")
        return read_marks()
    if any(mark < 0 or mark > 100 for mark in marks):
        print("Marks must be between 0 and 100.")
        return read_marks()
    return marks


def add_student():
    """Create a student record, rejecting duplicate roll numbers."""
    roll_no = input("Roll number: ").strip()
    if not roll_no:
        print("Roll number cannot be empty.")
        return
    if find_student(roll_no):
        print("A student with this roll number already exists.")
        return

    name = input("Full name: ").strip().title()
    department = input("Department: ").strip().title()
    email = input("Email: ").strip()
    subjects_raw = input("Subjects separated by commas: ").strip()
    subjects = [s.strip().title() for s in subjects_raw.split(",") if s.strip()]
    marks = read_marks()
    dob_raw = input("Date of birth (DD,MM,YYYY; leave blank if unknown): ").strip()
    dob = ()
    if dob_raw:
        try:
            parts = tuple(int(part.strip()) for part in dob_raw.split(","))
            if len(parts) != 3:
                raise ValueError
            dob = parts
        except ValueError:
            print("Date of birth must be three numbers, e.g. 15,8,2005. Saving as unknown.")
    attendance_raw = input("Attendance percentage (0-100; leave blank if unknown): ").strip()
    attendance = None
    if attendance_raw:
        try:
            attendance = float(attendance_raw)
            if not 0 <= attendance <= 100:
                raise ValueError
        except ValueError:
            print("Invalid attendance. Saving as unknown.")
            attendance = None
    clubs_raw = input("Clubs separated by commas: ").strip()
    clubs = {club.strip().title() for club in clubs_raw.split(",") if club.strip()}

    students.append({
        "roll_no": roll_no,
        "name": name,
        "department": department,
        "subjects": subjects,
        "marks": marks,
        "attendance": attendance,
        "dob": dob,
        "email": email,
        "clubs": clubs,
    })
    print("Student added successfully.")


def display_student(student):
    """Print one student record in a readable format."""
    print("-" * 45)
    print(f"Roll number : {student['roll_no']}")
    print(f"Name        : {student['name']}")
    print(f"Department  : {student['department']}")
    print(f"Email       : {student['email'] or 'Not provided'}")
    print(f"Subjects    : {', '.join(student['subjects']) or 'None'}")
    print(f"Marks       : {student['marks'] or 'Not entered'}")
    if student["marks"]:
        print(f"Average     : {sum(student['marks']) / len(student['marks']):.2f}")
    print(f"Attendance  : {student['attendance'] if student['attendance'] is not None else 'Unknown'}")
    print(f"Date of birth: {student['dob'] or 'Unknown'}")
    print(f"Clubs       : {', '.join(sorted(student['clubs'])) or 'None'}")
    print("-" * 45)


def search_student():
    """Search for a student by roll number."""
    roll_no = input("Enter roll number to search: ").strip()
    student = find_student(roll_no)
    if student:
        display_student(student)
    else:
        print("Student not found.")


def update_student():
    """Update selected basic details for an existing student."""
    student = find_student(input("Enter roll number to update: ").strip())
    if not student:
        print("Student not found.")
        return
    print("Fields: 1 Name  2 Department  3 Email  4 Marks  5 Attendance")
    choice = input("Choose field: ").strip()
    if choice == "1":
        value = input("New name: ").strip()
        if value:
            student["name"] = value.title()
    elif choice == "2":
        value = input("New department: ").strip()
        if value:
            student["department"] = value.title()
    elif choice == "3":
        student["email"] = input("New email: ").strip()
    elif choice == "4":
        student["marks"] = read_marks()
    elif choice == "5":
        value = input("New attendance percentage (0-100): ").strip()
        try:
            attendance = float(value)
            if not 0 <= attendance <= 100:
                raise ValueError
            student["attendance"] = attendance
        except ValueError:
            print("Invalid attendance; record was not changed.")
            return
    else:
        print("Invalid choice.")
        return
    print("Student record updated.")


def delete_student():
    """Delete a student using the roll number."""
    roll_no = input("Enter roll number to delete: ").strip()
    student = find_student(roll_no)
    if student:
        students.remove(student)
        print("Student record deleted.")
    else:
        print("Student not found.")


def display_all():
    """Display all records, including a friendly empty-state message."""
    if not students:
        print("No student records available.")
        return
    for student in students:
        display_student(student)


def calculate_average():
    """Calculate average marks for a selected student."""
    student = find_student(input("Enter roll number: ").strip())
    if not student:
        print("Student not found.")
    elif not student["marks"]:
        print("No marks available for this student.")
    else:
        average = sum(student["marks"]) / len(student["marks"])
        print(f"Average marks for {student['name']}: {average:.2f}")


def highest_scorer():
    """Find the student with the highest average among students with marks."""
    scored = [s for s in students if s["marks"]]
    if not scored:
        print("No marks available to determine the highest scorer.")
        return
    best = max(scored, key=lambda s: sum(s["marks"]) / len(s["marks"]))
    average = sum(best["marks"]) / len(best["marks"])
    print(f"Highest scorer: {best['name']} ({best['roll_no']}) - average {average:.2f}")


def list_by_department():
    """List students whose department matches the entered department."""
    department = input("Enter department: ").strip().casefold()
    matches = [s for s in students if s["department"].casefold() == department]
    if not matches:
        print("No students found in that department.")
        return
    for student in matches:
        print(f"{student['roll_no']} - {student['name']} ({student['department']})")


def count_students():
    """Display the total number of registered students."""
    print(f"Total students: {len(students)}")


def show_unique_data():
    """Demonstrate sets by displaying unique departments, subjects, and clubs."""
    departments = {s["department"] for s in students if s["department"]}
    subjects = {subject for s in students for subject in s["subjects"]}
    clubs = {club for s in students for club in s["clubs"]}
    print("Unique departments:", sorted(departments))
    print("Unique subjects:", sorted(subjects))
    print("Unique clubs:", sorted(clubs))


def load_demo_data():
    """Add a few sample records if the catalogue is empty."""
    if students:
        print("Demo data is only loaded when the student list is empty.")
        return
    students.extend([
        {"roll_no": "101", "name": "Aarav Patil", "department": "Computer Science",
         "subjects": ["Python", "Maths", "DBMS"], "marks": [85, 78, 92],
         "attendance": 91.0, "dob": (15, 8, 2005), "email": "aarav@example.com",
         "clubs": {"Coding", "Sports"}},
        {"roll_no": "102", "name": "Sara Khan", "department": "Information Technology",
         "subjects": ["Python", "Maths", "Networks"], "marks": [90, 88, 94],
         "attendance": 96.0, "dob": (2, 3, 2005), "email": "sara@example.com",
         "clubs": {"Coding"}},
        {"roll_no": "103", "name": "Rohan Deshmukh", "department": "Computer Science",
         "subjects": ["Python", "DBMS"], "marks": [72, 81],
         "attendance": 84.0, "dob": (), "email": "rohan@example.com",
         "clubs": {"Sports", "Music"}},
    ])
    print("Demo records loaded. These are sample records; replace them with your own test data.")


def menu():
    """Run the command-line menu until the user chooses to exit."""
    actions = {
        "1": add_student,
        "2": search_student,
        "3": update_student,
        "4": delete_student,
        "5": display_all,
        "6": calculate_average,
        "7": highest_scorer,
        "8": list_by_department,
        "9": count_students,
        "10": show_unique_data,
        "11": load_demo_data,
    }
    while True:
        print("\n=== STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM ===")
        print("PRN: 2126UMLM1123")
        print("1 Add student  2 Search student  3 Update student")
        print("4 Delete student  5 Display all  6 Calculate average")
        print("7 Highest scorer  8 List by department  9 Count students")
        print("10 Show unique departments/subjects/clubs  11 Load demo data  0 Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Thank you. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    menu()
