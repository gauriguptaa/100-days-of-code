from replit import clear

from art import logo

print(logo)
secret_auction=True
participants=[]
while secret_auction:
  bidder={}
  print("Welcome to the secret auction program.\n")
  name=input("What is your name?: ")
  bid=float(input("What's your bid?: $"))
  bidder={"name":name,"bid":bid}
  participants.append(bidder)
  option=input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  clear()
  if option == "yes":
    secret_auction=True
  else:
    secret_auction=False
#print(participants)

#Calculate who has highest bid

max_bid=0
max_bidder_name=''
for bidder in participants:
  if bidder['bid']>max_bid:
    max_bidder_name=bidder['name']
    max_bid=bidder['bid']
print(f"{max_bidder_name} has maximum bid of ${max_bid}")
