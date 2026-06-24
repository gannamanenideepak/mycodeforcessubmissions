t=int(input())

for _ in range(t):
    s=input()

    c=0
    i=0

    while i<len(s):
        if s[i]=='0':
            c+=1
            while i<len(s) and s[i]=='0':
                i+=1
        else:
            i+=1

    if c==0:
        print(0)
    elif c==1:
        print(1)
    else:
        print(2)