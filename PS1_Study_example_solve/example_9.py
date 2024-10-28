# 문제_ 주어진 코드를 활용해 주차 차량 등록 관리 프로그램을 작성하세요.

# 조건
# 1. 총 주차 가능 대수인 capacity는 객체를 생성할 때 전달받아 인스턴스 변수로 정의한다.
# 2. 현재 등록된 차량 수를 관리하는 count는 객체를 생성할 때 0으로 정의한다.
# 3. 객체를 생성할 때 등록 가능한 대수를 출력한다.
# 4. 차를 신규 등록하는 register() 메서드를 정의한다.
# 5. 신규 등록 시 등록 현황을 출력한다.
# 6. 총 주차 가능 대수를 초과하는 경우 "더 이상 등록할 수 없습니다." 라는 메시지를 출력한다.

# class ParkingManager:
#     # 주차 정보 초기화: 총 주차 가능 대수
#     def __init__(self, capacity):
#         pass

#     # 신규 차량 등록
#     def register(self):
#         pass

# # 테스트 코드
# manager = ParkingManager(5)
# for i in range(6):
#     manager.register()

# 실행결과
# 총 5대를 등록할 수 있습니다.
# 차량 신규 등록 (1/5)
# 차량 신규 등록 (2/5)
# 차량 신규 등록 (3/5)
# 차량 신규 등록 (4/5)
# 차량 신규 등록 (5/5)
# 더 이상 등록할 수 없습니다.

class ParkingManager:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        print(f"총 {self.capacity}대를 등록할 수 있습니다.")
    def register(self):
        if self.count < self.capacity:
            self.count += 1
            print(f"차량 신규 등록 ({self.count}/{self.capacity})")
        else:
            print("더 이상 등록할 수 없습니다.")

# 테스트 코드
manager = ParkingManager(5)
for i in range(6):
    manager.register()