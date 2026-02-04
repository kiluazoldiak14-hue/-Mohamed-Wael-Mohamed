# Create a dictionary called contacts
contacts = {
    "Ahmed": "01012345678",
    "Sara": "01187654321",
    "Omar": "01234567890"
}

# Print all names in the contact book
print("Contacts in the phone book:")
for name in contacts:
    print(name)

# Allow user to search for a contact by name
search_name = input("\nEnter a name to search: ")

if search_name in contacts:
    print("Phone number:", contacts[search_name])
else:
    print("Contact not found.")

    
    # Create a list of dictionaries for students
students = [
    {"name": "Ali", "grades": [85, 90, 88]},
    {"name": "Mona", "grades": [78, 82, 80]},
    {"name": "Youssef", "grades": [92, 95, 93]}
]

# Calculate and print the average grade for each student
for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    
    print(f"{name}'s average grade: {average}")