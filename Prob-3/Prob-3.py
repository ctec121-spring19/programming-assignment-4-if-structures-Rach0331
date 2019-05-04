# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Rachel Watson

def letterGrade(score):
    # your code here
    if score <= 1:
        grade = "F"
    elif score == 2:
        grade = "D"
    elif score == 3:
        grade = "C"
    elif score == 4:
        grade = "B"
    elif score == 5:
        grade = "A"
    else:
        grade = "Invalid value"

    return grade

def unitTest():
    # your test code here
    for score in range(7):
        print("Score:", score, "returns a grade of:", letterGrade(score))
if __name__ == "__main__":
    unitTest()