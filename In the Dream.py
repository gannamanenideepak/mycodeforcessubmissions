t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    x1,y1=max(a,b),min(a,b)
    x2,y2=max(c-a,d-b),min(c-a,d-b)
    if(x1<=2*(y1+1)) and (x2<=2*(y2+1)):
        print("YES")
    else:
        print("NO")