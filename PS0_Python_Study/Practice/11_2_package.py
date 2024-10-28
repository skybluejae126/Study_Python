# 패키지 : 모듈들을 모아 놓은 집합

# import travel_11_2.thailand # 맨 뒤에 'thailand'는 모듈이나 패키지만 가능. 클래스나 함수는 import 불가
# trip_to=travel_11_2.thailand.ThailandPackage()
# trip_to.detail()

# from travel_11_2.thailand import ThailandPackage # from import 구문에서는 가능
# trip_to = ThailandPackage()
# trip_to.detail()

from travel_11_2 import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()