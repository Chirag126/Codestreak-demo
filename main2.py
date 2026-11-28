def two_sum(nums, target):
    pairs = sorted((n, i) for i, n in enumerate(nums))
    left, right = 0, len(pairs) - 1
    while left < right:
        total = pairs[left][0] + pairs[right][0]
        if total == target:
            return sorted([pairs[left][1], pairs[right][1]])
        if total < target: left += 1
        else: right -= 1
print(two_sum([3, 2, 4], 6))

import random

secret = random.randint(1, 100)
tries = 0
while True:
    guess = int(input("Guess a number (1-100): "))
    tries += 1
    if guess == secret:
        print(f"Correct! You got it in {tries} tries."); break
    print("Too high!" if guess > secret else "Too low!")