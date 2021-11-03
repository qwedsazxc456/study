# class 선언, object는 python3에서 자동 상속

# class         SoccerPlayer   (    object    ) :
# class 예약어   class 이름     상속받는 객채명



# 변수와 class명 함수명은 짓는 방식이 존재 
# snake_case : 띄어쓰기 부분에 "_"를 추가 / 뱀 처럼 늘여쓰기 / 파이썬 함수 변수명에 사용
# CamelCase : 띄어쓰기 부분에 대문자 / 낙타의 등 모양 / 파이썬 Class명에 사용



# Attribute 추가는 __init__ , self와 함께
# __init__은 객체 초가화 예약 함수

class SoccerPlayer(object):
    def __init__(self, name : str , position : str , back_number : int):
        self.name = name
        self.pisition = position
        self.back_number = back_number
   
abc = SoccerPlayer('son', 'FW', 7)
park = SoccerPlayer('park', 'WF', 13)

print(abc is park) # False 
print(abc) # 메모리주소가 나온다


   
# __는 특수한 예약 함수나 변수 그리고 함수명 변경(맨글링)으로 사용
# 예) __main__ , __add__, __str__, __eq__

class SoccerPlayer(object):
    
    def __init__(self, name : str , position : str , back_number : int):
        self.name = name
        self.position = position
        self.back_number = back_number
        
    def __str__(self):
        return 'Hello, My name is %s. My back number is %d' % \
            (self.name , self.back_number)    

park = SoccerPlayer('park', 'WF', 13) 
print(park)


class SoccerPlayer(object):
    
    def __init__(self, name : str , position : str , back_number : int):
        self.name = name
        self.position = position
        self.back_number = back_number
        
    def __str__(self):
        return 'Hello, My name is %s. My back number is %d' % \
            (self.name , self.back_number)  
            
    def __add__(self, other):
        return self.name + other.name
    
abc = SoccerPlayer('son', 'FW', 7)
park = SoccerPlayer('park', 'WF', 13)

print(abc+park) # 이름끼리 더해져서 sonpark가 나온다



# method 구현하기
# method(Action) 추가는 기존 함수와 같이나, 반드시 self를 추가해야만 class 함수로 인정됨
# self는 생성된 instance 

class SoccerPlayer(object):
    def __init__(self, name : str , position : str , back_number : int):
        self.name = name
        self.position = position
        self.back_number = back_number
        
    def change_back_number(self, new_number):
        print('선수의 등번호를 변경합니다: From %d to %d' % \
            (self.back_number, new_number))
        self.back_number = new_number
        
    def __str__(self):
        return 'Hello, My name is %s. My back number is %d' % \
            (self.name , self.back_number) 

choi = SoccerPlayer('jinhyun','mf',10)
print(choi)       
        
choi.change_back_number(7)
print(choi) # back number가 7로 바껴서 나온다

choi.back_number = 20 # 바꿀수는 있지만 권장하지 않음 / 함수사용 하지 않고 바꿀 수 있음
print(choi)       



# 상속(Inheritance)
# 부모클래스로 부터 속성과 Method를 물려받은 자식 클래스를 생성 하는 것

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return '저의 이름은 {0} 입니다. 나이는 {1} 입니다' .format(
            self.name, self.age
        )

class Korean(Person):
    pass

first_korean = Korean('sungchul',35)
print(first_korean)


class Person: # (object) 적지 않아도 알아서 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def about_me(self): # Method 선언
        print('저의 이름은', self.name,'이구요, 제 나이는', str(self.age),'살 입니다.')
        
    def __str__(self):
        return '저의 이름은', self.name,'이구요, 제 나이는', str(self.age),'살 입니다.'
    
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender) # 부모객체 사용
        self.salary = salary
        self.hire_date = hire_date # 속성값 추가
        
    def do_work(self): # 새로운 Method 추가
        print('열심히 일을 합니다.')
        
    def about_me(self): # 부모 클래스 함수 재정의
        super().about_me() # 부모 클래스 함수 사용
        print('제 급여는', self.salary,'원 이구요, 제 입사일은',self.hire_date,'입니다.')

# super() 는 부모 클래스 가져온다

myPerson = Person('john',34,'male')
myPerson.about_me()

myEmployee = Employee('Daeho', 34, 'Male', 300000, '2012/03/01')
myEmployee.about_me() # 부모 클래스의 about_me와 자신의 about_me 둘다 나온다



# 다형성(Polymorphism)
# 같은 이름 메소드의 내부 로직을 다르게 작성
# Dynamic Typing 특성으로 인해 파이썬에서는 같은 부모클래스의 상속에서 주로 발생함
# 중요한 OOP의 개념 그러나 너무 깊이 알 필요 X 

class Animal:
    def __init__(self, name):
       self.name = name
       
    def talk(self):
        raise NotImplementedError('subclass must inplement abstract method')
    
class Cat(Animal):
    def talk(self):
        return 'Meow!'
    
class Dog(Animal):
    def talk(self):
        return 'woof! woof!'
    
animals = [Cat('Missy'),
           Cat('mr.Mistoffelees'),
           Dog('Lassie')]

for animal in animals:
    print(animal.name + ':' + animal.talk())
    

 
# 가시성(Bisibility)

# 객체의 정보를 볼 수 있는 레벨을 조절하는 것

# 누구나 객체 안에 모든 변수를 볼 필요가 없음
# 1) 객체를 사용하는 사용자가 임의로 정보 수정
# 2) 필요 없는 정보에는 접근 할 필요가 없음
# 3) 만약 제품으로 판매한다면? 소스의 보호

# Encapsulation
# 캡슐화 또는 정보 은닉(Information Hiding)
# Class를 설꼐할 때, 클래스  간 간섭/정보공유의 최소화
# 심판 클래스가 축구선수 클래스 가족 정보를 알아야 하나?
# 캡슐을 던지듯, 인터페이스만 알아서 써야함

# Visibility Example1
# Priduct 객체를 Inventory 객체에 추가
# Inventory에는 오직 Product 객체만 들어감
# Inventory에 Product가 몇 개인지 확인이 필요
# Inventory에 Product itens는 직접 접근이 불가

class Product:
    pass

class Inventory:
    def __init__(self):
        self.items = []
        self.test = 'abc'
        
    def add_new_item(self, product):
        if type(product) == Product:
            self.items.append(product)
            print('new item added')
        else:
            raise ValueError('Invalid item')
        
    def get_number_of_items(self):
        return len(self.items)

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product()) # 원하는 방법
my_inventory.items.append('abc')
my_inventory.items.append('abc')
my_inventory.items.append('abc')
my_inventory.items.append('abc') # 하지만 마음대로 추가 가능

class Product:
    pass

class Inventory:
    def __init__(self):
        self.__items = []
        self.test = 'abc'
        
    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            raise ValueError('Invalid item')
        
    def get_number_of_items(self):
        return len(self.__items)
    
my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product()) # 가능 
# __를 붙이면 my_inventory.__items 할 수 없게 된다. 
# 다른 객체 추가 불가 


# Visibility Example2 (접근이 필요할 때)
# Priduct 객체를 Inventory 객체에 추가
# Inventory에는 오직 Product 객체만 들어감
# Inventory에 Product가 몇 개인지 확인이 필요
# Inventory에 Product itens 접근 허용

class Inventory:
    def __init__(self):
        self.__items = []
        
    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            raise ValueError('Invalid item')
        
    @property #property decorator 숨겨진 변수를 반환하게 해줌
    def items(self):
        return self.__items    

my_inventory = Inventory()  
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
# my_inventory.__items 안됨 / 원래 하던대로 my_inventory.items
my_inventory.items.append('a') # 가능 



# First-class object
# 일등함수 또는 일급 객체
# 변수나 데이터 구조에 할당이 가능한 객체
# 파라미터로 전달이 가능 + 리턴 값으로 사용
# 파이썬의 함수는 일급함수 - 파라미터나 리턴값으로 사용가능

def square(x):
    return x*x

f = square # 함수를 변수로 사용

print(f(5))

def cube(x):
    return x*x*x

def formula(method, argument_list):
    return [method(value) for value in argument_list]



# 함수 내에 또 다른 함수가 존재 (Inner function)
def print_msg(msg):
    def printer():
        print(msg)
    printer()
    
print_msg('hello, Python')

def print_msg2(msg):
    print(msg)
    
print_msg2('hello, Python') 
### 어떤 차이가 있는걸까...?

def print_msg(msg):
    def printer():
        print(msg)
    return printer

another = print_msg('hello, Python')
another()
### printer() 와 return printer의 차이는 ...? / another도 함수...?


# closure : inner function을 return값으로 반환

# closure example
def tag_func(tag, text):
    text = text
    tag = tag
    
    def inner_func():
        return '<{0}>{1}<{0}>'.format(tag, text)
    
    return inner_func

h1_func = tag_func('title','This is Python Class')
P_func = tag_func('p', 'Data Academy')

print(h1_func)
print(P_func)


# decorator function 
# 복잡한 클로져 함수를 간단하게

def star(func):
    def inner(*args, **kwargs): 
        print('*'*30)
        func(*args, **kwargs)
        print('*'*30)
    return inner
### *args 여러개 인자 튜플형태, **kwargs 여러개 인자 딕셔너리 형태

@star
def printer(msg):
    print(msg)
    
printer('Hello')


def star(func):
    def inner(*args, **kwargs): 
        print(args[1]*30)
        func(*args, **kwargs)
        print(args[1]*30)
    return inner

@star
def printer(msg, mark):
    print(msg)
    
printer('Hello', 'T')
printer('Hello', '*')


def star(func):
    def inner(*args, **kwargs): 
        print('*'*30)
        func(*args, **kwargs)
        print('*'*30)
    return inner

def percent(func):
    def inner(*args, **kwargs): 
        print('%'*30)
        func(*args, **kwargs)
        print('%'*30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer('Hello')
### decorator function과 @ 알아보기

def generate_power(exponent):
    def wrapper(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return wrapper

@generate_power(2)
def raise_two(n):
    return n**2

print(raise_two(7))
### exponent에 2가 들어가고 raise_two(7)의 값 49가 f에 들어가고 2**49가 나온다
