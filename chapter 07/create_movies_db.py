import sqlite3

def create_database():
    # 데이터베이스 연결
    conn = sqlite3.connect('movies.sqlite')
    cursor = conn.cursor()

    # movie_db.sql 파일의 내용을 읽어와서 실행
    with open('movie_db.sql', 'r', encoding='utf-8') as sql_file:
        sql_script = sql_file.read()
    
    cursor.executescript(sql_script)

    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()
    print("movies.sqlite 데이터베이스가 생성되었습니다.")

if __name__ == "__main__":
    create_database()
