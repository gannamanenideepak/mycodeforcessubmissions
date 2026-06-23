t=int(input())
for i in range(t):
    m=int(input())
    m_s=input()
    n=int(input())
    n_s=input()
    o=input()
    res=m_s
    for i in range(len(o)):
        if(o[i]=="D"):
            res+=n_s[i]
        else:
            res=n_s[i]+res
    print(res)