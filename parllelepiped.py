import math

x, y, z = map(int, input().split())

a = int(math.sqrt(x * z // y))
b = int(math.sqrt(x * y // z))
c = int(math.sqrt(y * z // x))

print(4 * (a + b + c))
