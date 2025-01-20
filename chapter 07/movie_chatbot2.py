def movie_chatbot():
    print("안녕하세요! 영화 추천 챗봇입니다. 몇 가지 질문에 답해주시면 영화를 추천해드릴게요.")
    print("각 질문에 0을 입력하면 종료됩니다.\n")

    # 영화 정보를 저장할 사전
    movie_database = {
        "어벤져스: 엔드게임": {"genre": "액션", "mood": "밝은", "length": "120분 이상"},
        "조커": {"genre": "코미디", "mood": "어두운", "length": "90분 ~ 120분"},
        "기생충": {"genre": "드라마", "mood": "감동적인", "length": "120분 이상"}
    }

    while True:
        print("무엇을 하시겠습니까?")
        print("1) 영화 추천 받기  2) 영화 정보 추가하기")
        action = input("선택 (0 to exit): ")
        if action == '0':
            print("챗봇을 종료합니다. 감사합니다!")
            break

        if action == '1':
            # 영화 추천 로직
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

            # 영화 추천
            print("\n추천 영화:")
            found = False
            for title, info in movie_database.items():
                if info["genre"] == genre and info["mood"] == mood and info["length"] == length:
                    print(f" - {title}")
                    found = True
            if not found:
                print(" - 추천할 영화가 없습니다.")

        elif action == '2':
            # 영화 정보 추가 로직
            title = input("영화 제목을 입력하세요: ")
            if title in movie_database:
                print("이미 존재하는 영화입니다.")
                continue

            print("영화의 장르를 선택하세요:")
            print("   1) 액션  2) 코미디  3) 드라마  4) 공포  5) SF")
            genre = input("선택: ")

            print("영화의 분위기를 선택하세요:")
            print("   1) 밝은  2) 어두운  3) 감동적인  4) 긴장감 있는")
            mood = input("선택: ")

            print("영화의 길이를 선택하세요:")
            print("   1) 90분 이하  2) 90분 ~ 120분  3) 120분 이상")
            length = input("선택: ")

            # 영화 정보 추가
            movie_database[title] = {"genre": genre, "mood": mood, "length": length}
            print(f"영화 '{title}'가 추가되었습니다.")

        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

# movie_chatbot() 함수를 호출하여 챗봇을 실행할 수 있습니다.
if __name__ == "__main__":
    movie_chatbot()
    