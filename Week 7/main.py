my_marks = {
    "CSF": 68,
    "FunPro": 65,
    "WebTech": 72
}


def calculator(marks):
    average_mark = 0
    for mark in marks:
        average_mark += mark
    return average_mark / len(my_marks)

print("Average mark is:", calculator(list(my_marks.values())))

