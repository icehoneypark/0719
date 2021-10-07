# 1. subtree

```
입력
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10

출력
#1 3
#2 1
#3 3
```

```python
def cnt(now):
    if now == -1:
        return
    global rst
    rst += 1
    cnt(left[now])
    cnt(right[now])
 
 
t = int(input())
 
for cnt_t in range(1, t+1):
    rst = 0
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
 
    left = [-1 for _ in range(e+2)]
    right = [-1 for _ in range(e+2)]
 
    for tmp in range(e):
        if left[lst[tmp*2]] == -1:
            left[lst[tmp*2]] = lst[tmp*2+1]
        else:
            right[lst[tmp*2]] = lst[tmp*2+1]
 
    cnt(n)
 
    print('#{} {}'.format(cnt_t, rst))
```



# 2. 이진탐색

```
입력
3
6
8
15

출력
#1 4 6
#2 5 2
#3 8 14
```

```python
def tree(now):
    global n
    global num
    if now > n:
        return
    tree(now*2)
    lst[now] = num
    num += 1
    tree(now*2+1)


t = int(input())
for cnt_t in range(1, t+1):
    n = int(input())
    num = 1
    lst = [-1 for _ in range(n+1)]

    tree(1)

    print('#{} {} {}'.format(cnt_t, lst[1], lst[n // 2]))
```



# 3. 이진힙

```
입력
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

출력
#1 7
#2 5
#3 65
```

```python
def set(now):
    if now <= 1:
        return
    elif tree[now] < tree[now//2]:
        tree[now], tree[now//2] = tree[now//2], tree[now]
        set(now//2)



t = int(input())

for cnt_t in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    tree = [0]
    for tmp in lst:
        tree.append(tmp)
        set(len(tree) - 1)

    # for tmp in range(len(tree) - 1, 0, -1):
    #     if tree[tmp] < tree[tmp//2]:
    #         set(tmp)

    result = 0
    start = len(tree) - 1
    while start:
        start //= 2
        result += tree[start]

    print('#{} {}'.format(cnt_t, result))

```



# 4. 노드의 합

```
입력
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962

출력
#1 3
#2 845
#3 1801
```

```python
def set(now):
    if now == 0:
        return
    if now*2 > n:
        return
    elif now*2 + 1 > n:
        lst[now] = lst[now*2]
    else:
        lst[now] = lst[now*2] + lst[now * 2 + 1]
    set(now - 1)


t = int(input())
for cnt_t in range(1, t+1):
    n, m, l = map(int, input().split())
    lst = [-1 for _ in range(n+1)]
    for _ in range(m):
        key, data = map(int, input().split())
        lst[key] = data

    for tmp in range(len(lst)):
        if lst[tmp] != -1:
            last = tmp - 1
            break

    set(last)

    print('#{} {}'.format(cnt_t, lst[l]))

```



# 5. 사칙연산

```python
t = 10

for cnt_t in range(1, t+1):
    n = int(input())
    tree = [-1] * (n+1)
    for _ in range(n):
        tmp = list(input().split())
        if tmp[1].isdigit():
            tree[int(tmp[0])] = int(tmp[1])
        else:
            tmp_lst = list()
            tmp_lst.append(tmp[1])
            tmp_lst.append(int(tmp[2]))
            tmp_lst.append(int(tmp[3]))
            tree[int(tmp[0])] = tmp_lst

    for i in range(len(tree) - 1, 0, -1):
        if type(tree[i]) == list:
            if tree[i][0] == '+':
                tree[i] = tree[tree[i][1]] + tree[tree[i][2]]
            elif tree[i][0] == '-':
                tree[i] = tree[tree[i][1]] - tree[tree[i][2]]
            elif tree[i][0] == '*':
                tree[i] = tree[tree[i][1]] * tree[tree[i][2]]
            elif tree[i][0] == '/':
                tree[i] = tree[tree[i][1]] / tree[tree[i][2]]

    print('#{} {}'.format(cnt_t, int(tree[i])))

```

