from imdb import IMDb

def movie_chatbot():
    print("안녕하세요! 영화 추천 챗봇입니다. IMDb에서 영화를 추천해드릴게요.")
    print("각 질문에 0을 입력하면 종료됩니다.\n")

    # IMDbPY 객체 생성
    ia = IMDb()

    while True:
        print("1. 어떤 장르의 영화를 보고 싶으신가요?")
        print("   1) 액션  2) 코미디  3) 드라마  4) 공포  5) SF")
        genre_choice = input("선택 (0 to exit): ")
        if genre_choice == '0':
            print("챗봇을 종료합니다. 감사합니다!")
            break

        # IMDb 장르 매핑
        genre_map = {
            '1': 'Action',
            '2': 'Comedy',
            '3': 'Drama',
            '4': 'Horror',
            '5': 'Sci-Fi'
        }
        selected_genre = genre_map.get(genre_choice, None)
        if not selected_genre:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        # IMDb에서 영화 검색
        print("\n추천 영화:")
        movies = ia.search_movie(selected_genre)
        found = False
        for movie in movies[:10]:  # 상위 10개 영화만 표시
            print(f" - {movie['title']}")
            found = True
        if not found:
            print(" - 추천할 영화가 없습니다.")

# movie_chatbot() 함수를 호출하여 챗봇을 실행할 수 있습니다.
if __name__ == "__main__":
    movie_chatbot()
