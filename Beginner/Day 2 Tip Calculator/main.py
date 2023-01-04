print("Here is Toyin's tip calculator")
bill = float(input("What was the total bill?\n$"))
tip = int(input("Was the tip 10, 12 or 15?\n"))
people_split = int(input("How many people are splitting the bill?\n"))
tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_per_person = total_bill / people_split
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}" )
