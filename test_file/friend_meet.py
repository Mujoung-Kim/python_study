#TODO exception logic
# 친구를 만난다
# 1. 약속시간 1시간 전에 집에서 나온다. >> o
# 2. 버스 정류장에 도착한다. >> o
# 3. 200번 버스를 타고 명동 정류장에 내린다. -> 버스가 오지 않을 경우 > 처리 : 택시를 타고 간다.
# 4. 약속장소인 cafe를 찾아간다. -> 약속장소가 쉬는 날이다 > 처리 : 친구에게 전화해서 장소를 변경한다.
# 5. 친구를 만난다.
class NotStationBus(Exception):
	pass

class NotOpenCafe(Exception):
	pass

def friend_meetting():
    """
    친구를 만나는 과정을 출력하는 함수
    [parameter]
        time : int - 약속시간
    [return]
        None
    """
    def __init__(self, time):
        self.time = time

# function 이전 로직
in_num = input('약속시간 : ')

try :
    meet_time = int(in_num)
    start_time = meet_time - 1
    
    if meet_time >= 0 and meet_time < 25:
        if start_time == -1:
            start_time = 23
        print(f'{start_time}시에 집에서 출발하셔야 됩니다.')
        print('버스 정류장에 도착했습니다.')
    else:
        raise ValueError
except ValueError:
    print('약속시간을 잘못 입력하셨습니다. 0 ~ 24 사이의 시간 값을 입력하세요.')
except :
	pass

# result_value print area
if __name__ == '__main__':
    print(__name__)
    print(start_time)