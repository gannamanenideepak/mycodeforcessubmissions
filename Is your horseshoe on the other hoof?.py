lis=list(map(int,input().split()))
dic={}
for i in lis:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
if(len(dic)>=4):
    print(0)
else:
    print(4-len(dic))