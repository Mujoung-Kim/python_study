def a():
	print('start a')
	b()						# b() function call
	print('end a')

def b():
	print('start b')
	c()						# c() function call
	print('end b')

def c():
	print('start c')
	# print(100 / 0)			# error code
	print('end c')

if __name__ == '__main__':
	print('start main')
	a()
	print('end main')

# exception logic
# 친구를 만난다 -> test_file
# 1. 약속시간 1시간 전에 집에서 나온다.
# 2. 버스 정류장에 도착한다.
# 3. 200번 버스를 타고 명동 정류장에 내린다. -> 버스가 오지 않을 경우 > 처리 : 택시를 타고 간다.
# 4. 약속장소인 cafe를 찾아간다. -> 약속장소가 쉬는 날이다 > 처리 : 친구에게 전화해서 장소를 변경한다.
# 5. 친구를 만난다.

# try, except, finally
print('start')

txt = input()
try :
    num = int(txt)                      # ValueError
    result = 10 / num                   # ZeroDivisionError
    print('div result: ', result)
except ValueError:                      # ValueError가 발생하면 처리하는 코드
    # exception_handing code
    print('ValueError 발생한 것 처리')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except TypeError:
    print('TypeError')
except :
    print('공통 exception handing')
finally :                               # 실제 사용할 일은 많지 않다. -> try구문 안에서 무슨일이 발생해도 실행
    print('무적권 실행되는 코드')

print('input_value: ', txt)
print('end')

# exception_handing 구문
# 1. try - except (여러개)
# 2. try - except (여러개) - finally
# 3. try - finally -> function를 호출한 곳에서 처리할 때 사용되는 구문

# exception 발생
# (1 ~ 12)월을 받아서 저장하는 function
def set_month(month):
    """
    (1 ~ 12)월을 받아서 저장하는 함수
    [parameter]
        month: int - 저장할 월 1 ~ 12
    [return]
        None
    [exception]
        ValueError: 잘못된 월을 저장할 경우 발생
    """
    if month > 0 and month <= 12:
        print(f'{month}월을 저장장소에 저장합니다.')
        # return None : 정상 종료상태로 호출한 곳으로 돌아가라.
    else :
        # raise Exception_object : 비정상 종료상태로 호출한 곳으로 돌아가라.
        # Exception_object : 무슨 오류가 발생했는지를 표현
        raise ValueError('plase enter to 1 ~ 12')

try :
    set_month(10)
    set_month(1)
    set_month(100)
    print('month enter clear')
except :
    print('저장도중 오류발생')
print('end')

# exception 정의
class NotEnoughStockException(Exception):
    
    def __init__(self, stock_amount):
        self.stock_amount = stock_amount

    def __str__(self):
         return f'재고량이 부족합니다. 재고량 : {self.stock_amount}'

def order(order_amount):
    """
    주문 갯수를 받아서 주문을 처리하는 함수
    [parameter]
        order_amount: int - 주문갯수
    [return]
        None
    [exception]
        NotEnoughStockException: 주문량이 재고량보다 많으면 발생
    """
    # 1. 재고량 조회
    stock_amount = 10

    # if stock_amount < order_amount -> exception 발생
    if stock_amount < order_amount:
        raise NotEnoughStockException(stock_amount)

    # 2. stock_amount >= order_amount
    # 주문처리
    print('주문처리중')
    stock_amount -= order_amount
    print('주문완료. 남은 재고량 :', stock_amount)

try :
    order(5)
    order(100)
except NotEnoughStockException as e:
    # except Exception 타입 as e : e 변수에 발생한 Exception_object를 대입
    print('주문실패. 재고량 :', e.stock_amount)
    order(e.stock_amount)           # 재고 남은 것을 모두 주문