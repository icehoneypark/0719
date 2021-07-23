import json
from pprint import pprint

def movie_info(movies, genres):
    movie_info = []
    for movie in movies :
        movie_type_name = []
        # movies.json문서에서 id값을 찾아 그에 맞는 장르 영어표현을 genres.json문서에서 찾음
        for genre_id in movie['genre_ids'] :
            for genre in genres :
                if genre['id'] == genre_id :
                    movie_type_name.append(genre['name'])
                    # movies.json 문서와 genres.json 문서의 데이터를 합침
        movie_infos = {
            'genre_names': movie_type_name,
            'id' : movie['id'],
            'title' : movie['title'],
            'poster_path': movie['poster_path'],
            'vote_average' : movie['vote_average'],
            'overview' : movie['overview'],
        }
        #movies.json에 있는 모든 영화에 대한 내용을 list로 만듬
        movie_info.append(movie_infos)
    return movie_info
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))