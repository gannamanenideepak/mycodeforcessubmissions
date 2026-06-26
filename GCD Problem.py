import math
t=int(input())
for i in range(t):
    n=int(input())
    b=2
    while(True):
        a=n-1-b
        if(math.gcd(a,b)==1):
            print(a,b,1)
            break
        b+=1