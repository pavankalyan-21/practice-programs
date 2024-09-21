b=int(input())
k=list(map(int, input().split()))
u=list(map(int, input().split()))
mk=min(k)
mu=min(u)
cost=[]
for i in k:
    for j in u:
        t=i+j
        if t<b:
            cost.append(t)
if len(cost)==0:
    print(-1)
else:
    print(max(cost))
