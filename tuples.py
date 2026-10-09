"""Tuple packing, unpacking, methods, and immutability."""
date_of_birth = (15, 8, 2005)
day, month, year = date_of_birth
print("Packed tuple:", date_of_birth)
print("Unpacked:", day, month, year)
registration_parts = ("2126", "UMLM", "1123")
print("Tuple index:", registration_parts.index("UMLM"))
print("Tuple count:", registration_parts.count("1123"))
print("Tuples are immutable; assigning date_of_birth[0] = 20 raises TypeError.")
