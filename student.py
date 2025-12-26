def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    sem = input("Enter Semester: ")

    m1 = int(input("Enter marks 1: "))
    m2 = int(input("Enter marks 2: "))
    m3 = int(input("Enter marks 3: "))

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("Grade:", grade)


if _name_ == "_main_":
    main()