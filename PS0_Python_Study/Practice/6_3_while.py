# while
customer = "토르"
index = 5
while index >= 1:
    
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")
    
# 무한루프
# customer = "아이언맨"
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")