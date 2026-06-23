t=int(input())
for i in range(t):
    n=int(input())
    e=list(input())
    g=list(input())
    res=0

    for j in range(n):
        if(g[j]=='1'):

            if(e[j]=='0'):
                res+=1

            elif(j==0):
                if(e[j+1]=='1'):
                    res+=1
                    e[j+1]='0'

            elif(j==n-1):
                if(e[j-1]=='1'):
                    res+=1
                    e[j-1]='0'

            else:
                if(e[j-1]=='1'):
                    res+=1
                    e[j-1]='0'

                elif(e[j+1]=='1'):
                    res+=1
                    e[j+1]='0'
    print(res)