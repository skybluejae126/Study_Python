# print("Python", "Java", sep="")
print("Python", "Java", sep=",")
# print("Python", "Java", "JavaScript" sep=" vs ")

print("Python", "Java", sep=",", end="?") # 기본적으로는 end 부분이 줄바꿈으로 되어있었음.
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr) # 에러처리 가능

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4)\
          , sep=":") # 총 8개의 공간 중 왼쪽 정렬, 4칸 공간 중 오른쪽 정렬
    
# 은행 대기순번표
# 001, 002, 003 ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 3크기 만큼의 공간 확보 후, 값이 없으면 0으로 채우기

# 표준 입력
answer = input("아무 값이나 입력하세요 : ") # 입력을 통해 받으면 항상 문자열 형태로 받음
print(type(answer)) 
print("입력하신 값은 " + answer + "입니다.")