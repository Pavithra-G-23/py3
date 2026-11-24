students={}
def add_student():
    roll = input("enter roll no:")
    name = input("Enter Name:")
    dept = input("Enter Department:")
    students[roll]={"Name":name,"Department":dept}
    print("Student added successfully:")
def view_students():
    if not students:
        print("No student records found")
        return
    print("\n____student records_____")
    for roll , data in students.items():
        print("Roll No:",roll,"| Name:",data["Name"],"| Department:",data["Department"])
def search_student():
    roll = input("Enter Roll not to search:")
    if roll in students:
        print(students[roll])
    else:
        print("students not found")    
def delete_student():
    roll = input("Enter roll no to delete:")
    if roll in students:
        del students[roll]
        print("student deleted successfully.")
    else:
        print("student not found")    
    while True:
        print("\n1.Add student")
        print("2.view students")
        print("3.search student")
        print("4.Delete student")
        print("5.Exit")
choice = input("Enter your choice:")
if choice == "1":
    add_student()
elif choice == "2":
    view_students()
elif choice == "3":
    search_student()
elif choice =="4":
    delete_student()
elif choice == "5":
    print("Existing....")
    
else: 
    print ("Invalid Choice")               
    
    
