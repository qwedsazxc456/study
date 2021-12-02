# 순차탐색
# 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 하나씩

# 이진탐색
# 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 탐색
# 시작점, 끝점, 중간점을 이용하여 탐색 범위 설정

# 이진탐색 재귀
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# index 찾아준다

# 이진탐색 반복

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end = mid-1
        else:
            start=mid+1
    return None

# 파이썬 이진 탐색 라이브러리

# bisect_left(a,x) - a에 x를 삽입할 왼쪽 인덱스
# bisect_right(a,x) - a에 x를 삽입할 오른쪽 인덱스

from bisect import bisect_left, bisect_right

a=[1,2,4,4,5]
x=4

print(bisect_left(a,x)) #2
print(bisect_right(a,x)) #4

# 데이터 개수 right-left


# 파라메트릭 서치(Parametric Search)
# 최적화 문제를 결정 문제로 바꾸어 해결하는 기법

# 1920

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
