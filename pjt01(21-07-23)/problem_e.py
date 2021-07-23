import json

def dec_movies(movies):
    movie_ids = []
    movie_dec_list = []
    # 영화의 id 값을 리스트로 작성
    for movie in movies :
        movie_ids.append(movie['id'])
    # 각 영화의 id 값에 맞는 문서를 읽어 개봉일을 찾아 리스트로 작성
    for movie_id in movie_ids :
        movie_each_list_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_each_list = json.load(movie_each_list_json)
        # 개봉일을 한글자씩 잘라 리스트로 정리
        movie_date = list(movie_each_list['release_date'])
        # 12월인 영화의 제목을 리스트로 작성
        if movie_date[5] == '1' :
            if movie_date[6] == '2' :
                movie_dec_list.append(movie_each_list['title'])
    return movie_dec_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))