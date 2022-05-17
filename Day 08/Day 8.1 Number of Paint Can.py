from math import ceil


# creating a function of Paint_Calc
def PaintCalc(height, width, cover):
    area = (height * width)
    Num_of_can = ceil((area / cover))
    print(f"You'll need {Num_of_can} cans of paint.")


h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5

# calling a function

PaintCalc(height=h, width=w, cover=coverage)
