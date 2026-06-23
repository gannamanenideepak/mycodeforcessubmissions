t=int(input())

for _ in range(t):
    n=int(input())
    s=input()
    pos=s.rfind(min(s))
    print(s[pos]+s[:pos]+s[pos+1:])