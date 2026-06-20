salary = int(input("enter the salary: "))
bonus = 0

if salary >= 70000:
    bonus = salary * 0.2
elif salary >= 50000:
    bonus = salary * 0.15
elif salary >= 30000:
    bonus = salary * 0.1
else :
    bonus = salary * 0.05

    print("Bonus : ",bonus)