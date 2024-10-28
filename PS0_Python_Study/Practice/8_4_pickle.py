# 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb") # rb 읽기
profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

# 가지고 있는 데이터를, 피클을 이용해서 파일에 저장하고, 파일에 있는 내용을 불러와서 변수에 저장하여 사용 가능