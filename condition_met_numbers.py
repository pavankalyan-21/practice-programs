a=list(map(int, input().split()))
b=list(map(int, input().split()))
count=0
for i in range(2,min(b)+1):
    flag=0
    for j in a:
        if(i%j==0):
            flag+=1
    flag2=0
    if(flag==len(a)):
        for j in b:
            if (j%i==0):
                flag2+=1
    if(flag2==len(b)):
        count+=1
print(count)