import os   #파일 있는지 확인 (os.path.exists 사용하기 위해)
import json     #json(파일 내용을 파이썬으로 바꾸는 도구) 확인



class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
        
    def display(self):
        print(f"\n{self.question}")    #\n 으로 시작하니까 한 줄 띄고 시작
        for choice in self.choices:  
            print(choice)            #문제 객체에서 선택지들을 반복적으로 출력한다는 것임

    def is_correct(self, user_answer):
        return self.answer == user_answer    #usesr가 고른 정답이 문제 객체 정답과 같은가 확인


# Quiz 인스턴스 (객체) ...  jason이 안 읽히면 얘를 return해라 

DEFAULT_QUIZZES = [      #index(순서), 수정 자유로운 list로 객체 관리       #dic도 관리 가능 BUT 순서대로 quiz를 내보내기에는 더 적합 & value값을 list로 다시 변환해야 할 수도
    Quiz(          
        question="파이썬에서 주석을 나타내는 기호는?",          #quiz 안의 내용들은 바꾸지 않을 것이기에 튜플로 저장
        choices=["1. //", "2. ##", "3. #", "4. **"],          #index 있는 튜플, 리스트 모두 가능
        answer=3
    ),
    Quiz(
        question="파이썬에서 리스트를 만들 때 사용하는 괄호는?",
        choices=("1. ()", "2. []", "3. {}", "4. <>"),     # tuple 도 가능하니까~
        answer=2
    ),
    Quiz(
        question="파이썬에서 함수를 정의할 때 사용하는 키워드는?",
        choices=["1. func", "2. function", "3. define", "4. def"],
        answer=4
    ),
    Quiz(
        question="파이썬에서 무한 루프를 만들 때 사용하는 코드는?",
        choices=["1. while True", "2. for True", "3. loop True", "4. repeat True"],
        answer=1
    ),
    Quiz(
        question="파이썬에서 아무것도 없음을 나타내는 값은?",
        choices=["1. null", "2. undefined", "3. None", "4. empty"],
        answer=3
    ),
]





    

#퀴즈 생성 및 저장 

def get_text_input(message):
    while True:
        value = input(message).strip()   #입력값 양쪽 공백 제거 (사용자 실수 방지) main.py의 choice처럼 아예 안되게 하려는 것이 아님! 

        if value == "":
            print("⚠️  입력값이 없습니다.")
            continue

        return value   #return = 함수 종료
    

def get_answer_input(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("⚠️  입력값이 없습니다.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("⚠️  숫자를 입력해주세요.")
            continue

        if number < 1 or number > 4:
            print("⚠️  1~4 사이의 숫자를 입력해주세요.")
            continue

        return number
    
    #while True:
        #value = input("정답 번호 입력: ").strip()

        #if not value.isdigit():        #isdigit() - 문자열이 숫자(0~9)로만 이루어져 있는지 확인 (음수, 소수는 False)
            #print("숫자를 입력하세요.")
            #continue

        #num = int(value)

        #if 1 <= num <= 4:
            #return num
        #else:
        #    print("1~4 사이 숫자 입력")






