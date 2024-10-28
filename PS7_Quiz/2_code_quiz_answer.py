from random import *

words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : ???")
letters = "" # 사용자로부터 지금까지 입력받은 모든 알파벳

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ") 
            succeed = False
    print()

    if succeed:
        print("Success")
        break

    letter = input("Input letter > ")
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")
