__author__ = 'Administrator'

def grades_average(grade1, grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50:
        total = total + grade1
        grade_count = grade_count + 1
    elif grade2 >= 50:
        total = total + grade2
        grade_count = grade_count + 1

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)
print(grades_average(0.0, 55))#<- 55
print(grades_average(0.0, 45))#<- 0.0
print(grades_average(45, 55))#<- 55
print(grades_average(75, 55))#<- 65
print('------------------/-/-/-/-/-/-/-////-/-/-/-/---------------------')

def grades_average1(grade1, grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50 and grade2 >= 50:
        total = grade1 + grade2
        grade_count = 2

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)
print(grades_average1(0.0, 55))#<- 55
print(grades_average1(0.0, 45))#<- 0.0
print(grades_average1(45, 55))#<- 55
print(grades_average1(75, 55))#<- 65
print('------------------/-/-/-/-/-/-/-////-/-/-/-/---------------------')

def grades_average2(grade1, grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50:
        total = total + grade1
        grade_count = grade_count + 1
    if grade2 >= 50:
        total = total + grade2
        grade_count = grade_count + 1

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)
print(grades_average2(0.0, 55))#<- 55
print(grades_average2(0.0, 45))#<- 0.0
print(grades_average2(45, 55))#<- 55
print(grades_average2(75, 55))#<- 65
print('------------------/-/-/-/-/-/-/-////-/-/-/-/---------------------')

def grades_average3(grade1, grade2):
    total = 0
    grade_count = 0

    if grade1 >= 50:
        total = total + grade1
        grade_count = grade_count + 1
    else:
        total = total + grade2
        grade_count = grade_count + 1

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)
print(grades_average3(0.0, 55))#<- 55
print(grades_average3(0.0, 45))#<- 0.0
print(grades_average3(45, 55))#<- 55
print(grades_average3(75, 55))#<- 65