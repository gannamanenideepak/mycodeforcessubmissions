s=input()
printed=False
for i in s:
    if i=='H' or i=='Q' or i=='9':
        print("YES")
        printed=True
        break
if not printed:
    print("NO")