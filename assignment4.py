class dept:
    def __init__(self, id, dname, loc, hod):
        self.id = id
        self.dname = dname
        self.loc = loc
        self.hod = hod

    def display_info(self):
        print(f"\nDepartment id: {self.id}")
        print(f"Department name: {self.dname}")
        print(f"Location: {self.loc}")
        print(f"HOD: {self.hod}")


# Input number of departments
dept_count = int(input("Enter number of departments: "))
l = []

# Input department details
for i in range(dept_count):
    print(f"\nEnter details for department {i+1}")
    id = int(input("Enter department id: "))
    dname = input("Enter department name: ")
    location = input("Enter location: ")
    hod = input("Enter name of HOD: ")
    dept1 = dept(id, dname, location, hod)
    l.append(dept1)

# Display all departments
print("\n--- Department Details ---")
for department in l:
    department.display_info()

# Search menu
print("\n--- Search Department ---")
print("1. Search by Department ID")
print("2. Search by Department Name")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    search_id = int(input("Enter department ID to search: "))
    found = False
    for department in l:
        if department.id == search_id:
            print("\n--- Department Found ---")
            department.display_info()
            found = True
            break
    if not found:
        print("Department not found.")

elif choice == "2":
    search_name = input("Enter department name to search: ").lower()
    found = False
    for department in l:
        if department.dname.lower() == search_name:
            print("\n--- Department Found ---")
            department.display_info()
            found = True
    if not found:
        print("Department not found.")

else:
    print("Invalid choice.")



