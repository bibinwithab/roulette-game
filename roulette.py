print("RUSSIAN ROULETTE")
print("""Rules:
        >Enter a number from 1 to 6 to fire the gun.
        >And wish luck.""")

import random

bullet = random.randint(1, 6)
count = 0
shots_fired = 6
while count < shots_fired:
    guess = int(input("Enter a number: "))
    count += 1
    if guess == bullet:
        print("YOU DIED!")
        break
    else:
        print("You live to see another day.")