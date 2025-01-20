import requests
from bs4 import BeautifulSoup
import csv

# 웹사이트 URL
url = "https://jpub.tistory.com/category/%EB%8F%84%EC%84%9C%20%EC%86%8C%EA%B0%9C"

# 웹페이지 요청
response = requests.get(url)
response.raise_for_status()  # 요청이 성공했는지 확인

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 포스트 아이템 추출
post_items = soup.find_all('div', class_='post-item')

# CSV 파일 열기
with open('web_scrape.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 헤더 작성
    writer.writerow(['Image URL', 'Title', 'Excerpt'])

    # 각 포스트에서 정보 추출
    for post in post_items:
        # 미리보기 이미지 URL
        img_tag = post.find('img')
        img_url = img_tag['src'] if img_tag else 'No image'

        # 제목
        title_tag = post.find('span', class_='title')
        title = title_tag.text if title_tag else 'No title'

        # 내용 요약
        excerpt_tag = post.find('span', class_='excerpt')
        excerpt = excerpt_tag.text if excerpt_tag else 'No excerpt'

        # 추출한 정보를 CSV 파일에 작성
        writer.writerow([img_url, title, excerpt])
