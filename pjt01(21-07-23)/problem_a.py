import json
from pprint import pprint

def movie_info(movie):
    # 문서에서 각 'key'값에 맞는 'value'값을 출력
    movie_info = {
        'id' : movie['id'],
        'title' : movie['title'],
        'poster_path': movie['poster_path'],
        'vote_average' : movie['vote_average'],
        'overview' : movie['overview'],
        'genre_ids' : movie['genre_ids'],        
    }
    return movie_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))