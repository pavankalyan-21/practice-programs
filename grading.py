'''g=list(map(int, input().split()))
idx=0
for i in g:
    if i>0 and i<=100:
        if i<38 or i>100:
            pass
        else:
            nm=((int(i//5))+1)*5
            dif=nm-i
            if dif<3:
                g[idx]=nm
        idx +=1
    else:
        g.remove(i)
print(g)'''
li=list(map(int, input().split()))
for i in range(len(li)):
    if(li[i]>=38):
        if((li[i]+1)%5==0):
            li[i]=li[i]+1
        elif((li[i]+2)%5==0) :
            li[i]=li[i]+2
print(li)
