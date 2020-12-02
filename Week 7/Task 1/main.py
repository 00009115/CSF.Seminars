class Student:
    def __init__(self, id, marks):
        self.id = id
        self.marks = marks

    def calculator(self):
        total_mark = 0

        for mark in self.marks:
            total_mark += mark
        return total_mark / len(self.marks)

    def display(self):
        print("Average mark is:", self.calculator())

if __name__ == '__main__':
    student1 = Student(9115, {
                                "CSF": 68,
                                "FunPro": 69,
                                "WebTech": 72
                             }
    )
    student1.display()
    student2 = Student(9589, {
                                "CSF": 46,
                                "FunPro": 65,
                                "WebTech": 68
                             }
    )
    student1.display()