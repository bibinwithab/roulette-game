print("*********RUSSIAN ROULETTE*********")
print("""Rules:
        >Enter a number from 1 to 6 to fire the gun.
        >And wish luck.""")

import random

def game():
    bullet = random.randint(1, 6)
    count = 0
    shots_fired = 6
    while count < shots_fired:
        guess = int(input("Enter a number from one to six: "))
        count += 1
        if guess == bullet:
            print("YOU DIED!")
            break
        else:
            print("You live to see another day.")

ans = input("Wanna contiue? (y/n)").lower()
if ans == "y":
    game()
else:
    print("Bye!")
