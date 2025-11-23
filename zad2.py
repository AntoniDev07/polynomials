
x, n = map(int,input().split())

poly = (x,n)
y =1
for i in range(n):
    y=x*y+1
print(y)    