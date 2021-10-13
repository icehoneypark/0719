# 1. ugly number

```
입력
5
3
1 9 10
1
100
10
47 1152 505 955 444 1349 1441 1416 70 991
10
91 73 51 9 62 41 51 58 78 79
10
26 11 16 25 22 23 16 29 9 10

출력
#1 1 10 12
#2 1536
#3 216 131220000 984150 38400000 512000 398131200 637729200 566231040 576 48828125
#4 1200 640 250 10 405 150 250 360 750 768
#5 60 15 25 54 45 48 25 75 10 12
```

```python
def ugly_num(num):
    if num > int(21e8):
        return
    for tmp in ugly:
        num *= tmp
        if num in ugly_num_lst:
            pass
        else:
            ugly_num_lst.append(num)
            ugly_num(num)
        num //= tmp


t = int(input())

for cnt_t in range(1, t + 1):
    n = int(input())
    input_lst = list(map(int, input().split()))

    ugly = [2, 3, 5]

    ugly_num_lst = [0, 1]

    ugly_num(1)

    ugly_num_lst.sort()

    result = list()

    for data in input_lst:
        result.append(ugly_num_lst[data])

    # print(ugly_num_lst)
    print('#{} '.format(cnt_t), end='')
    print(*result)
```



# 2. 최장 경로

```
입력
2
1 0
3 2
1 2
3 2

출력
#1 1
#2 3
```

```python
def check(num):
    global n, cnt, max_length
    visited[num] = 1
    for tmp in range(1, n + 1):
        if connect_lst[num][tmp] == 1 and visited[tmp] == 0:
            cnt += 1
            if max_length < cnt:
                max_length = cnt
            check(tmp)
            visited[tmp] = 0
            cnt -= 1


t = int(input())

for cnt_t in range(1, t + 1):
    n, m = map(int, input().split())

    lst = list()

    connect_lst = list()

    if n == 1:
        max_length = 1

    for _ in range(n + 1):
        connect_lst.append([0] * (n + 1))


    for _ in range(m):
        num1, num2 = map(int, input().split())
        connect_lst[num1][num2] = 1
        connect_lst[num2][num1] = 1

    max_length = 0

    for num in range(1, n + 1):
        visited = [0] * (n + 1)
        cnt = 1
        check(num)

    if n == 1:
        max_length = 1

    print('#{} {}'.format(cnt_t, max_length))

```

