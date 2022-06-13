# 15649
from itertools import permutations as p
n,m = map(int, input().split())
a=[i for i in range(1,n+1)]
for i in list(p(a,m)):
    for j in i:
        print(j, end=' ')
    print()