import random
playing=True
number=str(random.randint(1,10))

print("i will generate random numbers from 1 to 10, then you guess the number,!!")
print("game ends when you get 1 hero!")
while playing:
    guess=(input("give me your best guess \n"))
    if guess=="":
     print("print enter a number")
     continue
     guess=int(guess)
 
    if number==guess:
        print("you win the game!")
        print("the number was: ",number)
        break
    else:
        print("try again the number is not",guess)
    