r=list(map(int,input().split()))
max,min=r[0],r[0]
mxcnt,mncnt=0,0
for i in r:
    if i>max:
        max=i
        mxcnt+=1
    elif i<min:
        min=i
        mncnt+=1
print(mxcnt,mncnt)