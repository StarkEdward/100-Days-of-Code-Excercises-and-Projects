# Creating a function for prime number checker
def Prime_checker(number):
    if number > 1:
        isPrime = True
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
        if isPrime:
            print("It's a Prime number.")
        else:
            print("It's not a Prime number.")
    else:
        print("It's not a Prime number.")

n = int(input("Enter Number to check: "))

# calling a function
Prime_checker(number = n)