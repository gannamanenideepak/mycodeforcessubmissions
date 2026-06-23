t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    res=""
    i=0
    while(i<n):
        c=s[i]
        res+=c
        i+=1
        while(i<n and s[i]!=c):
            i+=1
        i+=1
    print(res)