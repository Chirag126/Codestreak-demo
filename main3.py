import random

secret = random.randint(1, 100)
tries = 0
while True:
    guess = int(input("Guess a number (1-100): "))
    tries += 1
    if guess == secret:
        print(f"Correct! You got it in {tries} tries."); break
    print("Too high!" if guess > secret else "Too low!")