import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# 열었던 파일에 대해 close 할 필요 없이, with 문을 자동으로 탈출

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
