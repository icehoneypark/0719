# 1. 반복문자 지우기

```
입력
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

출력
#1 1
#2 4
#3 11
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    problem = list(input())
    state = 1
    while state :
        cnt = 0
        if len(problem) >= 2 :
            for cnt_p in range(len(problem)-1) :
                if problem[cnt_p] == problem[cnt_p+1] :
                    del problem[cnt_p]
                    del problem[cnt_p]
                    cnt = 1
                    break
                if cnt_p == len(problem) - 2 :
                    state = 0
        else :
            state = 0
    print('#{} {}'.format(cnt_t, len(list(problem))))
```

# 2. 그래프 경로

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
2 5
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
#1 1
#2 1
#3 1
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    v, e = map(int, input().split())

    adj = [
        [0 for _ in range(v+1)] for _ in range(v+1)
    ]
    for _ in range(e) :
        y, x = map(int, input().split())
        adj[y][x] = 1

    def dfs(now):
        global find
        global destination
        # 자식노드 찾기
        for next in range(v+1):
            if adj[now][next] == 1 and visited[next] == 0:  # 연결? 방문안함?
                visited[next] = 1  # 다시 재귀호출 방지
                if next == destination :
                    find = 1
                    break
                dfs(next)
        return

    parent, destination = map(int, input().split())
    find = 0
    visited = [0]*(v+1)
    visited[0] = 1  # 시작노드 0번 방문체크 (이후의 재귀호출에서 다시 재귀호출 방지가능)
    dfs(parent)
    print('#{} {}'.format(cnt_t, find))


    def dfs(now):
        for next in range(4):
            if adj[now][next] == 1 and visited[next] == 0:  # 연결? 방문안함?
                visited[next] = 1  # 다시 재귀호출 방지
                dfs(next)

        return
```

# 3. 괄호 검사

```
입력
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

출력
#1 1
#2 1
#3 0
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    problem = list(input())
    lst = [0]
    ret = 0
    for val in problem :
        if val == '{' :
            lst.append(val)
        elif val == '}' :
            if lst.pop() == '{':
                pass
            else :
                ret = 0
                lst.append('error')
                break
        elif val == '(' :
            lst.append(val)
        elif val == ')' :
            if lst.pop() == '(' :
                pass
            else :
                ret = 0
                lst.append('error')
                break
    if lst == [0] :
        ret = 1
    print('#{} {}'.format(cnt_t, ret))
```

# 4. 종이붙이기

```
입력
3
30
50
70

출력
#1 5
#2 21
#3 85
```

```
def box_cnt(w) :
    if w == 10 :
        return 1
    elif w == 20 :
        return 3
    else :
        return box_cnt(w-10) + box_cnt(w-20)*2

t = int(input())
for cnt_t in range(1, t+1) :
    n = int(input())
    print('#{} {}'.format(cnt_t, box_cnt(n)))
```

# 5. 비밀번호

```
t = 10
for cnt_t in range(1, t+1) :
    tsh, problem = input().split()
    problem = list(problem)
    state = 1
    while state :
        cnt = 0
        if len(problem) >= 2 :
            for cnt_p in range(len(problem)-1) :
                if problem[cnt_p] == problem[cnt_p+1] :
                    del problem[cnt_p]
                    del problem[cnt_p]
                    cnt = 1
                    break
                if cnt_p == len(problem) - 2 :
                    state = 0
        else :
            state = 0
    ret = ''
    for dat in problem :
        ret += str(dat)

    print('#{} {}'.format(cnt_t, ret))

    # ABCCB
    # NNNASBBSNV
    # UKJWHGGHNFTCRRCTWLALX
```

# 6. 길찾기

```
def search_line(start) :
    global ret
    if start == 99 :
        ret = 1
        return 0
    
    for destination in range(100) :
        if line_arr[start][destination] == 1 and check_list[destination] == 0:
            check_list[destination] = 1
            search_line(destination)
    return 0

# t = int(input())
t = 10
for cnt_t in range(1, t+1) :
    tsh, long = map(int, input().split())
    line = list(map(int,input().split()))
    line_arr = []
    for _ in range(100) :
        line_arr.append([0]*100)
    for idx in range(0, long*2, 2) :
        line_arr[line[idx]][line[idx+1]] = 1

    ret = 0

    check_list = [0] * 100

    check_list[0] = 1

    search_line(0)

    print('#{} {}'.format(cnt_t, ret))
```

