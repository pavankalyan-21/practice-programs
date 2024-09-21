a = list(map(int, input().split()))
cnt = 0
b = set(a)
for i in b:
    c = a.count(i)
    cnt += (c // 2)
print(cnt)
