import requests
from tmdb import TMDBHelper
from pprint import pprint

tmdb_helper = TMDBHelper('45fe12dfc780769c529bfbcba00bf611')

url = tmdb_helper.get_request_url(region='KR', language='ko')

data = requests.get(url).json()

def vote_average_movies():

    # 영화의 데이터값 얻기
    data_results = data['results']
    over_8_movies = []

    for data_result in data_results :
        # 평점이 8점 이상일 때 그 영화의 데이터 가져오기
        if data_result['vote_average'] >= 8 :
            over_8_movies.append(data_result)

    return over_8_movies

if __name__ == '__main__':
    pprint(vote_average_movies())