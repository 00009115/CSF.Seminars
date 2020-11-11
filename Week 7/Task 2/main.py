csf_assessment = {
    "cw-weight": 0.4,
    "cw-mark": 69,
    "exam-weight": 0.6,
    "exam-mark": 65
}


def calculator(assessment):

    cw = assessment.get("cw-mark", 0) * assessment.get("cw-weight")
    exam = assessment.get("exam-mark", 0) * assessment.get("exam-weight")

    return cw + exam

print("Final mark is:", calculator(csf_assessment))

