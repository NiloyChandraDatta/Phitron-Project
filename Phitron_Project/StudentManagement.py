#Python Midterm Assignment

class Student:
    def  __init__( self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)


    def enroll_student(self):
        if self.__is_enrolled:
            raise ValueError(f"{self.__name} is Already Enrolled.")
        self.__is_enrolled = True
        return f"{self.__name} enrolled successfully."
   
    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError(f"Sorry {self.__name} is not currently enrolled.")
        self.__is_enrolled = False
        return f"{self.__name} dropped"
   
    def view_student_info(self):
        current_status = "Enrolled" if self.__is_enrolled else "Not Enrolled."
        return (f"Student ID : {self.__student_id}\n"
                f"Name       : {self.__name}\n"
                f"Department : {self.__department}\n"
                f"Status     : {current_status}"
                )
   
    @property
    def student_id(self):
        return self.__student_id
   
    @property
    def name(self):
        return self.__name
   
    @property
    def department(self):
        return self.__department
   
    @property
    def is_enrolled(self):
        return self.__is_enrolled
       


class StudentDatabase:
    student_list = []


    @classmethod
    def add_student(cls,new_student):
        cls.student_list.append(new_student)
        return f"{new_student} added to the System."
   
    @classmethod
    def get_by_id(cls, sid):
        for stud in cls.student_list:
            if stud.student_id == sid:
                return stud
        raise ValueError(f"No student found with ID: {sid}")
   
    @classmethod
    def show_all(cls):
        if not cls.student_list:
            return "No students in the Database"
        return "\n\n".join(student.view_student_info() for student in cls.student_list)
       


s1 = Student(830001, "Niloy Chandra Datta", "Computer Science and Engineering ", True)
s2 = Student(830002, "Anik Gupta Tarun", "Computer Science and Engineering ", True)
s3 = Student(830003, "Nurul Absar Sadik", "Computer Science and Engineering ", True)
s4 = Student(830004, "Salman Sayeed", "Computer Science and Engineering ", False)
s5 = Student(830005, "Shubrata Basak Shuvo","Computer Science and Engineering ", False)
s6 = Student(830006, "Zihad Hasan" ,"Computer Science and Engineering ", True)
s7 = Student(830007, "Dipto Dey","Computer Science and Engineering ", True)
s8 = Student(830008, "Zaheed","Computer Science and Engineering ", True)
s9 = Student(830009, "Chris Hui","Computer Science and Engineering ", True)
s10 = Student(8300010, "Erik Demine","Computer Science and Engineering ", True)


# StudentDatabase.add_student(s1)
# StudentDatabase.add_student(s2)
# StudentDatabase.add_student(s3)
# StudentDatabase.add_student(s4)
# StudentDatabase.add_student(s5)
# StudentDatabase.add_student(s6)
# StudentDatabase.add_student(s7)
# StudentDatabase.add_student(s8)
# StudentDatabase.add_student(s9)
# StudentDatabase.add_student(s10)




def menu_loop():
    while True:
        print("\n--- Student Management Menu ---")
        print("1. View All Students")
        print("2. Enroll a Student")
        print("3. Drop a Student")
        print("4. Quit")


        user_input = input("Enter your choice(1-4): ").strip()


        if user_input == "1":
            print("\nCurrent Students")
            print(StudentDatabase.show_all())
       
        elif user_input =='2':
            try :
                sid = int(input("Enter Student ID to Enroll:\n"))
                person =StudentDatabase.get_by_id(sid)
                print(person.enroll_student())


            except ValueError as error:
                print(f"{error}")


           
        elif user_input =="3":
            try:
                sid = int (input("Enter Student ID to drop:\n"))
                person = StudentDatabase.get_by_id(sid)
                print(person.drop_student())


            except ValueError as error:
                print(f"{error}")


        elif user_input =='4':
            print("Goodbye, Dear Student.")
            break


        else:
            print("Sorry , this is not a valid choice. Please Enter a number between 1 to 4.")






if __name__ =="__main__":
    menu_loop()
