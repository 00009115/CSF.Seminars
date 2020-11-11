my_marks = {
    "CSF": 68,
    "FunPro": 69,
    "WebTech": 72
}


def calculator(marks):
    total_mark = 0
    for mark in marks:
        total_mark += mark
    return total_mark / len(my_marks)

print("Average mark is:", calculator(my_marks.values()))

