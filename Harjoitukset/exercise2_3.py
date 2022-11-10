salary = input("Anna kuukausipalkkasi: ")
tax = input("Anna veroprosenttisi: ")
salary = float(salary)
tax = float(tax)
tax_amount = tax / 100 * salary
tax_amount = round(tax_amount, 2)
net_salary = salary - tax_amount
net_salary = round(net_salary, 2)
print(f"Käteenjäävä osuus: {net_salary} €")
print(f"Verot: {tax_amount} €")
