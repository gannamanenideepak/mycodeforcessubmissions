t=int(input())

for _ in range(t):
    n=int(input())
    s=input()

    ans=[]
    i=n

    while i>0:
        if i==2:
            ans.append(s[i-2:i])
            break

        if s[i-2] in "ae":
            ans.append(s[i-2:i])
            i-=2
        else:
            ans.append(s[i-3:i])
            i-=3

    print(".".join(ans[::-1]))