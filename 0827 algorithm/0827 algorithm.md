# 1. 미로1

```
from collections import deque

def mazeescape(level):
    global result
    for _ in range(len(next_co)):
        start_co.append(next_co.popleft())


    for _ in range(len(start_co)):
        start_co_data = start_co.popleft()
        y = start_co_data[0]
        x = start_co_data[1]
        for tmp in range(4):
            y_new = y + dy[tmp]
            x_new = x + dx[tmp]
            if 0 <= y_new < 16 and 0 <= x_new < 16:
                if maze[y_new][x_new] == 0:
                    maze[y_new][x_new] = 2
                    next_co.append([y_new, x_new])
                    mazeescape(level+1)
                elif maze[y_new][x_new] == 3:
                    result = 1
                    break


t = 10

for cnt_t in range(1, t+1):

    tsh = int(input())

    maze = list()

    for _ in range(16):
        maze.append(list(map(int, (input()))))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]


    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                y_start = y
                x_start = x

    level = 0

    start_co = deque()
    next_co = deque()

    next_co.append([y_start, x_start])

    result = 0

    mazeescape(level)

    print('#{} {}'.format(cnt_t, result))

```

 # 2. 노드의 거리

```
입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

출력
#1 2
#2 4
#3 3
```

```
from collections import deque


def traveling(level):
    global goal, result
    state = 0
    for _ in range(len(next_lst)):
        start_lst.append(next_lst.popleft())

    for _ in range(len(start_lst)):
        node = start_lst.popleft()
        for next in range(1, v+1):
            if lst[node][next] == 1 and visited_lst[next] == 0:
                if next == goal:
                    result = level
                next_lst.append(next)
                visited_lst[next] = 1
                state = 1

    if state:
            traveling(level+1)





t = int(input())

for cnt_t in range(1, t+1):

    result = 0

    v, e = map(int, input().split())

    lst = [
        [0 for _ in range(v+1)] for _ in range(v+1)
    ]

    line_lst = list()
    for _ in range(e):
        line_lst.append(list(map(int, input().split())))

    for data in line_lst:
        lst[data[0]][data[1]] = 1
        lst[data[1]][data[0]] = 1

    start, goal = map(int, input().split())

    start_lst = deque()

    visited_lst = [0 for _ in range(v+1)]

    next_lst = deque()

    next_lst.append(start)

    level = 1

    traveling(level)

    print('#{} {}'.format(cnt_t, result))
```

# 3. 피자 굽기

```
입력
3
3 5 
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

출력
#1 4
#2 8
#3 6
```

```
from collections import deque

t = int(input())

for cnt_t in range(1, t+1):

    n, m = map(int, input().split())

    lst = list(map(int, input().split()))

    fire_pit = deque()
    pizza_num_lst = deque()

    for idx in range(n):
        fire_pit.append(lst[idx])
        pizza_num_lst.append(idx)

    pizza_num = len(pizza_num_lst) - 1
    cnt = 1
    while cnt:
        state = 1
        while state:
            state = fire_pit.popleft()
            state //= 2
            if state != 0:
                fire_pit.append(state)
                pizza_num_lst.append(pizza_num_lst.popleft())
            else:
                pizza_num_lst.popleft()
                if len(fire_pit) == 1:
                    cnt = 0
                    break
                if pizza_num < len(lst) - 1:
                     pizza_num += 1
                     fire_pit.append(lst[pizza_num])
                     pizza_num_lst.append(pizza_num)

    print('#{} {}'.format(cnt_t, pizza_num_lst[0]+1))
```

# 4. 미로의 거리

```
입력
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

출력
#1 5
#2 5
#3 0
```

```
from collections import deque

def escaping(level):
    state = 0
    global find_result
    for _ in range(len(next_queue)):
        start_queue.append(next_queue.popleft())

    for _ in range(len(start_queue)):
        start = start_queue.popleft()
        for cnt in range(4):

            new_y = start[0] + dy[cnt]
            new_x = start[1] + dx[cnt]

            if 0 <= new_y < n and 0 <= new_x < n:
                if map[new_y][new_x] == 0:
                    map[new_y][new_x] = 2
                    next_queue.append([new_y, new_x])
                    state = 1
                elif map[new_y][new_x] == 3:
                    find_result = level
                    return
                else:
                    pass
    if state:
        escaping(level + 1)

    # if start_queue == deque() and next_queue == deque():
    #     if find_result != 0: continue

t = int(input())

for cnt_t in range(1, t+1):
    n = int(input())

    map = list()

    for _ in range(n):
        map.append(list(input()))

    for y in range(len(map)):
        for x in range(len(map[y])):
            map[y][x] = int(map[y][x])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    start_queue = deque()

    next_queue = deque()

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 2:
                next_queue.append([y, x])

    level = 0

    find_result = level

    escaping(level)

    print('#{} {}'.format(cnt_t, find_result))

```

# 5. 이진 트리 전위 순회

```
입력
1
13
1 2
1 3
2 4
3 5
3 6
4 7
5 8
5 9
6 10
6 11
7 12
11 13

출력
#1 1 2 4 7 12 3 5 8 9 6 10 11 13
```

```
def tree(parent):
    print(parent, end = ' ')
    if left_list[parent] != 0:
        tree(left_list[parent])
    if right_list[parent] != 0:
        tree(right_list[parent])

t = int(input())

for cnt_t in range(1, t+1):
    v = int(input())

    left_list = [0 for _ in range(v+1)]
    right_list = [0 for _ in range(v+1)]

    for _ in range(v-1):
        parent, son = map(int, input().split())
        if left_list[parent] == 0:
            left_list[parent] = son
        else:
            right_list[parent] = son

    print('#{}'.format(cnt_t), end=' ')

    tree(1)

    print()
```

# 6. 중위순회

```
def inorder(parent):
    if left[parent] != 0:
        inorder(left[parent])
    inorder_list.append(parent)
    if right[parent] != 0:
        inorder(right[parent])
    return


t = 10

for cnt_t in range(1, t + 1):
    n = int(input())

    input_data = list()

    for _ in range(n):
        input_data.append(list(input().split()))

    left = [0] * (n + 1)
    right = [0] * (n + 1)

    key_data = [0] * (n + 1)

    for data in input_data:
        if len(data) == 4:
            key_data[int(data[0])] = data[1]
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])
        elif len(data) == 3:
            key_data[int(data[0])] = data[1]
            left[int(data[0])] = int(data[2])
        else:
            key_data[int(data[0])] = data[1]
    root = 1

    inorder_list = list()

    inorder(root)

    result_str = ''

    for inorder_data in inorder_list:
        result_str += key_data[inorder_data]

    print('#{} {}'.format(cnt_t, result_str))

```

