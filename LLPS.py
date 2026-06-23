s = input().strip()
n = len(s)

def is_palindrome(x):
    return x == x[::-1]

def is_lex_greater(a, b):
    m = min(len(a), len(b))
    for i in range(m):
        if a[i] != b[i]:
            return a[i] > b[i]
    return len(a) > len(b)

best = ""

# generate all non-empty subsequences
for mask in range(1, 1 << n):
    cur = ""
    for i in range(n):
        if mask & (1 << i):
            cur += s[i]

    if is_palindrome(cur):
        if best == "" or is_lex_greater(cur, best):
            best = cur

print(best)
