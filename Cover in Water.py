t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    res=0
    for i in range(1,len(s)-1):
        if(s[i]==s[i-1] and s[i]==s[i+1] and s[i]=='.'):
            res+=2
            print(res)
            break
    if(res==0):
        print(s.count('.'))
    