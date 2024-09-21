# Chaitan went to a zoo he is given id to each and every animal he saw 
# he wants to determine the id of the most frequently seen animal if more than
# one type has been spoted the maximum amount return the smallest of their id's.

# taking inputs
x=list(map(int,input().split()))
# initializing count and ids as zero 
count=0
id=0

for i in x:
    #counting how many time an animal has spotted
    c=x.count(i)
    # if the count is greater than previous animals then id will be changed to the animals
    if(c>count):
        count=c
        id=i
    # if the count is less than previous count the id remains same
    elif(c==count and i<id):
        id=i
# printing the id of animal which has spotted most
print (id)
