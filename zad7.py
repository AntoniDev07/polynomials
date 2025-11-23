import math

a = list(map(int, input().split()))
A, B, C, D = a
# pochodna 3 * A * x**2 + 2 * B * x + C
delta = 4 * B**2 - 4 * 3 * A * C
if delta > 0:
    x1 = (-2 * B - math.sqrt(delta)) / (2 * 3 * A)
    x2 = (-2 * B + math.sqrt(delta)) / (2 * 3 * A)

    y1 = A * x1**3 + B * x1**2 + C * x1 + D
    y2 = A * x2**3 + B * x2**2 + C * x2 + D
    print(x1, y1)
    print(x2, y2)
elif delta == 0:
    x = -2 * B / (2 * 3 * A)
    y = A * x**3 + B * x**2 + C * x + D
    print(x, y)
else:
    print("Funkcja nie ma ekstremum rzeczywistego :<")
