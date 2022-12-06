#TODO exception logic
# 친구를 만난다
# 1. 약속시간 1시간 전에 집에서 나온다. >> o
# 2. 버스 정류장에 도착한다. >> o
# 3. 200번 버스를 타고 명동 정류장에 내린다. -> 버스가 오지 않을 경우 > 처리 : 택시를 타고 간다. >> o
# 4. 약속장소인 cafe를 찾아간다. -> 약속장소가 쉬는 날이다 > 처리 : 친구에게 전화해서 장소를 변경한다. >> o
# 5. 친구를 만난다. >> o
# 6. 객체화?
class NotStationBusException(Exception):

    def __init__(self, station):
        self.station = station
        
    def __str__(self):
        return f'{self.station}으로 택시를 타고 출발합니다.'

class NotOpenLocationException(Exception):
	
    def __init__(self, location):
        self.location = location

    def __str__(self):
        return f'친구에게 전화해서 {self.location}에서 만나기로 합니다.'

# 객체화
class Meet():
    def __init__(self, time=0, station=None, location=None):
        self.time = time
        self.station = station
        self.location = location

    # 도착 station 설정
    def set_station(self, station):
        try :
            if isinstance(station, str):  
                self.station = station
            else :
                raise ValueError(f'{station}은 존재하지 않습니다.')
        except ValueError as e:
            print(e)

    # 약속장소 설정
    def set_location(self, location):
        try :
            if isinstance(location, str):
                self.location = location
            else :
                raise ValueError(f'{location}은 존재하지 않습니다.')
        except ValueError as e:
            print(e)

    # 출발시간 계산
    def meet_time(self) :
        meetting_time = self.time - 1

        try :
            if self.time >= 0 and self.time < 25:
                if meetting_time == -1:
                    meetting_time = 23
                print(f'{meetting_time}시에는 집에서 출발하셔야 됩니다.')
            else :
                raise ValueError(f'{self.time}은 0 ~ 24사이의 값을 넣으셔야 됩니다.')
        except ValueError as e:
            print(e)

    # 정류장 정보
    def get_station(self):
        return f'{self.station}정류장으로 가야합니다.'

    # 버스타고 정류장으로 이동
    def going_station(self):

        try : 
            if self.station != None:
                isbus = True
            else :
                isbus = False

            if isbus == True:
                print(f'{self.station}에 도착했습니다.')
            else :
                raise NotStationBusException(self.station)
        except NotStationBusException as e :
            print(e)

    # 약속장소 정보'
    def get_location(self):
        return f'약속장소는 {self.location}입니다.'

    # 약속장소
    def going_location(self):
        
        try :
            if self.location != None :
                isopen = True
            else : 
                isopen = False

            if isopen == True :
                print(f'{self.location}에 도착했습니다. 친구를 기다립니다.')
            else :
                raise NotOpenLocationException(self.location)
        except NotOpenLocationException as e :
            print(e)

def meet_friend(num, destination=None, location=None):
    """
    친구를 만나는 과정을 출력하는 함수
    [parameter]
        time : int - 약속시간
        destination : str - 목적 정류장
        location : str - 약속장소
    [return]
        None
    """
    isbus, isopen = False, False

    try :
        # 집
        if isinstance(num, int) :
            meet_time = num - 1
            if meet_time == 0 :
                meet_time = 23
            print(f'{meet_time}에는 출발하셔야 됩니다.')
        else :
            raise ValueError

        # 버스 정류장
        print('버스 정류장에 도착했습니다.')
        if destination != None :
            isbus = True
        else : 
            destination = input('정류장 : ')

        if isbus == True :
            print(f'{destination}로 200번 버스를 타고 출발합니다.')
        else : 
            print('200번 버스가 없습니다.')
            raise NotStationBusException(destination)

        # 약속장소
        if location != None :
            isopen = True
        else :
            print('약속장소가 문을 열지 않았습니다.')
            location = input('변경할 장소 : ')
            
        if isopen == True :
            print(f'{location}에 도착했습니다. 친구를 기다립니다.')
        else : 
            raise NotOpenLocationException(location)

    except ValueError : 
        print(f'{num}은 시간이 아닙니다. 약속시간은 0 ~ 24사이의 숫자를 입력하세요.')
    except NotStationBusException as e :
        print(e)
    except NotOpenLocationException as e :
        print(e)

# result_value print area
if __name__ == '__main__':
    print(__name__)
    # num = input('meet_time : ')
    # mf = Meet(int(num))
    # mf.meet_time()
    # station = input('set_station : ')
    # mf.set_station(station)
    # location = input('set_location : ')
    # mf.set_location(location)
    # mf.going_station()
    # mf.going_location()
    meet_friend(15, '명동')
    print('system end!')