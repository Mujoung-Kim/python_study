# class 정의 -> 실행 : python 실행환경에 등록 (새로운 사용자정의 data_type)
class Person:
    pass

p = Person()                    # Person 객체 생성 -> Person 타입의 값을 표현
print(type(p))

# instance create
p = Person()

# instance에 attribute 추가
p.name = 'sancho'
p.age = 20
p.address = 'seoul'
print(f'name : {p.name}, age : {p.age}, address = {p.address}')

# instance에 attritute 변경
p.age = 50
p.address = 'busan'
# instance의 attribute 조회
print(f'name : {p.name}, age : {p.age}, address = {p.address}')

print(p.__dict__)               # class안의 attribute를 알려줌

# initializer attribute
class Person2:
    # initailizer -> 객체 생성 시 호출
    # self : 생성되는 객체
    def __init__(self, name, age, email=None) -> None:
        print("Person2, __init__() call", name, age, email)
        self.name = name        # self.name : attribute_name
        self.age = age          # self.age : attribute_age
        self.email = email
        self.address = None

# Person2('sancho', 20)
# 1. 메모리에 객체를 생성(영역을 할당한다.)
# 2. 객체를 생성하는 클래스에 정의된 initializer를 호출한다.
#    이때 생성시 전달한 값들이 initializer의 두 번째 parameter부터 전달된다.
#    첫 번째 parameter -> 1. 에서 생성된 객체가 전달된다.
p1 = Person2('sancho', 20)
p2 = Person2('anthony', 23, 'anthony@manchester.com')
p3 = Person2('martial', 28, 'martial@manchester.com')
print(p1.name, p2.name, p3.name)

class Person3:
    def __init__(self, name, age, email=None) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.address = None

    def print_attributes(self):
        info = f'name: {self.name}, age: {self.age}, email: {self.email}, address: {self.address}'
        print(info)

    def add_age(self, age):
        '''
        나이를 더해주는 method
        [parameter]
            self
            age : int = 더 할 나이
        [return]
            None
        '''
        self.age += age

p = Person3('sancho', 20, 'sancho@manchester.com')
p.print_attributes()
p.add_age(3)
p.print_attributes()

# 정보 은닉 -> attribute 검증로직을 넣고 싶을 때 주로 사용
# name은 두 글자이상, age는 양수만 가능, email은 @가 있어야 한다.
class Person4:
    def __init__(self, name, age, email=None) -> None:
        self.__name = name
        self.__age = age
        self.__email = email

    def set_name(self, name):           # name을 변경하는 method
        if  len(name) >= 2:
            self.__name = name          # 같은 class안에서는 __name으로 호출 가능
            print('변경되었습니다.')
        else:
            print('이름은 두 글자이상 입력하세요.')

    def get_name(self):              # name를 조회하는 method
        return self.__name
    
    # age 변경하는 method
    def set_age(self, age):
        if  age > 0:
            self.__age = age
            print('변경되었습니다.')
        else:
            print('나이는 양수만 입력할 수 있습니다.')
    
    # age 조회하는 method
    def get_age(self):
        return self.__age
    
    # email 변경하는 method
    def set_email(self, email):
        if  '@' in email:
            self.__email = email
            print('변경되었습니다.')
        else:
            print('email 형식이 잘못되었습니다. 다시 입력해주세요.')
    
    # email 조회하는 method
    def get_email(self):
        return self.__email

    def print_attribute(self):
        print(f'name: {self.__name}, age: {self.__age}, email: {self.__email}')

p = Person4('martial', 28, 'martial@manchester.com')
print('=' * 68)
p.print_attribute()
print('=' * 68)
p.set_name('anthony')
p.set_age(-10)
p.set_email('anthony@manchester.com')
p.print_attribute()
print(p.get_name(), p.get_age(), p.get_email())

# decorator를 이용한 setter/getter 구현
class Person5:
    def __init__(self, name) -> None:
        self.__name = name

    # getter : method_name을 attribute_name으로 정한다.
    @property                   # decorator
    def name(self):
        print('getter')
        return self.__name

    # setter : method_name을 attribute_name으로 정한다.
    # @getter_name.setter -> setter decorator
    @name.setter
    def name(self, name):
        print('setter', name)
        self.__name = name

p = Person5('sancho')           # @property -> name() method call
print(p.name)
p.name = 'anthony martial'      # @name.setter -> name() method call

# 상속
# Person, Student, Teacher
# Student, Teacher가 가지는 공통 attribute, method는 Person에 구현
# Student, Teacher는 Person을 상속해서 구현
class Person6:
    def go(self):
        print('학교에 간다.')
    
    def eat(self):
        print('점심을 먹는다.')

class Student(Person6):
    def study(self):
        print('수업을 듣는다.')

class UniversityStudent(Student):
    def drink(self):
        print('술을 마신다.')

class Teacher(Person6):
    def teach(self):
        print('수업을 가르킨다.')

s = Student()
t = Teacher()
us = UniversityStudent()
s.go()
s.eat()
s.study()
t.go()
t.eat()
t.teach()
us.go()
us.study()
us.drink()

# method overriding
class Student2(Person6):
    def go(self):
        print('스쿨버스를 타고 학교에 간다.')

s = Student2()
s.go()

# 상속과 attribute
class Person7:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}이 점심을 먹습니다.')

    def get_attribute(self):
        return f'{self.name}, {self.age}'

# Student attribute : name, age(Person), grade(추가 attribute가 있을 경우 initalizer를 재정의)
class Student(Person7):
    def __init__(self, name, age, grade):
        # SuperClass의 __init__()을 호출
        super().__init__(name, age)
        self.grade = grade

    def get_attribute(self):
        # SuperClass의 method()를 호출
        info = super().get_attribute()

        return f'{info}, {self.grade}'

s = Student('anthony', 23, 3)
info = s.get_attribute()
print(info)

# 연산자 class -> SuperClass는 어떻게 구현할 지 틀을 만드는 역할
class Operator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcuate(self):
        # attribute num1, num2를 이용해 계산
        pass

# 덧셈
class Plus(Operator):

    def calcuate(self):
        return self.num1 + self.num2

# 뺄셈
class Minus(Operator):

    def calcuate(self):
        return self.num1 - self.num2

plus = Plus(10, 20)
print(plus.calcuate())
minus = Minus(10, 20)
print(minus.calcuate())