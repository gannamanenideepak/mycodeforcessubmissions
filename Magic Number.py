n = input().strip()

# Rule 1: must start with 1
if n[0] != '1':
    print("NO")
    exit()

# Rule 2: only digits 1 and 4 allowed
for ch in n:
    if ch != '1' and ch != '4':
        print("NO")
        exit()

# Rule 3: no "444"
if "444" in n:
    print("NO")
else:
    print("YES")
