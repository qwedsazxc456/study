# 순차 탐색
def search_list(a,x):
    return a.index(x) if x in a else -1

# 선택정렬1
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx


def sel_sort(a):   
    result=[]
    while a:
        min_idx=find_min_idx(a)
        value=a.pop(min_idx)
        result.append(value)
    return result

# 선택정렬2

def sel_sort(a):
    n=len(a)
    for i in range(n):
        index=a.index(min(a[i:n]))
        a[i],a[index]=a[index],a[i]
    return a
        
# 삽입정렬

    