def logger(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


students = []

@logger
def add_student(*grades, **info):
    student_record = {
        "name": info.get("name", "Unknown"),
        "id": info.get("id", "N/A"),
        "grades": list(grades)
    }
    students.append(student_record)


@logger
def calculate_results():
    for student in students:
        grades = student["grades"]
        if not grades:
            print(f"{student['name']} has no grades.")
            continue
        avg = sum(grades) / len(grades)
        print(f"\nStudent: {student['name']}")
        print(f"ID: {student['id']}")
        print(f"Grades: {grades}")
        print(f"Average: {avg:.2f}")


add_student(85, 90, 78, name="vaishnavi", id="101")
add_student(45, 40, 50, name="kavya", id="102")
add_student(95, 88, 92, name="Charlie", id="103")

calculate_results()
