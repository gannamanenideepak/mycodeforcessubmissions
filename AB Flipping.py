t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    first=s.find('A')
    last=s.rfind('B')

    if first==-1 or last==-1 or first>last:
        print(0)
    else:
        print(last-first)