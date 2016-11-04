# guess the number.



import random

random_num = random.randint(1,10)

tipp = -1


for i in range(0,10):
    print("You have " + str(10 - i) + " try/tries left!")
    tipp = int(input("Guess a number between one and ten!"))

    if random_num == tipp:
        print("YOU WIN!")
        break
    else:
        print("Try again!")
    if random_num > tipp:
        print("Guess a bigger number!")
    if random_num < tipp:
        print("Guess a smaller number!")

if random_num != tipp:
    print("You Lose!")


