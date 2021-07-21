#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def challenge_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for i in range(0,6):
    challenge_hurdle()

'''
Using While loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():   
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
   
no_of_hurdles=5    
while no_of_hurdles >=0 :
     jump()
     no_of_hurdles-=1   

'''
