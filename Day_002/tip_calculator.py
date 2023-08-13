# udemy Course - 100 Days of Code - Python#

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal placed = 33.60

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? €/$"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
count_people = int(input("How many people to split the bill? "))

pay_per_person = round(total_bill * ((percentage_tip + 100) / 100) / count_people,2)
print(f"Each person should pay: €/${pay_per_person:.2f}")
