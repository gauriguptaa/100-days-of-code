# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number:")
print(int(int(two_digit_number)/10)+int(two_digit_number)%10)
#Another Solution was extracting the digits in string format i.e int(two_digit_number[0])+int(two_digit_number[1]) 
