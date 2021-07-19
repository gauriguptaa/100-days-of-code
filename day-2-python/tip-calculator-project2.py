print("Welcome to the tip calculator.\n")
total_bill=float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people=int(input("How many people to split the bill?\n"))
share=(total_bill+((total_bill*tip)/100))/people
share=round(share,2)
#.format is handy little trick for formatting a digit to 2 decimal places
print(f"Each Person should pay {'{0:.2f}'.format(share)}")
