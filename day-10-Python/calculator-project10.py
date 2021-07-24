from art import logo
from replit import clear

def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  if n2!=0:
    return n1/n2        

def calculate():
  print(logo)
  use_prev_output=True
  n1=int(input("What's the first number?: "))
  print(" +\n -\n *\n /")
  while use_prev_output:
    option = input('pick an operation: ')
    if option not in ['+','-','*','/']:
      print("Please select a valid operation.")
      clear()
      calculate()
    n2=int(input("What's the next number?: "))
    operations = {
    '+': add(n1,n2),
    '-': sub(n1,n2),
    '*': mul(n1,n2),
    '/': div(n1,n2)
    }
    output=operations[option]
    print(f"{n1} {option} {n2} = {output}")
    n1=output
    choice=input(f"Type 'y' to continue calculations with {output},'n' to start new calculations: ").lower()
    if choice == 'y':
      use_prev_output=True
    elif choice =='n':
      use_prev_output=False
      clear()
      calculate()   
    else:
      use_prev_output=False  
calculate()
