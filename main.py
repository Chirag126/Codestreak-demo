x = 2
y = x * 5
print("x =", x, "y =", y)
total = x + y
print("Sum:", total)
numbers = [x, y, total, 7, 3]
print("List:", numbers)
print("Max:", max(numbers), "Min:", min(numbers))
squares = [n ** 2 for n in numbers]
print("Squares:", squares)
if total % 2 == 0:
    print(total, "is even")
else:
    print(total, "is odd")
for i in range(1, 4):
    print(x, "x", i, "=", x * i)
def area(length, width):
    return length * width
print("Area:", area(x, y))
print("Average:", sum(numbers) / len(numbers))

nums, target = [2, 7, 11, 15], 9
seen = {}
for i, n in enumerate(nums):
    if target - n in seen: print([seen[target - n], i])
    seen[n] = i

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
