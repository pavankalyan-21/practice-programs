x=list(map(int, input().split()))
j=[]
for i in x:
    if i%2 ==0 :
        j.append(i)
for i in x:
    if i %2 !=0:
        j.append(i)
print(j)