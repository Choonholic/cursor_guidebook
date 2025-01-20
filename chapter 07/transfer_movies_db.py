import json
import sqlite3

def transfer_data():
    # JSON 파일 읽기
    with open('movies.json', 'r', encoding='utf-8') as json_file:
        movie_data = json.load(json_file)

    # SQLite 데이터베이스 연결
    conn = sqlite3.connect('movies.sqlite')
    cursor = conn.cursor()

    # JSON 데이터를 SQLite 데이터베이스로 삽입
    for title, info in movie_data.items():
        cursor.execute('''
            INSERT OR IGNORE INTO movies (title, genre, mood, length)
            VALUES (?, ?, ?, ?)
        ''', (title, int(info['genre']), int(info['mood']), int(info['length'])))

    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()
    print("JSON 데이터가 SQLite 데이터베이스로 이전되었습니다.")

if __name__ == "__main__":
    transfer_data()
 