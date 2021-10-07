# 1. 부분수열의 합

```
예제 입력 1 
5 0
-7 -3 -2 5 8

예제 출력 1 
1
```

```python
n, s = map(int, input().split())

lst = list(map(int, input().split()))

result_lst = list()

cnt = 0

for x in range(1, (1 << n)):
    lst_sum = 0
    for y in range(n):
        if x & (1 << y):
            lst_sum += lst[y]
    cnt += 1
    result_lst.append(lst_sum)

result_cnt = 0
for sum_sum in result_lst:
    if sum_sum == s:
        result_cnt += 1
print(result_cnt)
```



# 2. 최소합

```
입력
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

출력
#1 15
#2 18
#3 33
```

```python
def length(y, x):
    global sum

    if y == n:
        return
    elif x == n:
        return
    sum += lst[y][x]
    if y == n-1 & x == n-1:
        result_lst.append(sum)
        sum -= lst[y][x]
        return
    length(y + 1, x)
    length(y, x + 1)
    sum -= lst[y][x]

t = int(input())

for cnt_t in range(1, t + 1):
    sum = 0
    n = int(input())
    lst = list()
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    result_lst = list()
    length(0, 0)


    min_num = 20e18
    for result in result_lst:
        if min_num > result:
            min_num = result
    print('#{} {}'.format(cnt_t, min_num))
```



# 3. 전자카트

```
입력
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

출력
#1 89
#2 96
#3 139
```

```python
def check(y, level):
    global sum_data
    if level == n - 1:
        sum_data += lst[y][0]
        sum_data_lst.append(sum_data)
        sum_data -= lst[y][0]
        return
    for x in range(n):
        if visited[x] == 0:
            visited[x] = 1
            sum_data += lst[y][x]
            check(x, level + 1)
            sum_data -= lst[y][x]
            visited[x] = 0




t = int(input())

for cnt_t in range(1, t + 1):
    n = int(input())
    lst = list()
    sum_data_lst = list()
    for _ in range(n):
        lst.append(list(map(int, input().split())))

    visited = [0] * n
    visited[0] = 1
    sum_data = 0
    check(0, 0)

    min_num = 21e18

    for number in sum_data_lst:
        if min_num > number:
            min_num = number

    print('#{} {}'.format(cnt_t, min_num))
```



# 4. 컨테이너 운반

```
입력
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

출력
#1 8
#2 45
#3 84
```

```python
t = int(input())

for cnt_t in range(1, t + 1):
    n, m = map(int, input().split())

    w_lst = list(map(int, input().split()))
    mt_lst = list(map(int, input().split()))

    state = 1
    while state:
        state = 0
        for tmp in range(len(w_lst) - 1):
            if w_lst[tmp] > w_lst[tmp + 1]:
                w_lst[tmp], w_lst[tmp + 1] = w_lst[tmp + 1], w_lst[tmp]
                state = 1
    state = 1
    while state:
        state = 0
        for tmp in range(len(mt_lst) - 1):
            if mt_lst[tmp] > mt_lst[tmp + 1]:
                mt_lst[tmp], mt_lst[tmp + 1] = mt_lst[tmp + 1], mt_lst[tmp]
                state = 1


    mt_full_lst = [0] * len(mt_lst)
    sum_mt = 0
    for idx_w in range(len(w_lst) - 1, -1, -1):
        for idx_mt in range(len(mt_lst) - 1, -1, -1):
            if mt_lst[idx_mt] >= w_lst[idx_w]:
                if mt_full_lst[idx_mt] == 0:
                    mt_full_lst[idx_mt] = 1
                    sum_mt += w_lst[idx_w]
                    break
    print('#{} {}'.format(cnt_t, sum_mt))
```



# 5. 화물 도크

```
입력
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24

출력
#1 4
#2 4
#3 5
```

```python
def cmp(tup):
    return (tup[1], tup[0])

def truck(level):
    global cnt
    if level == n:
        result_lst.append(cnt)
        return
    data = data_lst[level]
    for tmp in range(data[0], data[1]):
        if used_lst[tmp] != 0:
            truck(level + 1)
            return
    for tmp in range(data[0], data[1]):
        used_lst[tmp] = 1
    cnt += 1
    truck(level + 1)
    for tmp in range(data[0], data[1]):
        used_lst[tmp] = 0
    cnt -= 1


t = int(input())

for cnt_t in range(1, t+1):

    used_lst = [0]*24

    n = int(input())

    data_lst = list()

    result_lst = list()

    for _ in range(n):
        data_lst.append(list(map(int, input().split())))

    cnt = 0

    data_lst.sort(key = cmp)

    truck(0)

    # print(data_lst)

    print('#{} {}'.format(cnt_t, result_lst[0]))
```

# 6. 베이비진 게임

```
입력
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3

출력
#1 0
#2 1
#3 2
```

```python
t = int(input())

for cnt_t in range(1, t + 1):

    lst = list(map(int, input().split()))

    check1 = [0] * 10
    check2 = [0] * 10

    winner = 0

    for cnt in range(len(lst)):
        if cnt % 2:
            check2[lst[cnt]] += 1
            for cnt2 in range(8):
                if check2[cnt2] > 0:
                    if check2[cnt2 + 1] > 0 and check2[cnt2 + 2] > 0:
                        winner = 2
                        break
            if winner:
                break
            for cnt2 in range(10):
                if check2[cnt2] == 3:
                    winner = 2
                    break
            if winner:
                break

        else:
            check1[lst[cnt]] += 1
            for cnt2 in range(8):
                if check1[cnt2] > 0:
                    if check1[cnt2 + 1] > 0 and check1[cnt2 + 2] > 0:
                        winner = 1
                        break
            if winner:
                    break
            for cnt2 in range(10):
                if check1[cnt2] == 3:
                    winner = 1
                    break
            if winner:
                break

    print("#{} {}".format(cnt_t, winner))
```

