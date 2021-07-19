#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = int(input("What is your current age?\n"))
print(f"You have {(90-age)*365} days, {(90-age)*52} weeks, and {(90-age)*12} months left.")
