x=list(map(int,input().split()))
count=0
id=0
for i in x:
    c=x.count(i)
    if(c>count):
        count=c
        id=i
    elif(c==count and i<id):
        id=i
print (id)