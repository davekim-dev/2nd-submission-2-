#json 이란? - JavaScript Object Notation, 데이터를 저장하거나 전달하기 위한 텍스트 형식
#왜 json을 사용하는가? - 데이터 교환이 쉽고, 다양한 언어에서 지원되며, 사람이 읽기 쉽기 때문 => 구조적으로 해결해주기 때문에
#json 으로 저장하려면? - json module 사용해서 저장 (객체 > 딕션어리 > json) / json.load() - json > 딕션어리 > 객체 
#json은 주석을 달 수 없음..

from game import QuizGame   #game.py 에서 QuizGame class를 가져온다

def main():
    try:
        game = QuizGame()
        game.run()
    except KeyboardInterrupt:     #사용자가 Ctrl+C로 강제 종료할 때 발생하는 예외
        print("\n\n⚠️  프로그램이 강제 종료되었습니다.")
        print("안전하게 종료하기 위해 데이터를 저장합니다...")
        try:
            # 현재 게임 상태 저장 시도
            if hasattr(game, 'save_quizzes'):    #hasattr() - 객체가 특정 속성이나 메서드를 가지고 있는지 확인하는 함수(내장함수 like "IOError, json.JSONDecodeError")
                game.save_quizzes()
            if hasattr(game, 'save_high_score'):
                game.save_high_score()
            print("✅ 데이터가 성공적으로 저장되었습니다.")   #2개의 if절 (2개의 메서드가 확인) 통과 되었을 때만
        except Exception as e:   #Exception - 모든 예외의 기본 클래스, 어떤 종류의 예외가 발생하든지 잡아낼 수 
            print(f"⚠️  데이터 저장 중 오류가 발생했습니다: {e}")
        print("게임을 종료합니다. 안녕히 가세요!")
    except EOFError:     #입력 스트림 종료 시 (맨 위 try 에 걸림)
        print("\n\n⚠️  입력 스트림이 종료되었습니다.")
        print("안전하게 종료하기 위해 데이터를 저장합니다...")
        try:
            # 현재 게임 상태 저장 시도
            if hasattr(game, 'save_quizzes'):
                game.save_quizzes()
            if hasattr(game, 'save_high_score'):
                game.save_high_score()
            print("✅ 데이터가 성공적으로 저장되었습니다.")
        except Exception as e:
            print(f"⚠️  데이터 저장 중 오류가 발생했습니다: {e}")
        print("게임을 종료합니다. 안녕히 가세요!")


if __name__ == "__main__":   #직접 실행할 때만 실행...'의도치 않은 참견 방지' 
    main()

