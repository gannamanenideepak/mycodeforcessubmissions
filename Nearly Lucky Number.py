n = input()

count = 0

# count lucky digits
for ch in n:
    if ch == '4' or ch == '7':
        count += 1

# check if count is lucky
if count == 0:
    print("NO")
else:
    s = str(count)
    for ch in s:
        if ch != '4' and ch != '7':
            print("NO")
            break
    else:
        print("YES")
