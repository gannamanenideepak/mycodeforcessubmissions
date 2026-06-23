q=int(input())
for i in range(q):
    s=input()
    t=input()

    c=0
    for j in range(min(len(s),len(t))):
        if(s[j]==t[j]):
            c+=1
        else:
            break

    if(c==0):
        print(len(s)+len(t))
    else:
        print(len(s)+len(t)-c+1)