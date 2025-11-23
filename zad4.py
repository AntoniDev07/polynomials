import random

n = random.randint(2, 6)
a = [random.randint(1, 9) for _ in range(n + 1)]
xr = 2
y = a[n]
for i in range(n - 1, -1, -1):
    y = xr * y + a[i]
print(y)
