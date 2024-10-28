# 파일을 열고, 쓰고, 닫기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # "a"를 쓰면 append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # 줄 바꿈 적어줘야 함
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # "r" 은 읽기
# print(score_file.read())
# score_file.close()                  

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 파일이 몇 줄인지 모를 때, 반복문으로 불러오기 가능
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 리스트에 넣어서 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()