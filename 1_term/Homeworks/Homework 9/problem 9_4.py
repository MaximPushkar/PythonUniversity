import random


n = int(input())
for i in range(10):
    counter = 0
    correct = 0
    for i in range(n):
        counter += 1
        x, y = random.randint(1, 6), random.randint(1, 6)
        if max(x, y) <= 4:
            correct += 1
    print(correct / counter)
print(16/36)