import requests
from tmdb import TMDBHelper

# 본인의 key값 입력
tmdb_helper = TMDBHelper('45fe12dfc780769c529bfbcba00bf611')

# tmdb.py에 정의돼어있는 함수, 한국에서의 영화정보를 가져오기, 한국어로 표기
url = tmdb_helper.get_request_url(region='KR', language='ko')

# json 형식으로 url 주소의 데이터 받아오기
data = requests.get(url).json()

# data에 있는 영화의 갯수를 길이측정으로 카운트
def popular_count():

    return len(data['results'])

if __name__ == '__main__':
    print(popular_count())