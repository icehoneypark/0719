# 1. 부분집합 합

```
N 개의 정수가 입력됩니다. (중복된 수는 입력되지 않는다)
입력받은 정수들의 부분집합 중 합이 0이 되는 경우의 수를 구해주세요.

단, 부분집합중 공집합은 합을 0으로 합니다.


[입력]
10개의 테스트 케이스가 입력됩니다. 
각 테스트 케이스 별로
첫째줄에는 N ( 1 <= N <= 10)
두번째 줄에는 N개의 정수가 공백으로 구분되어 입력됩니다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  부분집합의 합이 0이 되는 경우의 수를 출력합니다
```

```
입력 :
5
2 3 -2 -3 5 
5
1 5 -2 -4 2 
5
-9 -3 4 -10 -1 
6
-6 8 -8 -5 -9 -3 
7
-9 1 5 -8 -3 6 -6 
7
-8 3 2 -9 6 8 5 
9
-3 -4 1 8 -1 2 9 5 4 
9
-7 1 -8 3 -6 -9 -2 -3 7 
10
7 9 -7 -9 -1 8 6 5 0 -8 
10
-2 -4 -10 -8 -6 -5 0 -1 -9 3 

출력 :
#1 5
#2 3
#3 2
#4 3
#5 5
#6 6
#7 11
#8 10
#9 28
#10 4
```

```
for w in range(10) :
    N = int(input())

    lst = list(map(int, input().split()))

    n = len(lst)

    cnt = 0

    sum_tmp = 0

    for x in range(1<<n) :

        sum_tmp = 0
        tmp = []
        for y in range(n+1) :
            if x & (1<<y) :
                # print(lst[y], end=", ")
                tmp.append(lst[y])
        for tmp_data in tmp :
            sum_tmp += tmp_data

        if sum_tmp == 0 :
            cnt += 1

    print('#{} {}'.format(w + 1, cnt))
```



# 2. 델타검색

```
N x N 2차원 리스트가 입력됩니다.
어느 한 요소에 대하여 상,하,좌,우로 이웃한 요소와의 차의 절대값들을 구하고 이들의 합을 구하려 합니다.

예를들어, 아래 그림에서 7 값의 상하좌우로 이웃한 값는 2,12,6,8 이며 차들의 절대값의 합은 12 입니다.
 

NxN 리스트에 있는 모든 요소들에 대해서 위처럼 조사하여 이들을 전부 더한 총합을 구해주세요.
단, [0][0] 처럼 이웃한 요소가 2개인 값은 2개 대해서만 합을 구해줍니다.


[ 입력 ]
10개의 테스트케이스가 입력됩니다.
각 테스트 케이스마다 첫 번째 줄에는 N ( 1 <= N <= 100 )
두 번째 줄부터는 N 줄에 걸쳐 N x N 개의 정수가 입력되며 정수들은 공백으로 구분되어 입력된다.

[ 출력 ] 
#과 테스트케이스 번호(1~10)을 출력후 공백과 총합을 출력한다.
```

```
입력 :
5 // N 값
1 7 4 0 9 // N x N 개의 정수 입력
4 8 8 2 4 
5 5 1 7 1 
1 5 2 7 6 
1 4 2 3 2 

출력 :
#1 246
#2 232
#3 1352
#4 27782
#5 1246
#6 4870
#7 11708
#8 331784
#9 13129418
#10 135355682
```

```
for i in range(10) :

    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)] # N 개의 1차원 리스트가 만들어짐

    y = 0
    x = 0
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    abs_sum = 0


    while 1 :
        while 1 :
            for t in range(4):
                ny = y + dy[t] # 새로운 좌표는 현재 좌표에서 변화량 더해주면 된다
                nx = x + dx[t]
                if ny < 0 or nx <0 or ny >= N or nx >= N :
                    pass
                else :
                    # continue # 범위 바깥에 나가면 continue -> 다음 반복 진행
                    abs_data = abs(MAP[y][x]-MAP[ny][nx])
                    abs_sum += abs_data
            x += 1
            if x == N :
                x = 0
                break
        y += 1
        if y == N :
            print('#{} {}'.format(i + 1, abs_sum))
            break
```

# 3. 달팽이 숫자

```
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


[예제]

N이 3일 경우,

N이 4일 경우,
 


[제약사항]

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```

```
입력 :
2    
3   
4    

출력 :
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
```

```
t = int(input())

for q in range(t) :
    k = int(input())

    if k == 1 :
        print('#{}'.format(q + 1))
        print('1')
    elif k < 1 :
        print('')
    else :
        lst = [0]*(k+2)
        new_lst = []

        for _ in range(k+2) :
            new_lst.append(list(lst))

        for y in range(k+2) :
            for x in range(k+2) :
                if y == 0 or y == k + 1 :
                    new_lst[y][x] = -1
                elif x == 0 or x == k + 1 :
                    new_lst[y][x] = -1

        t = 1
        x = 1
        y = 1

        while 1 :
            if new_lst[y][x] == -1 :
                pass
            else :
                # 위쪽확인(오른쪽으로)
                while 1 :
                    if new_lst[y-1][x] != 0 :
                        new_lst[y][x] = t
                        t += 1
                        x += 1
                    if new_lst[y][x+1] != 0 :
                        break
                if t == (k ** 2) + 1:
                    break
                    # 오른쪽확인(아래쪽으로)
                while 1:
                    if new_lst[y][x+1] != 0 :
                        new_lst[y][x] = t
                        t += 1
                        y += 1
                    if new_lst[y+1][x] != 0 :
                        break
                if t == (k ** 2) + 1:
                    break
                    # 아래쪽확인(왼쪽으로)
                while 1:
                    if new_lst[y+1][x] != 0 :
                        new_lst[y][x] = t
                        t += 1
                        x -= 1
                    if new_lst[y][x-1] != 0 :
                        break
                if t == (k ** 2) + 1:
                    break
                    # 왼쪽확인(위쪽으로)
                while 1:
                    if new_lst[y][x-1] != 0 :
                        new_lst[y][x] = t
                    y -= 1
                    t += 1
                    if new_lst[y - 1][x] != 0:
                        break
                if t == (k ** 2) + 1:
                    break
        w = 0
        for lst_value in new_lst :
            if w == 0 or w == k + 1 :
                pass
            else :
                lst_value.remove(-1)
                lst_value.remove(-1)
            w += 1

        del new_lst[0]
        del new_lst[k]

        print('#{}'.format(q + 1))
        for lst_value in new_lst :
            print_str = ''
            for value in lst_value :
                print_str = print_str + str(value) + ' '
            print(print_str)
```

# 4. Sum

```
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.



[제약 사항]

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
```

```
for cnt in range(10) :

    t = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)] # N 개의 1차원 리스트가 만들어짐

    sum_x_list = []
    sum_y_list = []

    for sum_y in lst :
        sum_y_tmp = 0
        for y in sum_y :
            sum_y_tmp += y
        sum_y_list.append(sum_y_tmp)

    for x_position in range(100) :
        sum_x_tmp = 0
        for y_position in range(100) :
            sum_x_tmp += lst[y_position][x_position]
        sum_x_list.append(sum_x_tmp)

    x_max = 0
    y_max = 0

    for x_sum_value in sum_x_list :
        if x_max < x_sum_value :
            x_max = x_sum_value

    for y_sum_value in sum_y_list :
        if y_max < y_sum_value :
            y_max = y_sum_value

    max_of_max = 0

    if x_max > y_max :
        max_of_max = x_max
    else :
        max_of_max = y_max

    print('#{} {}'.format(cnt + 1, max_of_max))
```

