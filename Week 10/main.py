class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display_name(self):
        print(self.firstname, self.lastname)


student1 = Student("Khasanboy", "Khabibullaev")

Student.display_name(student1)