n=int(input())
i=1
name=[]
while i<=n:
    m=input()
    name.append(m)
    i+=1
m=int(input())
n=1
while n<=m:
    u,v=map(int,input().split())
    name[u-1]='I_love_'+name[v-1]
    n+=1
print(name[0])