n = int(input())
seq = list(map(int, input().split()))
max_value=[seq[0]]+[0]*(n-1)
len_b=[1]+[0]*(n-1)
for i in range(1,len(seq)):
    max_len = -1
    for j in range(i):
        if seq[i] > max_value[j] and max_len<len_b[j]:
            max_value[i] = seq[i]
            max_len = len_b[j]
    if max_len == -1:
        max_value[i] = seq[i]
        len_b[i] = 1
    else: len_b[i] = max_len+1
max_value_r=[0]*(n-1)+[seq[-1]]
len_b_r=[0]*(n-1)+[1]
for i in range(len(seq)-2,-1,-1):
    max_len = -1
    for j in range(len(seq)-1,i,-1):
        if seq[i] > max_value_r[j] and max_len<len_b_r[j]:
            max_value_r[i] = seq[i]
            max_len = len_b_r[j]
    if max_len == -1:
        max_value_r[i] = seq[i]
        len_b_r[i] = 1
    else: len_b_r[i] = max_len+1
s=[]
for i in range(n):
    s.append(len_b[i]+len_b_r[i])
print(max(s)-1)