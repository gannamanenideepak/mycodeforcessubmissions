n = int(input())
a = list(map(int, input().split()))
 
max_val = max(a)
min_val = min(a)
 
# first occurrence of maximum
max_idx = a.index(max_val)
 
# last occurrence of minimum
min_idx = n - 1 - a[::-1].index(min_val)
 
ans = max_idx + (n - 1 - min_idx)
 
# overlap correction
if max_idx > min_idx:
    ans -= 1
 
print(ans)