import random

x = 0
y = []
z = 0

while z == 0:
    pass_length = int(input("How long do you want the password to be: "))
    while x < pass_length:
        random_choice = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        y.append(random_choice)
        x += 1
        man = "".join(y)
    print(pass_length)
    man = input("again(yes or no)?: ")
    if man == "yes":
        print("ok")
        x = 0
        y = []
    elif man == "no":
        print("ok")
        z += 1
    else:
        print("You didn't answer correctly!")
        z += 1
