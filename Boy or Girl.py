s = input().strip()
distinct = len(set(s))

if distinct % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
