# 예외 처리 : 어떤 에러가 발생했을 때 그에 대해 처리해주는 것
# 예) 계산기에 숫자를 입력받아야 하는데, 문자를 입력 받았을 때 / 접속이 잘 안 될 때

# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err) # 발생하는 에러 문장을 그대로 출력

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1])) # List out of range 에러가 뜸.
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err) # 발생하는 에러 문장을 그대로 출력
except Exception as err: # 위 두 에러 제외 나머지 모든 에러 처리 가능
    print("알 수 없는 에러가 발생하였습니다.") 
    print(err)