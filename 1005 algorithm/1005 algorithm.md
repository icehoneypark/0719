# 1. 부분수열의 합

```
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
```

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
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

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
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89 


이 경우 최소 소비량은 89가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

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
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.

트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.

이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.

화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고, 다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.

1<=N, M<=100, 1<=wi, ti<=50
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

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
24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.

0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고, 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 신청서 N이 주어지고, 다음 줄부터 N개의 줄에 걸쳐 화물차의 작업 시작 시간 s와 종료 시간 e가 주어진다.

1<=N<=100, 0<=s<24, 0 ＜ e ＜= 24 


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

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
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 각 줄에 0에서 9사이인 12개의 숫자가 주어진다.
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

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

