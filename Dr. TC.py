t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    o_c=s.count('1')
    res=0
    for i in range(len(s)):
        if(s[i]=='1'):
            res+=o_c-1
        else:
            res+=o_c+1
    print(res)