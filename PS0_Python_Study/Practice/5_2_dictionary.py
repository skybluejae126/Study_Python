# 해당 키만 열 수 있음
# 키는 중복이 안됨

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100]) # 대괄호

print(cabinet.get(3)) # 소괄호
# print(cabinet[5]) # 해당 키가 없으면 오류가 나옴
print(cabinet.get(5)) # 해당 키가 없으면 non 출력 (4_3의 index, find와 비슷)
print(cabinet.get(5, "사용가능")) # 뒤 string 출력

print(3 in cabinet) # True
print(5 in cabinet) # False

# 정수가 아닌 string 도 키 지정 가능
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 업데이트
cabinet["C-20"] = "조세호" # 추가
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)



