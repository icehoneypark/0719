# PJT 01

### 이번 pjt 를 통해 배운 내용

* Python 기본 문법 실습
* 파일 입출력에 대한 이해
* 데이터 구조에 대한 분석과 이해
* 데이터를 가공하고 JSON 형태로 저장



## A. 제공되는 영화 데이터의 주요내용 수집

* 요구사항 : 샘플 영화데이터가 주어집니다. 이 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.

* 결과 : 

  1. 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져옵니다.  

  2.가져온 정보를 새로운 dictionary로 반환하는 함수 movie_info를 완성합 니다.

  ```python
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
  ```
  
  * 문제 접근 방법 및 코드 설명 : 특정 파일의 데이터를 json 형태로 받아와 딕셔너리로 다루며 필요한 정보를 수집
* 이 문제에서 어려웠던점 : 딕셔너리 데이터에서 특정한 정보를 추출하는 것이 어려움
  * 내가 생각하는 이 문제의 포인트 : 특정 파일의 데이터를 json 형태로 받아오기, 딕셔너리에서 원하는 정보를 가져오는 방법을 아는 것이 중요
  
  -----

  ## B. 제공되는 영화 데이터의 주요내용 수집

* 요구사항 : 이전단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔 반환하는 함수를 완성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.

* 결과 : 

  1. 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져옵니다.
  2. genres.json파일을 이용하여 genre_ids를 genre_names로 변환하여 dictionary에 추가합니다.
  3. 완성된 dictionary를 반환하는 함수 movie_info를 완성합니다.

  ```python
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
  ```

  * 문제 접근 방법 및 코드 설명 : movie.json에서 id값을 찾아 genres.json에서 id값과 일치하는  key 값으로 value값을 추출하고, 그 값을 movie.json에서 얻은 자료와 합치는 과정이 필요
  * 이 문제에서 어려웠던점 : 한 파일에 있는 데이터를 찾아 이 정보를 토대로 다른 자료에 있는 자료를 찾는 것과, 그 후 다시 두 파일의 내용을 합치는 것이 어려움
  * 내가 생각하는 이 문제의 포인트 : 두 파일에서의 key 값과 value 값을 혼동하지 않고 정확하게  사용하여 데이터를 정리하는 것이 중요

-----

## C. 제공되는 영화 데이터의 주요내용 수집

* 요구사항 : TMDB기준 평점이 높은 20개의 영화데이터가 주어집니다. 이 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다. 완성된 함수는 향후 커뮤니티 서비스에서 제공되는 영화 목록을 제공하기 위한 기능으로 사용됩니다.

* 결과 : 

  1. 전 단계의 함수 구조를 재사용합니다.
  2. 영화 전체 정보를 수정하여 반환하는 함수 movie_info를 완성합니다.

  ```python
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
  ```
  
  * 문제 접근 방법 및 코드 설명 : B 문제에서 나아가서 movies.json에 있는 모든 영화에 대한 원하는 자료를 추출하여 정리
  * 이 문제에서 어려웠던점 : movies.json에 있는 영화에 대한 데이터를 추출하고 이를 리스트로 만드는 것이 어려움
  * 내가 생각하는 이 문제의 포인트 : B 문제에서 만든 함수의 변수를 다시 바꾸고 얻은 데이터를 다시 리스트로 만드는 것이 중요

-----

## D. 제공되는 영화 데이터의 주요내용 수집

* 요구사항 : 세부적인 영화 정보 중 수익 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성합니다. 해당 데이터는 향후 커뮤니 티 서비스에서 메인 페이지 기본정보로 사용됩니다.

* 결과 : 

  1. 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성합니다.

  ```python
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
  ```
  
  * 문제 접근 방법 및 코드 설명 : movies.json에서 얻은 id 값에 대한 자료를 movies 폴더에서 파일을 찾은 후, 그에 맞는 수익정보(revenue) 값을 추출해 리스트로 정리. 수익정보 중 가장 수익액이 큰 영화를 찾아 제목(title)을 찾아 반환
  * 이 문제에서 어려웠던점 : id 값을 가져와 그에 맞는 각 파일에서 수익액을 찾아오고 그 값 중 가장 큰 수익액을 찾는 것까진 쉬웠으나, 이 값을 기준으로 다시 영화의 제목을 찾는 것이 어려움
  * 내가 생각하는 이 문제의 포인트 : for문을 여러번 사용하고, 변수의 이름들이 비슷해 헷갈리지 않으며 딕셔너리의 key, value 값을 정확하게 사용해 원하는 데이터를 찾는 것이 중요

-----

## E. 제공되는 영화 데이터의 주요내용 수집

* 요구사항 : 세부적인 영화 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다. 해당 데이터는 향후 커뮤니티 서비스에서 추천기능의 정보로 사용됩니다.

* 결과 : 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 dec_movies 를 완성합니다.

  ```python
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
  ```
  
  * 문제 접근 방법 및 코드 설명 : movies.json에서 id 값을 찾아 그 값에 맞는 영화들의 개봉일(release_date)를 찾아 리스트로 정리, 개봉일을 1개의 문자열로 잘라 배열의 6번째, 7번째의 값이 1, 2(12월)인 데이터를 추출한 후 그에 맞는 영화제목을 추출
  * 이 문제에서 어려웠던점 : 처음에 코드를 잘못 작성해 (id).json이 아닌 movies.json에서 개봉일을 추출해 실행결과와 파일의 데이터가 일치하지 않아 오랫동안 문제에 대해 고민함, 문제점을 발견한 후 다시 해결
  * 내가 생각하는 이 문제의 포인트 : 각 id 값에 맞는 영화의 개봉일을 리스트로 만들어 개봉일이 12월인 영화를 필터링하는 것이 중요





# 후기

* 딕셔너리에 대한 것은 여러번 해도 익숙해지기 힘든 것 같다. 딕셔너리 데이터를 계속 사용하며 print()를 계속해서 사용하는 습관이 들기 시작하면서 코드를 작성하는데 좀 더 수월해진 것 같다.
* 반복문이 많아지고 이에 대한 변수들이 많아지면서 어떠한 데이터를 어디에 사용했는지 헷갈리는 순간이 몇번 있었다. 반복문이 많을 때도 print()를 자주 사용하는 습관을 들이는 것이 좋은 것 같다.
* 파일을 여는 함수를 사용해본 적이 없었는데 주어진 코드를 활용해 f-string을 사용해 각 (id).json에서 데이터를 얻어오는 작업을 성공하고 뿌듯했다.
* 아직 배운 적은 없지만 append()는 정말 편한 것 같다.
* E 문제에서 집중력이 흐려진 상태에서 코드를 작성하다가 release_date를 movies.json에서 추출해 목록에 맞지 않는 영화들이 나왔다. movies.json과 (id).json에서의 개봉일 값이 다르다는 것에 당황했고, 반 사람들이 정답을 공유해서 내가 틀렸다는 것을 알았기에 다행이였다. 현실에서 이러한 상황이 발생해 소비자들에게 혼동을 주고 피해를 불러일으킨다면 정말 아찔할 것이다. 이 부분은 크게 반성해야할 것이다.