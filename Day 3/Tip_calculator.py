total_bill = float(input("what was the total bill?"))
percent_tip = int(input("what percent tip would you like to give?"))
split_among = int(input("Among how many people to split the bill?"))

tip_calculator = float((total_bill * percent_tip) / (100 * split_among))


print("Each person should pay","$",tip_calculator,"in tip and total ")