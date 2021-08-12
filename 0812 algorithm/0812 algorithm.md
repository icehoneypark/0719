# 1. 특별한 정렬

```
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5
 

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다
```

```
입력 :
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11 
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

출력 :
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21
```

```
t = int(input())

for cnt_t in range(t) :

    n = int(input())

    get_data = list(map(int, input().split()))

    result = []

    for _ in range(5) :

        max = 21e-8
        min = 21e8

        for data in get_data :
            if max < data :
                max = data
            if min > data :
                min = data
        get_data.remove(max)
        get_data.remove(min)
        result.append(max)
        result.append(min)
    print('#{} '.format(cnt_t+1), end='')
    print(*result)
```

# 2. 이진탐색

```
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.



책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.
```

```
입력 :
3
400 300 350
1000 299 578
1000 222 888

출력 :
#1 A
#2 0
#3 A
```

```
t = int(input())

for cnt_t in range(t) :

    get_data = list(map(int, input().split()))

    left_A = left_B = 1
    right_A = right_B = get_data[0]
    target_A = get_data[1]
    target_B = get_data[2]

    lst_A = [0]
    lst_B = [0]

    for page in range(1, right_A + 1) :
        lst_A.append(page)
    for page in range(1, right_B + 1) :
        lst_B.append(page)

    cnt_A = 0
    cnt_B = 0

    success_A = 0
    success_B = 0

    while left_A <= right_A :
        mid = (left_A + right_A) // 2
        cnt_A += 1
        if target_A == lst_A[mid]:
            success_A = 1
            break
        elif target_A < lst_A[mid] :
            right_A = mid
        elif target_A > lst_A[mid] :
            left_A = mid
    while left_B <= right_B :
        mid = (left_B + right_B) // 2
        cnt_B += 1
        if target_B == lst_B[mid]:
            success_B = 1
            break
        elif target_B < lst_B[mid] :
            right_B = mid
        elif target_B > lst_B[mid] :
            left_B = mid

    if success_A == 1 :
        if success_B == 1 :
            if cnt_A > cnt_B :
                print('#{} B'.format(cnt_t + 1))
            elif cnt_A < cnt_B :
                print('#{} A'.format(cnt_t + 1))
            else :
                print('#{} 0'.format(cnt_t + 1))
        else :
            print('#{} A'.format(cnt_t + 1))
    else :
        if success_B == 0 :
            print('#{} 0'.format(cnt_t + 1))
        else :
            print('#{} B'.format(cnt_t + 1))
```

# 3. 부분집합의 합

```
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
 

예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
 

테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력 :
3
3 6
5 15
5 10

출력 :
#1 1
#2 1
#3 0	
```

```
n = [1,2,3,4,5,6,7,8,9,10,11,12]

t = int(input())

for cnt_t in range(t) :

    tmp = list(map(int,input().split()))

    ans = 0
    
    for bit in range(1<<12) :
        sum = 0
        cnt = 0
        for j in range(12) :
            if bit & (1 << j):
                sum += n[j]
                cnt += 1
        if cnt == tmp[0] and sum == tmp[1]:
            ans += 1
    print('#{} {}'.format(cnt_t+1, ans))
```

# 4. 색칠하기

```
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
 


예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.

2

2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )

3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강), color = 2 (파랑)

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력 :
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

출력 :
#1 4
#2 5
#3 7
```

```
t = int(input())

for cnt_t in range(t) :
    n = int(input())
    red_fixel = []
    blue_fixel = []
    for cnt_n in range(n) :
        colors = list(map(int,input().split()))
        # color_y1 = colors[0]
        # color_x1 = colors[1]
        # color_y2 = colors[2]
        # color_x2 = colors[3]
        # color = colors[4]

        for y in range(colors[0], colors[2] + 1) :
            for x in range(colors[1], colors[3] + 1) :
                if colors[4] == 1:
                    red_fixel.append([y,x])
                else :
                    blue_fixel.append([y,x])
    # if ['tmp'] in red_fixel :
    #     red_fixel.remove(['tmp'])
    # if ['tmp'] in blue_fixel :
    #     red_fixel.remove(['tmp'])
    # set(red_fixel)
    # set(blue_fixel)

    result = 0

    for red in red_fixel :
        for blue in blue_fixel :
            if red == blue :
                result += 1
    print('#{} {}'.format(cnt_t + 1, result))
```

# 5. 파리퇴치

```
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

아래는 N=5 의 예이다.
 



M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

죽은 파리의 개수를 구하라!

예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
 



[제약 사항]

1. N 은 5 이상 15 이하이다.

2. M은 2 이상 N 이하이다.

3. 각 영역의 파리 갯수는 30 이하 이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

다음 N 줄에 걸쳐 N x N 배열이 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```

```
t = int(input())
for cnt_t in range(1, t+1) :

    tmp1 = list(map(int, input().split()))  # 1차원 리스트 (한줄)

    n = tmp1[0]
    m = tmp1[1]
    data = []

    area_sum_list = []

    for _ in range(n) :
        tmp2 = list(map(int, input().split()))  # 1차원 리스트 (한줄)
        data.append(tmp2)

    for w in range(n-m+1) :
        for z in range(n-m+1) :
            tmp_sum = 0
            for y in range(m) :
                for x in range(m) :
                    tmp_sum += data[y+w][x+z]

            area_sum_list.append((tmp_sum))

    max_sum = 21e-8
    for value in area_sum_list :
        if max_sum < value :
            max_sum = value

    print('#{} {}'.format(cnt_t, max_sum))
```

# 6. 어디에 단어가 들어갈 수 있을까

```
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

[예제]

N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때
 



길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로 4번)이 된다.
 


[제약 사항]

1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)

2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.

테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.

퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```

```
t = int(input())

for cnt_t in range(t) :
    tmp = list(map(int,input().split()))

    n = tmp[0]
    k = tmp[1]
    lst = []
    for _ in range(n) :
        tmp2 = list(map(int,input().split()))
        lst.append(tmp2)

    a1 = [0]*n
    a2 = [0]*n
    lst.insert(0, a1)
    lst.insert(len(lst), a2)

    for lst_data in lst :
        lst_data.insert(0, 0)
        lst_data.insert(len(lst_data), 0)
        # print(lst_data)

    cnt = 0
    result = 0
    for y_tmp in range(1, n+1) :
        for x in range(1, n-k+2) :
            if lst[y_tmp][x] == 1 :
                if lst[y_tmp][x-1] == 0 :
                    if lst[y_tmp][x+k] == 0 :
                        for tmp in range(k) :
                            if lst[y_tmp][x+tmp] == 1 :
                                cnt += 1
                            else :
                                cnt = 0
                                break
                            if cnt == k :
                                cnt = 0
                                result += 1
    for x_tmp in range(1, n+1) :
        for y in range(1, n-k+2) :
            if lst[y][x_tmp] == 1 :
                if lst[y-1][x_tmp] == 0 :
                    if lst[y+k][x_tmp] == 0 :
                        for tmp in range(k) :
                            if lst[y+tmp][x_tmp] == 1 :
                                cnt += 1
                            else :
                                cnt = 0
                                break
                            if cnt == k :
                                cnt = 0
                                result += 1


    print('#{} {}'.format(cnt_t+1, result))
```

# 7. 숫자를 정렬하자

```
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

[제약 사항]

N 은 5 이상 50 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```

```
t = int(input())

for cnt_t in range(1, t+1) :

    n = int(input())

    lst = list(map(int, input().split()))  # 1차원 리스트 (한줄)

    for i in range(n-1) :
        for j in range(1, n-i) :
            if lst[i] > lst[i+j] :
                lst[i], lst[i+j] = lst[i+j], lst[i]

    print('#{} '.format(cnt_t), end='')
    print(*lst)
```

# 8. Ladder1

```
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.
 


<그림 1> 사다리 게임에 대한 설명 (미니맵)

아래 <그림 2>와 같은 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라 (‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).
 
 
<그림 2> 테스트 케이스에 의해 생성되는 실제 사다리의 모습

[제약 사항]

한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다.
```

```
for cnt_t in range(1, 11):

    cnt_t = int(input())

    ladder = []

    for _ in range(100) :
        tmp = list(map(int,input().split()))
        ladder.append(tmp)

    for x in range(100) :
        y = 0
        if ladder[y][x] == 1 :
            start = x
            while y < 100 :
                if x == 0 :
                    if ladder[y][x+1] == 0 :
                        y += 1
                    if ladder[y][x+1] == 1 :
                        while 1 :
                            x += 1
                            if x == 99:
                                break
                            if ladder[y][x+1] == 0 :
                                break
                        y += 1
                elif x == 99 :
                    if ladder[y][x-1] == 0 :
                        y += 1
                    if ladder[y][x-1] == 1 :
                        while 1 :
                            x -= 1
                            if x == 0:
                                break
                            if ladder[y][x-1] == 0 :
                                break
                        y += 1
                else :
                    if ladder[y][x+1] == 0 and ladder[y][x-1] == 0 :
                        y += 1
                    if ladder[y][x+1] == 1 :
                        while 1:
                            x += 1
                            if x == 99:
                                break
                            if ladder[y][x+1] == 0:
                                break
                        y += 1
                    if ladder[y][x-1] == 1:
                        while 1:
                            x -= 1
                            if x == 0:
                                break
                            if ladder[y][x-1] == 0:
                                break
                        y += 1
                if ladder[y][x] == 2 :
                    print('#{} {}'.format(cnt_t, start))
                if y == 99 :
                    break
```

