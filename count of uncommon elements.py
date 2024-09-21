a=list(map(int, input().split()))
b=list(map(int, input().split()))
count=0
for i in a:
    if i not in b:
        count +=1
for i in b:
    if i not in a:
        count +=1
print(count)