#branch 만들었다가 merge 했지롱~
#왜 안되는거지?
import json
import os

from quiz import DEFAULT_QUIZZES, Quiz, get_answer_input, get_text_input


STATE_FILE = "state.json"


class QuizGame:
    def __init__(self):
        self.quizzes = self.load_quizzes()
        self.score = 0
        self.high_score = self.load_high_score()

    def show_menu(self):      #메뉴 기능을 이렇게 만들어둔다!
        print("\n===== 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("====================")


    def run(self):
        while True:
            self.show_menu()   #위에 만들어둔 메뉴를 실행한다!!
            choice = input("번호를 선택하세요: ").strip()  # .strip() => input의 공백 삭제

            if choice == "":    #밑에 int(choice) 있으므로 필요X 
                print("⚠️  입력값이 없습니다. 번호를 입력해주세요.")
                continue

            try:
                number = int(choice)        # ← 숫자 변환 시도  문자 & 빈칸 모두 잡아줌!! only int만 받기 때문에
            except ValueError:
                print("⚠️  숫자를 입력해주세요.")
                continue                    # ← 다시 while 처음으로

            if number < 1 or number > 5:      #밑의 else 와 같은 의미
                print("⚠️  1~5 사이의 숫자를 입력해주세요.")
                continue

            if choice == "1":
                print("[퀴즈 풀기]")
                self.play()
            elif choice == "2":
                print("[퀴즈 추가]")
                self.add_quiz()
            elif choice == "3":
                print("[퀴즈 목록]")
                self.show_quizzes()
            elif choice == "4":
                print("[점수 확인]")
                self.show_high_score()
            elif choice == "5":
                print("게임을 종료합니다. 안녕히 가세요!")
                break
            else:
                print("⚠️  잘못된 입력입니다. 1~5 중에서 선택해주세요.")


    def load_quizzes(self):
        if not os.path.exists(STATE_FILE):
            return list(DEFAULT_QUIZZES)

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
            return list(DEFAULT_QUIZZES)

        quizzes = []
        for item in data.get("quizzes", []):
            quiz = Quiz(item["question"], item["choices"], item["answer"])
            quizzes.append(quiz)

        return quizzes

    def save_quizzes(self):
        try:
            # 현재 state.json 읽기 (high_score 보존)
            if os.path.exists(STATE_FILE):
                with open(STATE_FILE, "r", encoding="utf-8") as file:
                    entire_data = json.load(file)    #여기서 high_score가 저장되는 것!
            else:
                entire_data = {"high_score": 0}   #파일 없다면 기본값 설정

            # quizzes 데이터 생성
            quiz_data = []
            for quiz in self.quizzes:
                item = {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                quiz_data.append(item)

            # quizzes 업데이트
            entire_data["quizzes"] = quiz_data

            # 전체 저장
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                json.dump(entire_data, file, ensure_ascii=False, indent=4)
        except (IOError, json.JSONDecodeError) as e:   #파일 손상 등 문제 
            print(f"⚠️  파일 저장 중 오류가 발생했습니다: {e}")

    def load_high_score(self):
        if not os.path.exists(STATE_FILE):
            return 0

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("⚠️  데이터 파일이 손상되었습니다. 최고 점수를 0으로 초기화합니다.")
            return 0

        return data.get("high_score", 0)   #high_score 값을 가져옴! / 0: key(high_score가 망가졌을 때 value를 꺼내오는 것)

    def  save_high_score(self):
        try:
            # 현재 state.json 읽기 (quizzes 보존)
            if os.path.exists(STATE_FILE):
                with open(STATE_FILE, "r", encoding="utf-8") as file:
                    entire_data = json.load(file)    
            else:
                entire_data = {"quizzes": []}  #파일 못 받았을 때 새로운 dict를 만든다

            # high_score 업데이트
            entire_data["high_score"] = self.high_score

            # 전체 저장 (결국에는 high_score만 업데이트 되는 것)
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                json.dump(entire_data, file, ensure_ascii=False, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            #error type(except class) 사전 정의 
                #IOEror: 파일/권한/용량 X  ex) json : r-- => high_score 입력 X
                #json.JSONDecodeError: json형식 안 맞을 때
            print(f"⚠️  파일 저장 중 오류가 발생했습니다: {e}")  #except 에서 잡힌 오류를 출력

    
    def play(self):
        if not self.quizzes:
            print("⚠️  퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        self.score = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}/{len(self.quizzes)}]")
            quiz.display()    # for문에서 self.quizzes를 반복해서 출력받을 변수
            answer = self.get_answer()

            if quiz.is_correct(answer):   #quiz.py 에 있는 함수
                print("✅ 정답입니다!")
                self.score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")
 
        self.show_result()   #for문 끝나면 저장

    def get_answer(self):
        while True:
            choice = input("정답을 입력하세요 (1~4): ").strip()

            if choice == "":
                print("⚠️  입력값이 없습니다.")
                continue

            try:
                number = int(choice)
            except ValueError:
                print("⚠️  숫자를 입력해주세요.")
                continue

            if number < 1 or number > 4:
                print("⚠️  1~4 사이의 숫자를 입력해주세요.")
                continue

            return number   #get_answer(self)의 값

    def add_quiz(self):
        question = get_text_input("문제를 입력하세요: ")
        choice1 = get_text_input("1번 선택지를 입력하세요: ")
        choice2 = get_text_input("2번 선택지를 입력하세요: ")
        choice3 = get_text_input("3번 선택지를 입력하세요: ")
        choice4 = get_text_input("4번 선택지를 입력하세요: ")
        answer = get_answer_input("정답 번호를 입력하세요 (1~4): ")

        choices = [
            f"1. {choice1}",
            f"2. {choice2}",
            f"3. {choice3}",
            f"4. {choice4}",
        ]

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_quizzes()

        print("퀴즈가 저장되었습니다.")

    def show_quizzes(self):
        if not self.quizzes:
            print("⚠️  저장된 퀴즈가 없습니다.")
            return

        print("\n===== 퀴즈 목록 =====")
        for index, quiz in enumerate(self.quizzes, start=1):   
            print(f"{index}. {quiz.question}")    #quiz 중에서 qustion 부분만 

    def show_high_score(self):
        total = len(self.quizzes)

        if total == 0:
            print("⚠️  등록된 퀴즈가 없습니다.")
            return

        if self.high_score > total:
            self.high_score = total

        print(f"최고 점수: {self.high_score}/{total}")

    def show_result(self):
        total = len(self.quizzes)

        if self.high_score > total:   #quiz_add, 초기설정값 오류로 인해 high_score가 퀴즈 수 보다 커졌을 때 대비
            self.high_score = total

        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        print(f"\n========== 결과 ==========")
        print(f"총 {total}문제 중 {self.score}문제 정답!")
        print(f"점수: {self.score}/{total}")
        print(f"최고 점수: {self.high_score}/{total}")
        print("==========================")


if __name__ == "__main__":
    game = QuizGame()
    game.run()
