students = []

def add_student():
    name = input("Enter name: ")
    grade = int(input("Enter grade: "))
    students.append({"name": name, "grade": grade})
    
def view_students():
    for s in students:
        print(s["name"], "-", s["grade"])
        
while True:
    print("1. Add Student")
    print("2. View students")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break