a = [1,2,3]
b = [1,2,3]

a.remove(2) # remove 안에 값
c=b.pop(2) # pop 안에 index / b 에서는 값 제거 값을 c에 저장

print(a,b,c)

a.clear() # 모두 삭제
print(a)

s=set()
s.add(1)
s.add(2) # list의 append 처럼 원소 한개씩만
print(s)

s.discard(2) # 삭제
print(s)

# clear / x in s 리스트 처럼 사용 가능

# 최대공약수

def gcd(a,b):
    i=min(a,b)
    while True:
        if a%i ==0 and b%i == 0:
            return i
        i -= 1

# while True 도 return 있으면 그만???

# 최대공약수 유클리드사용

def gcd(a,b):
    return a if b == 0 else gcd(b, a%b) 
    
# 하노이

# 움직인 횟수
def hanoi_1(n):
    return 1 if n ==1 else hanoi_1(n-1)*2+1

# 움직인 과정
def hanoi_2(n,a,b,c):
    if n ==1:
        print(a,c)
    else:
        hanoi_2(n-1,a,c,b)
        print(a,c)
        hanoi_2(n-1,b,a,c)


        

    

    
        
    

   
