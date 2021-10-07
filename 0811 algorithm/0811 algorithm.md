# 1. 부분집합 합

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

