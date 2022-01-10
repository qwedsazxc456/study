a=[1,1,1,2,2]+[0 for _ in range(95)]
t=int(input())
for i in range(95):
    a[i+5] = a[i]+a[i+4]
for _ in range(t):
    n = int(input())
    print(a[n-1])