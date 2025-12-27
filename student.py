def display_grade_table():
    print("\n--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------")


def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


def main(
    name="NIKHIL",
    dept="BCA",
    sem="3",
    m1=85,
    m2=90,
    m3=95
):
    print("\n--- Student Details ---")
    print("Name:", name)
    print("Department:", dept)
    print("Semester:", sem)

    display_grade_table()

    avg = (m1 + m2 + m3) / 3

    print("\nAverage Marks:", avg)

    grade = calculate_grade(avg)
    print("Final Grade:", grade)


if __name__ == "__main__":
    main()
