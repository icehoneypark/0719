import requests
from tmdb import TMDBHelper
from pprint import pprint

tmdb_helper = TMDBHelper('45fe12dfc780769c529bfbcba00bf611')

url = tmdb_helper.get_request_url(region='KR', language='ko')

data = requests.get(url).json()

rec_movies_title = []

# 입력한 영화의 id 값 얻어오기
def recommendation(title):
    movie_id = tmdb_helper.get_movie_id(title)

    # 영화 id 값에 맞는 주소 정의
    url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=45fe12dfc780769c529bfbcba00bf611&language=ko'

    data2 = requests.get(url2).json()

    # 존재하는 영화를 입력했지만 추천영화가 없을 때
    if  data2.get('total_results') == 0 :
        return []
    # 존재하지 않는 영화를 입력했을 때
    elif    data2.get('success') == False :
        return None
    else :
    # 추천영화가 있을 때
        for data2_title in data2['results'] :
            rec_movies_title.append(data2_title['title'])
        return rec_movies_title

if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))