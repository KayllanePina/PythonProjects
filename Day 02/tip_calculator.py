print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip = float(bill) * (100 + int(percentage)) / 100
qtd_people = input("How many people to split the bill? ")
total_bill = tip / int(qtd_people)

print(f"Each person should pay: ${round(total_bill, 2)}")


