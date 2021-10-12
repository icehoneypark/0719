# 1. 벽돌 깨기

```python
import copy

def arrange(copy_data):
    global n, w, h

    for x in range(w):
        pos = h - 1
        for y in range(h - 1, -1, -1):
            if copy_data[y][x] > 0:
                copy_data[pos][x], copy_data[y][x] = copy_data[y][x], copy_data[pos][x]
                pos -= 1

    return copy_data


def break_block(y, x, copy_data):
    global n, w, h

    if 0 <= y < h and 0 <= x < w:
        if copy_data[y][x] == 1:
            copy_data[y][x] = 0

        else:
            length = copy_data[y][x]
            copy_data[y][x] = 0
            for up in range(1, length):
                break_block(y - up, x, copy_data)
            for down in range(1, length):
                break_block(y + down, x, copy_data)
            for left in range(1, length):
                break_block(y, x - left, copy_data)
            for right in range(1, length):
                break_block(y, x + right, copy_data)

    return copy_data

def pin(x):

    global n, w, h

    for y in range(h):
        if old_lst_data[y][x] > 0:
            copy_data = copy.deepcopy(old_lst_data)
            new_lst.append(arrange(break_block(y, x, copy_data)))
            return
    tmp_lst = list()

    for y in range(h):
        tmp_lst.append([0] * w)
        
    if old_lst_data == tmp_lst:
        new_lst.append(tmp_lst)


t = int(input())

for cnt_t in range(1, t + 1):
    lst = list()

    n, w, h = map(int, input().split())

    # dy = [-1, 1, 0, 0]
    # dx = [0, 0, -1, 1]
    for _ in range(h):
        lst.append(list(map(int, input().split())))

    old_lst = list()

    new_lst = list()

    new_lst.append(lst)


    de = -1

    for _ in range(n):
        old_lst = copy.deepcopy(new_lst)
        new_lst.clear()
        de = -1
        for old_lst_data in old_lst:
            for x in range(w):
                pin(x)

    de = -1

    min_cnt = 21e8
    for new_lst_data in new_lst:
        sum_num = 0
        for y in range(h):
            for x in range(w):
                if new_lst_data[y][x] > 0:
                    sum_num += 1
        if min_cnt > sum_num:
            min_cnt = sum_num

    print('#{} {}'.format(cnt_t, min_cnt))

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



