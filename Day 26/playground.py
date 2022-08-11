# *args many positional arguments

def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum
    # for n in args:
    #     print(n)


print(add(3, 5, 6, 4, 5))