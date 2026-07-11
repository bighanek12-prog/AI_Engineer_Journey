class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")

    def is_adult(self):
        return self.age >= 18
    

    def celebrate_birthday(self):
      self.age += 1

student1 = Student("Kunal", 24, "M.Sc Computer Science")
student2 = Student("Rahul", 22, "B.Tech")

student1.display_info()

student1.celebrate_birthday()

print("\nAfter Birthday:")
student1.display_info()

print("Adult:",student1.is_adult())

student2.display_info()

student2.celebrate_birthday()

print("\nAfter Birthday:")
student2.display_info()

print("Adult:",student2.is_adult())
