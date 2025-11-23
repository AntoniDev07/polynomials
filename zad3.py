x, n, *a = map(int,input().split())

y = a[n]
for i in range(n-1,-1,-1):
    y = x*y+a[i]
print(y)    
