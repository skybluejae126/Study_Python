# 가변 인자 : 적어야 하는 변수의 개수가 달라질 수 도 있을 떄 사용

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t"\
#           .format(name, age), end=" ") # end=" " 빈칸으로 하면 아래 문장을 이어서 출력
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t"\
          .format(name, age), end=" ") # end=" " 빈칸으로 하면 아래 문장을 이어서 출력
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

