# 지역변수 : 함수 내에서만 사용. 함수 호출될 때 만들어졌다가, 함수 끝나면 사라짐
# 전역변수 : 모든 프로그램 내에서 사용 가능

gun = 10

# 지역변수여서 오류남
# def checkpoint(soliders): # 경계근무
#     gun = gun - soliders 
#     print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint(soliders): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soliders 
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

