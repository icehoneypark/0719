import json

def max_revenue(movies):
    movie_ids = []
    movie_each_revenue = []
    movie_copy_list = []
    movie_best_revenue = 0
    # movies.json의 각 영화에 대한 id 값을 찾아 리스트로 작성
    for movie in movies :
        movie_ids.append(movie['id'])
    # movies.json에서 id값을 찾아 movies 파일에 있는 각 id.json파일에서 영화의 상세정보를 찾음
    for movie_id in movie_ids :
        movie_each_list_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_each_list = json.load(movie_each_list_json)
        # 각 영화의 매출액을 리스트로 작성
        movie_each_revenue.append(movie_each_list['revenue'])
        movie_copy_list.append(movie_each_list)
        # 가장 매출액이 많은 영화의 매출액을 찾음
    for movie_revenue in movie_each_revenue :
        if movie_best_revenue < movie_revenue :
            movie_best_revenue = movie_revenue
        # 가장 매출액이 많은 영화의 제목을 찾음
    for movie_find_revenue in movie_copy_list :
        if movie_best_revenue == movie_find_revenue['revenue'] : 
            return movie_find_revenue['title']
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))