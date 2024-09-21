n = int(input())
def bill(n):
    even, odd = 0,0
    while(n>0):
        rem=n%10
        if rem%2 ==0:
            even += rem
        else:
            odd += rem
        n=n//10
    return odd*even
print(bill(n))