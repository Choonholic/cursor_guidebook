def movie_chatbot():
    print("안녕하세요! 영화 추천 챗봇입니다. 몇 가지 질문에 답해주시면 영화를 추천해드릴게요.")
    print("각 질문에 0을 입력하면 종료됩니다.\n")

    while True:
        print("1. 어떤 장르의 영화를 보고 싶으신가요?")
        print("   1) 액션  2) 코미디  3) 드라마  4) 공포  5) SF")
        genre = input("선택 (0 to exit): ")
        if genre == '0':
            print("챗봇을 종료합니다. 감사합니다!")
            break

        print("2. 어떤 분위기의 영화를 선호하시나요?")
        print("   1) 밝은  2) 어두운  3) 감동적인  4) 긴장감 있는")
        mood = input("선택 (0 to exit): ")
        if mood == '0':
            print("챗봇을 종료합니다. 감사합니다!")
            break

        print("3. 선호하는 영화의 길이는?")
        print("   1) 90분 이하  2) 90분 ~ 120분  3) 120분 이상")
        length = input("선택 (0 to exit): ")
        if length == '0':
            print("챗봇을 종료합니다. 감사합니다!")
            break

        # 간단한 추천 로직 (예시)
        print("\n추천 영화:")
        if genre == '1' and mood == '1':
            print(" - '어벤져스: 엔드게임'")
        elif genre == '2' and mood == '2':
            print(" - '조커'")
        # 추가적인 추천 로직을 여기에 추가할 수 있습니다.
        else:
            print(" - '기생충'")

        print("\n다시 시작하려면 아무 키나 누르세요. 종료하려면 0을 입력하세요.")
        restart = input()
        if restart == '0':
            print("챗봇을 종료합니다. 감사합니다!")
            break

# movie_chatbot() 함수를 호출하여 챗봇을 실행할 수 있습니다.
if __name__ == "__main__":
    movie_chatbot()
