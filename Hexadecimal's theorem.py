n = int(input())

# Special cases
if n == 0:
    print(0, 0, 0)
    exit()
if n == 1:
    print(0, 0, 1)
    exit()

# Generate Fibonacci numbers
fib = [0, 1]
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])

# Find representation
k = fib.index(n)
print(fib[k-2], fib[k-1], 0)
