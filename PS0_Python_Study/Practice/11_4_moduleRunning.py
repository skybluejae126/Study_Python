# 실제 패키지나 모듈을 만들 때에는, 모듈이 잘 동작하는지 테스트 해봐야 함

from travel_11_2 import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# "Thailand 외부에서 모듈 호출" 이라는 구문이 출력됨
# 모듈 내에서 실행하는지, 외부에서 실행하는지 구분 가능