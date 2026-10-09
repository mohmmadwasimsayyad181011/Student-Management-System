"""Dictionary operations for one student profile."""
student = {
    "roll_no": "101",
    "name": "Aarav Patil",
    "department": "Computer Science",
    "marks": [85, 78, 92]
}
print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:")
for key, value in student.items():
    print(key, "->", value)
print("get email default:", student.get("email", "Not provided"))
student.update({"department": "Information Technology"})
print("updated department:", student["department"])
removed = student.pop("marks")
print("removed marks:", removed)
