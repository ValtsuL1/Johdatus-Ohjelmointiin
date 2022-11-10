weeklyHours = input("Syötä viikon työtunnit: ")
salary = input("Syötä tuntipalkkasi: ")
weeklyHours = float(weeklyHours)
salary = float(salary)

if weeklyHours > 40:
    overtime = weeklyHours - 40
    overtimewage = overtime * salary * 1.5
    wage = salary * (weeklyHours - overtime) + overtimewage
    wage = round(wage, 2)
    print(f"Viikon ansiosi ovat: {wage} €")
if weeklyHours <= 40:
    wage = salary * weeklyHours
    wage = round(wage, 2)
    print(f"Viikon ansiosi ovat: {wage} €")
