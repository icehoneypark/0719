# 1. 미로1

```
아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

아래의 예시에서는 도달 가능하다.
 

  

아래의 예시에서는 출발점이 (1, 1)이고, 도착점이 (11, 11)이며 도달이 불가능하다.


[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).
```

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
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.

주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.


   

 
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.

E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.

```

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
N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.

1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.

주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.





- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.

3<=N<=20, N<=M<=100, 1<=Ci<=20

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

```

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
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

```

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
첫 줄에는 이진트리의 정점의 총 수 V가 주어진다. 1 <= V <= 15

정점들은 1 ~ V의 번호를 갖는다.

그 다음 줄부터 V-1개의 줄에 걸쳐 간선에 대한 정보가 나열된다.

간선은 그것을 이루는 두 정점으로 표기된다.

간선은 항상 “부모 자식” 순서로 표기된다.

간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다. 

입력받은 이진트리를 전위 순회하여 정점의 번호를 출력하는 프로그램을 작성하시오.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다. 1 <= T <= 10

다음 줄부터 테스트 케이스 별로 이진트리에 대한 정보가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

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
다음은 특정 단어(또는 문장)를 트리 형태로 구성한 것으로, in-order 형식으로 순회하여 각 노드를 읽으면 원래 단어를 알 수 있다고 한다.
 


 
위 트리를 in-order 형식으로 순회할 경우 SOFTWARE 라는 단어를 읽을 수 있다.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.

총 노드의 개수는 100개를 넘어가지 않는다.

트리는 완전 이진 트리 형식으로 주어지며, 노드당 하나의 알파벳만 저장할 수 있다.

노드가 주어지는 순서는 아래 그림과 같은 숫자 번호대로 주어진다.
 


[입력]

각 테스트 케이스의 첫 줄에는 각 케이스의 트리가 갖는 정점의 총 수 N(1≤N≤100)이 주어진다. 그 다음 N줄에 걸쳐 각각의 정점 정보가 주어진다.

해당 정점에 대한 정보는 해당 정점의 알파벳, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호가 차례대로 주어진다.

정점번호는 1부터 N까지의 정수로 구분된다. 입력에서 정점 번호를 매기는 규칙은 위와 같으며, 루트 정점의 번호는 반드시 1이다.

입력에서 이웃한 알파벳이나 자식 정점의 번호는 모두 공백으로 구분된다.

위의 예시에서, 알파벳 S가 7번 정점에 해당하면 “7 S”으로 주어지고, 알파벳 ‘F’가 2번 정점에 해당하면 두 자식이 각각 알파벳 ‘O’인 4번 정점과 알파벳 ‘T’인 5번 정점이므로 “2 F 4 5”로 주어진다.

총 10개의 테스트 케이스가 주어진다,

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
```

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

