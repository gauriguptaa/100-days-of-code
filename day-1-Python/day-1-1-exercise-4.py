#Write a program that switches the values stored in the variables a and b.
a = int(input("a: "))
b = int(input("b: "))
a=a+b
b=a-b
a=a-b
#If 3rd variable needs to be used then (x=a a=b b=x )
print("a: " + str(a))
print("b: " + str(b))
#In Python we could also do a,b=b,a 
