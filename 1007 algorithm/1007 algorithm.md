# 1. 트리 순회

```
예제 입력
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

예제 출력
ABDCEFG
DBAECFG
DBEGFCA
```

```python
def finder(node):
    global finder1
    global finder2
    global finder3
    if node =='.':
        return
    finder1 += node
    finder(left_lst[parents.index(node)])
    finder2 += node
    finder(right_lst[parents.index(node)])
    finder3 += node


n = int(input())

parents = list()
left_lst = list()
right_lst = list()

finder1 = ''
finder2 = ''
finder3 = ''

for _ in range(n):
    tmp1, tmp2, tmp3 = input().split()
    parents.append(tmp1)
    left_lst.append(tmp2)
    right_lst.append(tmp3)

finder(parents[0])

print(finder1)
print(finder2)
print(finder3)
```



# 2. 최소 생산 비용

```
입력
3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4
sample_input(11).txt
출력
#1 63
#2 78
#3 129
```

```python
def checking(level):
    global n
    global price
    global min_price
    if level == n:
        if min_price > price:
            min_price = price
        pass
    for tmp in range(n):
        if visited[tmp] == 0:
            if price + price_lst[level][tmp] < min_price:
                price += price_lst[level][tmp]
                visited[tmp] = 1
                checking(level + 1)
                visited[tmp] = 0
                price -= price_lst[level][tmp]


t = int(input())

for cnt_t in range(1, t + 1):
    min_price = 20e8
    price = 0

    n = int(input())

    price_lst = list()

    for _ in range(n):
        price_lst.append(list(map(int, input().split())))

    visited = [0]*n

    checking(0)

    print('#{} {}'.format(cnt_t, min_price))
```



# 3. 전기버스 2

```
입력
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

출력
#1 1
#2 2
#3 5
```

```python
def charging(level):
    global battery
    global position
    global time_cnt



    for battery_potion in range(battery, 0, -1):
        position += battery_potion

        if position >= bus_charge[0]:
            if time_cnt > level:
                time_cnt = level
            position -= battery_potion
            return


        else:
            if level >= time_cnt:
                position -= battery_potion
                return
            battery = bus_charge[position]
            charging(level + 1)
            position -= battery_potion




t = int(input())

for cnt_t in range(1, t + 1):

    bus_charge = list(map(int, input().split()))

    battery = bus_charge[1]

    position = 1

    time_cnt = 20e8

    charging(0)

    print('#{} {}'.format(cnt_t, time_cnt))
```



# 4. 이진 탐색

```
입력
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5

출력
#1 2
#2 0
#3 3
```

```
def check(l, r, b_data):
    global cnt
    global flat
    m = (l + r) // 2
    if a[m] == b_data:
        cnt += 1
        return
    elif a[m] > b_data:
        if flat == 0 or flat == "RIGHT":
            flat = "LEFT"
            check(l, m - 1, b_data)
        else:
            return
    else:
        if flat == 0 or flat == "LEFT":
            flat = "RIGHT"
            check(m + 1, r, b_data)
        else:
            return


t = int(input())

for cnt_t in range(1, t + 1):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))

    l = 0
    r = len(a) - 1


    cnt = 0

    check_lst = list()

    for b_data in b:
        if b_data in a:
            flat = 0
            check(l, r, b_data)

    print('#{} {}'.format(cnt_t, cnt))
```

# 5. 퀵 정렬

```
입력
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

출력
#1 2
#2 6
```

```python
def sort(s, e):
    i = s + 1
    j = e

    pivot_index = s

    while i <= j:
        while i <= j and lst[pivot_index] >= lst[i]:
            i += 1
        while i <= j and lst[pivot_index] <= lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[pivot_index], lst[j] = lst[j], lst[pivot_index]

    return j

def quick_sort(s, e):

    if s > e:
        return

    pivot_index = sort(s, e)

    quick_sort(s, pivot_index - 1)
    quick_sort(pivot_index + 1, e)


t = int(input())

for cnt_t in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    s = 0
    e = len(lst) - 1
    quick_sort(s, e)

    print('#{} {}'.format(cnt_t, lst[n//2]))
```

# 6. N-Queen 

```
입력
2
1
2

출력
#1 1
#2 0
```

```python
def chess(level):
    global n, cnt

    if level == n:
        cnt += 1
        return

    for position in range(n):
        state = 1
        for x in range(position):
            if lst[level][x] != 0:
                state = 0
        if state:
            for y in range(level):
                if lst[y][position] != 0:
                    state = 0
        if state:
            tmp_cnt = 1
            if position - tmp_cnt >= 0 and level - tmp_cnt >= 0:
                while position - tmp_cnt >= 0 and level - tmp_cnt >= 0:
                    if lst[level-tmp_cnt][position-tmp_cnt] != 0:
                        state = 0
                        break
                    tmp_cnt += 1
        if state:
            tmp_cnt = 1
            if level - tmp_cnt >= 0 and position + tmp_cnt < n:
                while position + tmp_cnt < n and level - tmp_cnt >= 0:
                    if lst[level - tmp_cnt][position+tmp_cnt] != 0:
                        state = 0
                        break
                    tmp_cnt += 1
        if state:
            lst[level][position] = 1
            chess(level + 1)
            lst[level][position] = 0


t = int(input())


for cnt_t in range(1, t + 1):
    n = int(input())
    cnt = 0

    lst = list()
    for _ in range(n):
        lst.append([0] * n)

    chess(0)

    print('#{} {}'.format(cnt_t, cnt))
```



# 7. 동철이의 일 분배

```
입력
1
3
13 0 50
12 70 90
25 60 100
 
출력
#1 9.100000
```

```python
def check(level):
    global n
    global save_per
    global tmp_per

    if level == n:
        if save_per < tmp_per:
            save_per = tmp_per
        return

    for tmp in range(n):
        if visited[tmp] == 0:
            if per[level][tmp] == 0:
                pass
            else:
                tmp_per *= (per[level][tmp] * 0.01)
                if save_per < tmp_per:
                    visited[tmp] = 1
                    check(level + 1)
                    visited[tmp] = 0
                tmp_per /= (per[level][tmp] * 0.01)

    return

t = int(input())

for cnt_t in range(1, t+1):
    n = int(input())

    per = list()

    for _ in range(n):
        per.append(list(map(int, input().split())))

    visited = [0] * n

    save_per = 0

    tmp_per = 1

    check(0)

    max_per = save_per * 100

    print('#{} {:6f}'.format(cnt_t, max_per))
```

