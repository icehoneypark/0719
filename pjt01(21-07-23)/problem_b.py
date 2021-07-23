import json
from pprint import pprint

def movie_info(movie, genres):
    movie_type_name = []
    # movie.json문서에서 id값을 찾아 그에 맞는 장르 영어표현을 genres.json문서에서 찾음
    for genre_id in movie['genre_ids'] :
        for genre in genres :
            if genre['id'] == genre_id :
                movie_type_name.append(genre['name'])
    # movie.json 문서와 genres.json 문서의 데이터를 합침
    movie_info = {
        'genre_names': movie_type_name,
        'id' : movie['id'],
        'title' : movie['title'],
        'poster_path': movie['poster_path'],
        'vote_average' : movie['vote_average'],
        'overview' : movie['overview'],
    }
    return movie_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))