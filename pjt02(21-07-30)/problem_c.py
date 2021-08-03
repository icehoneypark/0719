import requests
from tmdb import TMDBHelper
from pprint import pprint

tmdb_helper = TMDBHelper('45fe12dfc780769c529bfbcba00bf611')

url = tmdb_helper.get_request_url(region='KR', language='ko')

data = requests.get(url).json()


def ranking():

    data_results = data['results']

    vote_avg_list = []

    top5_movie_list = []

    # 평점값만 가져옴
    for data_result in data_results :
        vote_avg_list.append(data_result['vote_average'])
    
    # 내림차순으로 정렬
    vote_avg_list.sort(reverse=True)
    
    # 인덱서 5부터 삭제 (1 ~ 5등만 남김)
    del vote_avg_list[5:len(vote_avg_list)]

    # 중복되는 숫자 삭제
    vote_avg_list = set(vote_avg_list)

    for vote in vote_avg_list :
        for data_result in data_results :
            # 평점이 1 ~ 5등의 평점과 같을 때, 영화 데이터 입력
            if data_result['vote_average'] == vote :
                top5_movie_list.append(data_result)

    return top5_movie_list

if __name__ == '__main__':
    pprint(ranking())