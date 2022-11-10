import statistics

student_amount = int(input("Opiskelijoiden lukumäärä:\n"))

grades = []

for x in range(student_amount):
    grade = int(input("Anna opiskelijan arvosana:\n"))
    grades.append(grade)

grade_average = sum(grades) / len(grades)
grade_average = round(grade_average, 1)

print(f"Keskiarvo: {grade_average}")

if 0 <= grade_average < 1:
    print("Huono tulos")
elif 1 <= grade_average < 2:
    print("Heikko tulos")
elif 2 <= grade_average < 3:
    print("Tyydyttävä tulos")
elif 3 <= grade_average < 4:
    print("Hyvä tulos")
elif 4 <= grade_average <= 5:
    print("Kiitettävä tulos")

grade_median = statistics.median(grades)

print(f"Mediaani: {grade_median}")

grade_most_common = statistics.mode(grades)

print(f"Yleisin arvosana: {grade_most_common}")
