# Visit this link and copy paste or type the below code to run.

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Hurdle challenge 1
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
# using for loop
#for i in range(6):
#    jump()

# using while loop
number_of_hurdle = 6
while number_of_hurdle > 0 :
    jump()
    number_of_hurdle -= 1