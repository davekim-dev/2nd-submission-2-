#json 이란? - JavaScript Object Notation, 데이터를 저장하거나 전달하기 위한 텍스트 형식
#왜 json을 사용하는가? - 데이터 교환이 쉽고, 다양한 언어에서 지원되며, 사람이 읽기 쉽기 때문 => 구조적으로 해결해주기 때문에
#json 으로 저장하려면? - json module 사용해서 저장 (객체 > 딕션어리 > json) / json.load() - json > 딕션어리 > 객체 
#json은 주석을 달 수 없음..

from game import QuizGame   #game.py 에서 QuizGame class를 가져온다

def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":   #직접 실행할 때만 실행...'의도치 않은 참견 방지' 
    main()

