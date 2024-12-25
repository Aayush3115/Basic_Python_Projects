import math
import random

print("Welcome To The Game")
print("I am Gussing Between 1 to 100")
number=random.randint(1,100) 

print("Select Difficulty level:")
print(" 1.Easy(10 Guess) \n 2.Medium(6 Guess) \n 3.Hard(3 Guess)\n ")
Guess=int(input("Enter Your Choice:"))


if Guess==1 :
    remaining=10
    for i in range(10):
        x=int(input("Enter Your Guess:"))
        if number==x:
            print(f"Correct You Took {i+1} Attempt!",)
            break
        else:
            remaining=remaining-1
            if remaining==0:
                print("Game Over You Failed To Guess!!!!!")
            else:
                if number>x:
                    print(f"Incorrect Number is greater than {x}")
                else:
                    print(f"Incorrect Number is less than {x}")
                print(f"Remaining attempts:{remaining}\n",)

elif Guess==2 :
    remaining=6
    for i in range(6):
        x=int(input("Enter Your Guess:"))
        if number==x:
            print(f"Correct You Took {i+1} Attempt!",)
            break
        else:
            remaining=remaining-1
            if remaining==0:
                print("Game Over You Failed To Guess!!!!!")
            else:
                if number>x:
                    print(f"Incorrect Number is greater than {x}")
                else:
                    print(f"Incorrect Number is less than {x}")
                print(f"Remaining attempts:{remaining}\n",)
    

elif Guess==3 :
    remaining=3
    for i in range(3):
        x=int(input("Enter Your Guess:"))
        if number==x:
            print(f"Correct You Took {i+1} Attempt!",)
            break
        else:
            remaining=remaining-1
            if remaining==0:
                print("Game Over You Failed To Guess!!!!!")
            else:
                if number>x:
                    print(f"Incorrect Number is greater than {x}")
                else:
                    print(f"Incorrect Number is less than {x}")
                print(f"Remaining attempts:{remaining}\n",)
    

else :
    print("Error While Selecting!!!!")

