"""Set operations for unique departments, subjects, and clubs."""
departments = ["Computer Science", "Mechanical", "Computer Science", "Civil"]
unique_departments = set(departments)
print("Unique departments:", unique_departments)
a = {"Python", "DBMS", "Maths"}
b = {"Python", "Networks"}
print("Add:", end=" ")
b.add("Cyber Security")
print(b)
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Python in a:", "Python" in a)
b.discard("Unknown")  # discard does not raise an error if missing
print("After discard:", b)
