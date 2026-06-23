n=int(input())
arr=list(map(int, input().split()))
m=int(input())
q=list(map(int, input().split()))
pos = {}
for i in range(n):
    pos[arr[i]] = i + 1

vasya = 0
petya = 0

for x in q:
    p = pos[x]
    vasya += p             
    petya += n - p + 1     

print(vasya, petya)
