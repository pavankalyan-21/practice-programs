#a=[1,1,2,2,4,4,5,5,5]
a=list(map(int, input().split()))
b=set(a)
count=0
for i in b:
    c=a.count(i)
    c1=a.count(i+1)
    c2=a.count(i-1)
    if c1>c2:
        c=c+c1
    else:
        c=c+c2
    if count<c:
        count=c
print(count)