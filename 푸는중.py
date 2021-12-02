# n = int(input())
# list_1=[]
# list_2=[]
# for i in range(n):
#     s,e = map(int, input().split())
#     list_1.append(s)
#     list_2.append(e)
# c=0
# m=min(list_2)
# while True:
#     m_2=max(list_2)
#     for j in range(n):
#         if list_1[j] == list_2[j]:
#             c += 1
#         else:
#             for i in range(n):
#                 if list_1[i]>=m:
#                     if list_2[i]<m_2:
#                         m_2=list_2[i]
#                         m=list_1[i]
#     if m_2==max(list_2):
#         break
#     c += 1

# print(c+1)

n = int(input())
list_1 = list(map(int, input().split()))
m = int(input())
list_2 = list(map(int, input().split()))
list_1.sort()

def bi(list_1,x,s,e):
    while s <= e:
        m = (s+e)//2
        if list_1[m]==x:
            return 1
        elif list_1[m]<x:
            s = m+1
        else:
            e = m-1
    return 0


for i in list_2:
    print(bi(list_1,i,0,n-1))       