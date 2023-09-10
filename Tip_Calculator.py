print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, 15? ")
people = input("How many people to split the bill? ")
calculate_tip = round((float(total) * (1+float(tip)/100)) / int(people),2)

print(f"Each person should pay: ${calculate_tip}")