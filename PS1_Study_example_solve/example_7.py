# 문제) 미세먼지 수치를 입력받아 대기질 상태를 출력하는 함수를 만들어 보세요.

# 조건
# 1. get_air_quality 라는 이름으로 함수를 만든다.
# 2. 이 함수는 전달값으로 미세먼지 수치를 입력받는다.
# 3. 이 함수는 대기질 상태를 반환한다.
# 4. 미세먼지 수치에 따른 대기질 상태는 다음과 같다.
#     ・좋음 : 0~30
#     ・보통 : 31~80
#     ・나쁨 : 81~150
#     ・매우 나쁨 : 151 이상
# 5. 함수에 전달되는 전달값은 항상 0 이상의 값이라고 가정한다.

# # 테스트 코드
# print(get_air_quality(15)) # 좋음
# print(get_air_quality(85)) # 나쁨

# 실행결과
# 좋음
# 나쁨

def get_air_quality(fine_dust):
    if 0 <= fine_dust <= 30:
        return "좋음"
    elif fine_dust <= 80:
        return "보통"
    elif fine_dust <= 150:
        return "나쁨"
    else:
        return "매우 나쁨"

# 테스트 코드
print(get_air_quality(15))
print(get_air_quality(85))

     