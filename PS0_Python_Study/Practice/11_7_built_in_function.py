# 따로 import 필요 없이 바로 사용 가능한 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시 
# print(dir())
# import random # 외장 함수
# print(dir()) # random 이 추가됨
# import pickle
# print(dir()) # pickle 이 추가됨

# print(dir(random)) # random 모듈 안에서 쓸 수 있는 것들 나옴
# lst = [1, 2, 3]
# print(dir(lst))

name = "Jim"
print(dir(name))

# 구글에서 파이썬 내장함수에서 쓸 수 있는 것 설명 검색 가능