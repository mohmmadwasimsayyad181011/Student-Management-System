"""String methods used for student data."""
name = "  rahul sharma  "
print("Original:", repr(name))
print("strip():", name.strip())
print("title():", name.strip().title())
print("upper():", name.upper())
print("lower():", name.lower())
print("replace():", name.strip().replace("rahul", "rohan"))
print("split():", "Python,DBMS,Maths".split(","))
print("join():", ", ".join(["Python", "DBMS", "Maths"]))
print("find():", "Student Management".find("Management"))
print("count():", "banana".count("a"))
print("startswith():", "2126UMLM1123".startswith("2126"))
