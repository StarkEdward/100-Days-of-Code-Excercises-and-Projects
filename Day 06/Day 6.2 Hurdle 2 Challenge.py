# Visit this link and copy paste or type the below code to run.

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# Hurdle 2 Challenge

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

# method 1
while not at_goal():
   jump()

# method 2
# while at_goal() != True:
#    jump()
#
# method 3
#flag = at_goal()
#while flag == at_goal():
#    jump()