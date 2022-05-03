# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2

if bmi < 18.5:
  print("Your BMI is {:.2f} kg/m2, you are Underweight.".format(bmi),)
elif bmi < 25:
  print("Your BMI is {:.2f} kg/m2, you have a Normal Weight.".format(bmi))
elif bmi < 30:
  print("Your BMI is {:.2f} kg/m2, you are Slightly Overweight.".format(bmi))
elif bmi <35:
  print("Your BMI is {:.2f}, you are Obese(fat).".format(bmi))
else:
  print("Your BMI is {:.2f}, you are Clinically Obese.".format(bmi))






