class Student:

    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Ism: {self.name}, Yosh: {self.age}")
   
         


t1=Student("Bekzod", 22 )
t2=Student("Jonibek", 19 )
t3=Student("Ali", 16 )
t4=Student("Vali", 26 )
t5=Student("Sami", 19 )

students = [t1, t2, t3, t4, t5]


oldest_student = max(students, key=lambda student: student.age)



oldest_student.show_info()

   