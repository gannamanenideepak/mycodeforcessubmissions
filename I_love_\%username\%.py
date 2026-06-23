n = int(input())
scores = list(map(int, input().split()))
 
best = scores[0]
worst = scores[0]
count = 0
 
for i in range(1, n):
    if scores[i] > best:
        count += 1
        best = scores[i]
    elif scores[i] < worst:
        count += 1
        worst = scores[i]
 
print(count)