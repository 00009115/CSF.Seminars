s1 = (18, 00009898, "Samarkand")
s2 = (19, 00009597, "Tashkent")

if s1[0] > s2[0]:
    print("Student with an ID of", s1[2], "is older than", "Student with an ID of", s2[2])
elif s1[0] == s2[0]:
    print("Student with an ID of", s1[2], "is in the same age with", "Student with an ID of", s2[2])
else:
    print("Student with an ID of", s2[2], "is older than", "Student with an ID of", s1[2])
