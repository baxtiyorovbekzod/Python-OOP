class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade} .")

t1 = Student("Bekzod", 22, "2-kurs talabasi")


t1.info()