max = 0

for a in range(1, 61):
    for b in range(1, 62 - a):
        for c in range(1, 61 - a - b):
            d = 63 - a - b - c
            new = a * b + b * c + c * d
            max = new if new > max else max
print(max)