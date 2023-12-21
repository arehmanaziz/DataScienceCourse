bill = float(input("Input bill: "))
people = int(input("Input number of people: "))
tip_percent = float(input("Tip percent: "))
total_bill = bill + (bill*(tip_percent/100))
each_person = total_bill / people
round_bill = format(each_person, ".2f")

print(f"Every person should pay {round_bill}Rs. amount.")