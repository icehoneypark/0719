import requests
from tmdb import TMDBHelper
from pprint import pprint

tmdb_helper = TMDBHelper('45fe12dfc780769c529bfbcba00bf611')

url = tmdb_helper.get_request_url(region='KR', language='ko')

data = requests.get(url).json()

def credits(title):

    movie_id = tmdb_helper.get_movie_id(title)

    url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=45fe12dfc780769c529bfbcba00bf611'

    data2 = requests.get(url2).json()

    cast, crew = [], []

    # 영화에 대한 데이터가 없을 때
    if    data2.get('success') == False :
        return None
    else :
        # cast_id가 10보다 작은 경우 이름 가져오기
        for casts in data2['cast'] :
            if  casts['cast_id'] <= 10 :
                cast.append(casts['name'])

        # department가 Directing인 crew의 이름 가져오기
        for crews in data2['crew'] :
            if  crews['department'] == 'Directing' :
                crew.append(crews['name'])

        # 각 key에 맞는 value 입력 후 딕셔너리 변수 만들기
        high_member = {'cast' : cast, 'crew' : crew}

        return high_member

if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))
