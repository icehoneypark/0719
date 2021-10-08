# 1. 정식이의 은행업무

```python
def two_chg_func(level):
    if level == len(two_num):
        return

    two_num_tmp = list(two_num)

    if two_num_tmp[level] == '1':
        two_num_tmp[level] = '0'
    else:
        two_num_tmp[level] = '1'

    two_num_str = ''
    for tmp in two_num_tmp:
        two_num_str += tmp

    two_num_chg[level] = two_num_str

    two_chg_func(level + 1)

def three_chg_func(level):

    if level == len(three_num):
        return

    three_num_tmp = list(three_num)

    if three_num_tmp[level] == '0':
        three_num_tmp[level] = '1'
        three_num_chg1[level] = list(three_num_tmp)
        three_num_tmp[level] = '2'
        three_num_chg2[level] = list(three_num_tmp)
    elif three_num_tmp[level] == '1':
        three_num_tmp[level] = '0'
        three_num_chg1[level] = list(three_num_tmp)
        three_num_tmp[level] = '2'
        three_num_chg2[level] = list(three_num_tmp)
    else:
        three_num_tmp[level] = '0'
        three_num_chg1[level] = list(three_num_tmp)
        three_num_tmp[level] = '1'
        three_num_chg2[level] = list(three_num_tmp)

    three_num_str1 = ''
    for tmp in three_num_chg1[level]:
        three_num_str1 += tmp

    three_num_chg1[level] = three_num_str1

    three_num_str2 = ''
    for tmp in three_num_chg2[level]:
        three_num_str2 += tmp

    three_num_chg2[level] = three_num_str2

    three_chg_func(level + 1)


def cal_two_num(level):

    if level == len(two_num):
        return

    two_num_chg[level] = int(two_num_chg[level], 2)

    cal_two_num(level + 1)


def cal_three_num(level):

    if level == len(three_num):
        return

    three_num_chg1[level] = int(three_num_chg1[level], 3)

    three_num_chg2[level] = int(three_num_chg2[level], 3)

    cal_three_num(level + 1)

t = int(input())

for cnt_t in range(1, t+1):
    two_num = input()
    three_num = input()

    two_num_chg = [''] * len(two_num)
    three_num_chg1 = [''] * len(three_num)
    three_num_chg2 = [''] * len(three_num)

    two_chg_func(0)
    three_chg_func(0)

    cal_two_num(0)
    cal_three_num(0)

    for two_num_data in two_num_chg:
        if two_num_data in three_num_chg1:
            print('#{} {}'.format(cnt_t, two_num_data))
            break
        elif two_num_data in three_num_chg2:
            print('#{} {}'.format(cnt_t, two_num_data))
            break
```



# 2. 격자판의 숫자 이어 붙이기

```python
def check(x, y, level):

    for tmp in range(4):
        nx = x + dx[tmp]
        ny = y + dy[tmp]
        if 0 <= nx < 4 and 0 <= ny < 4:
            state = 1

            result_tmp[level] = map_lst[ny][nx]
            if level == 6:
                comb()
            else:
                check(nx, ny, level + 1)


def comb():
    re_tmp = ''
    for data in result_tmp:
        re_tmp += data
    result_lst.append(re_tmp)

t = int(input())

for cnt_t in range(1, t+1):
    n = 4
    map_lst = list()
    for _ in range(n):
        map_lst.append(list(input().split()))

    # level1 = list()
    # level2 = list()
    # level3 = list()
    # level4 = list()
    # level5 = list()

    result_lst = list()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for y in range(n):
        for x in range(n):
            result_tmp = [''] * 7
            
            result_tmp[0] = map_lst[y][x]
            check(x, y, 1)
    # print(result_lst)
    # print('#{} {}'.format(cnt_t, len(result_lst)))
    result_lst = set(result_lst)
    # print(result_lst)
    print('#{} {}'.format(cnt_t, len(result_lst)))
```



# 3. 쉬운 거스름돈

```python
def remain(level, remainder):
    if remainder == 0:
        return

    if level == 0:
        tmp = remainder // 50000
        lst[level] = tmp
        remain(level + 1, remainder % 50000)
    elif level == 1:
        tmp = remainder // 10000
        lst[level] = tmp
        remain(level + 1, remainder % 10000)
    elif level == 2:
        tmp = remainder // 5000
        lst[level] = tmp
        remain(level + 1, remainder % 5000)
    elif level == 3:
        tmp = remainder // 1000
        lst[level] = tmp
        remain(level + 1, remainder % 1000)
    elif level == 4:
        tmp = remainder // 500
        lst[level] = tmp
        remain(level + 1, remainder % 500)
    elif level == 5:
        tmp = remainder // 100
        lst[level] = tmp
        remain(level + 1, remainder % 100)
    elif level == 6:
        tmp = remainder // 50
        lst[level] = tmp
        remain(level + 1, remainder % 50)
    elif level == 7:
        tmp = remainder // 10
        lst[level] = tmp
        remain(level + 1, remainder % 10)


t = int(input())

for cnt_t in range(1, t+1):

    remainder = int(input())

    lst = [0] * 8

    remain(0, remainder)

    print('#{} '.format(cnt_t))
    print(*lst)
```



# 4. 정사각형 방

```python
def room(y, x, level):
    global max_num, position, start_y, start_x
    if start_lst[lst[y][x]] < lst[start_y][start_x]:
        return
    else:
        start_lst[lst[y][x]] = lst[start_y][start_x]
    cnt = 0
    for tmp in range(4):
        ny = y + dy[tmp]
        nx = x + dx[tmp]
        if 0 <= ny < n and 0 <= nx < n:
            # 갈 방이 현 위치 + 1 일 경우
            if lst[y][x] + 1 == lst[ny][nx]:
                room(ny, nx, level + 1)
            # 갈 방의 값이 +1 이 아닐 경우
            else:
                cnt += 1
        # 갈 위치의 방이 없을 경우
        else:
            cnt += 1

        # 상하좌우 갈 곳이 없을 때
        if cnt == 4:
            # 움직인 방이 최대일 경우
            if max_num <= level:
                max_num = level
                # 움직인 방이 최대일 때, 시작점의 값이 작을 경우
                if position[max_num] > lst[start_y][start_x]:
                    position[max_num] = lst[start_y][start_x]



t = int(input())

for cnt_t in range(1, t + 1):
    n = int(input())

    lst = list()

    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for _ in range(n):
        lst.append(list(map(int, input().split())))



    # 움직인 칸 최대숫자
    max_num = 0
    # max_num이 최대일 때, 시작한 방의 값의 최소값
    position = [21e8] * (n ** 2 + 1)
    start_lst = [21e8] * (n ** 2 + 1)
    for y in range(n):
        for x in range(n):
            de = -1
            # 시작위치 저장
            start_y = y
            start_x = x
            room(y, x, 1)

    print('#{} {} {}'.format(cnt_t, position[max_num], max_num))
```



# 5. 장훈이의 높은 선반

```python
# def find_tall():
#     for tmp in range(1, 2 ** len(lst)):
#         for x in range(len(lst)):
#             if tmp & (1 << x):
#                 check[x] = 1
#         check_tall()
#
#         check = [0] * n
def check_tall():
    global n, b, min_sub
    sum_tall = 0
    for tmp in range(n):
        if check[tmp] == 1:
            sum_tall += lst[tmp]
            if sum_tall - b > min_sub:
                return
    if sum_tall >= b:
        min_sub = sum_tall - b

t = int(input())

for cnt_t in range(1, t + 1):

    n, b = map(int, input().split())

    lst = list(map(int, input().split()))

    check = [0] * n

    min_sub = 21e8

    # find_tall()
    for tmp in range(1, 2 ** len(lst)):
        for x in range(len(lst)):
            if tmp & (1 << x):
                check[x] = 1
        check_tall()

        check = [0] * n
    print("#{} {}".format(cnt_t, min_sub))
```



