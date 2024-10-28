python = "Python is Amazing"
print(python.lower()) # 전부 소문자
print(python.upper()) # 전부 대문자
print(python[0].isupper()) # 대소분자 확인
print(len(python)) # 길이
print(python.replace("Python", "Java")) # 교체

index = python.index("n") # "n" 위치 확인
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 값이 없을 경우 -1 반환
# print(python.index("Java")) # index 에서는 오류로 반환

# n이 몇개 있는지 세기
print(python.count("n"))