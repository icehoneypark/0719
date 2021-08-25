# 1. 스도쿠 검증

```
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
 



같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
 


입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


[제약 사항]

1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    sudoku = []
    for _ in range(9) :
        sudoku.append(list(map(int, input().split())))

    result1 = []
    result2 = []
    result3 = []

    for y in range(9) :
        num_list = [0] * 9
        for x in range(9) :
            num_list[sudoku[y][x]-1] = 1
        if num_list == [1]*9 :
            result1.append(1)

    for x in range(9) :
        num_list = [0] * 9
        for y in range(9) :
            num_list[sudoku[y][x]-1] = 1
        if num_list == [1]*9 :
            result2.append(1)

    for x in range(9)[0:8:3] :
        for y in range(9)[0:8:3]:
            num_list = [0] * 9
            for x_plus in range(3) :
                for y_plus in range(3) :
                    num_list[sudoku[y+y_plus][x+x_plus] - 1] = 1
            if num_list == [1] * 9:
                result3.append(1)

    if result1 == result2 == result3 == [1]*9 :
        print('#{} 1'.format(cnt_t))
    else :
        print('#{} 0'.format(cnt_t))
```

# 2. 토너먼트 카드게임

```
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.
 

1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.

그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.

 


 
두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.

다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.

 



N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.


 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100

카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.
```

```
입력
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

출력
#1 3
#2 5
#3 1
```

```
def people(left, right):
    if left == right:
        return left
    mid = (left+right)//2
    human1 = people(left, mid)
    human2 = people(mid+1, right)
    result = battle(human1, human2)
    return result

def battle(a, b):
    if datas[a] == 1:
        if datas[b] == 1:
            return a
        elif datas[b] == 2:
            return b
        else:
            return a
    elif datas[a] == 2:
        if datas[b] == 1:
            return a
        elif datas[b] == 2:
            return a
        else:
            return b
    else:
        if datas[b] == 1:
            return b
        elif datas[b] == 2:
            return a
        else:
            return a









t = int(input())

for cnt_t in range(1, t+1):
    n = int(input())
    datas = list(map(int, input().split()))
    datas.insert(0, -1)
    winner = people(1, n)

    print('#{} {}'.format(cnt_t, winner))
```

# 3. 배열 최소 합

```
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
 

예를 들어 다음과 같이 배열이 주어진다.
 

2

1

2

5

8

5

7

2

2



이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.
```

```
입력
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
 

출력
#1 8
#2 14
#3 9
```

```
def mini(level):
    global min_sum
    global sum
    if level == n:
        if sum >= min_sum:
            pass
        else:
            min_sum = sum
        return
    for x in range(n):
        if checked[x] == 0:
            sum += datas[level][x]
            # if sum > min_sum:
            #     sum -= datas[level][x]
            #     return
            checked[x] = 1
            mini(level+1)
            checked[x] = 0
            sum -= datas[level][x]


t = int(input())

for cnt_t in range(1, t+1):
    n = int(input())
    checked = [0]*n
    datas = list()
    min_sum = 21e8
    sum = 0
    for _ in range(n):
        datas.append(list(map(int, input().split())))
    de=-1
    mini(0)
    print('#{} {}'.format(cnt_t, min_sum))
```

# 4. 미로

```
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.
 

다음은 5x5 미로의 예이다.
 

13101

10101

10101

10101

10021

 

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
 

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 1 또는 0으로 출력한다
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
#1 1
#2 1
#3 0
```

```
def miro(y, x):
    global result
    global master
    if result == 1 : return
    if miro_pan[y][x] == 1 : return
    elif miro_pan[y][x] == 3 :
        result = 1
        return
    else:
        miro_pan[y][x] = 2
        # print('_______')
        # for _ in miro_pan:
        #     print(_)
        # print('_______')
        # time.sleep(1)
        if y-1 >= 0 :
            if visited[y-1][x] == 0:
                visited[y - 1][x] = 1
                miro(y-1, x)
                visited[y - 1][x] = 0
        if y+1 <= n-1:
            if visited[y+1][x] == 0:
                visited[y+1][x] = 1
                miro(y + 1, x)
                visited[y+1][x] = 0
        if x-1 >= 0:
            if visited[y][x-1] == 0:
                visited[y][x-1] = 1
                miro(y, x-1)
                visited[y][x-1] = 0
        if x+1 <= n-1:
            if visited[y][x+1] == 0:
                visited[y][x+1] = 1
                miro(y, x+1)
                visited[y][x+1] = 0
        miro_pan[y][x] = 0

t = int(input())

for cnt_t in range(1, t+1):
    n = int(input())
    miro_pan = list()
    start_y = 0
    start_x = 0
    result = 0
    visited = list()
    for _ in range(n):
        tmp = list(map(int, input().strip()))
        miro_pan.append(tmp)
        visited.append(list(tmp))
    for y in range(n):
        for x in range(n):
            if visited[y][x] != 2:
                visited[y][x] = 0
            else:
                visited[y][x] = 1
    for y in range(n):
        for x in range(n):
            if miro_pan[y][x] == 2:
                start_y = y
                start_x = x
    de = -1
    miro(start_y, start_x)

    print('#{} {}'.format(cnt_t, result))
```

# 5. Forth

```
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
 

3 4 + .
 

Forth에서는 동작은 다음과 같다.
 

숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.

 

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
 

다음은 Forth 연산의 예이다.
 

코드

출력

4 2 / .

2

4 3 - .

1

 

 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.

나눗셈의 경우 항상 나누어 떨어진다.

 

[출력]
 

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
```

```
입력
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

출력
#1 84
#2 error
#3 168
```

```
t = int(input())

for cnt_t in range(1, t+1):
    datas = list(input().split())
    state = 0
    stack = list()
    for data in datas:
        if data.isdigit():
            stack.append(int(data))
        elif data == '*':
            if len(stack) <= 1:
                state = 1
                break
            b = stack.pop()
            a = stack.pop()
            if str(b).isdigit() and str(a).isdigit():
                c = a*b
                stack.append(c)
            else:
                state = 1
                break
        elif data == '/':
            if len(stack) <= 1:
                state = 1
                break
            b = stack.pop()
            a = stack.pop()
            if str(b).isdigit() and str(a).isdigit():
                # if b == 0 :
                #     state = 1
                #     break
                c = a // b
                stack.append(c)
            else:
                state = 1
                break
        elif data == '+':
            if len(stack) <= 1:
                state = 1
                break
            b = stack.pop()
            a = stack.pop()
            if str(b).isdigit() and str(a).isdigit():
                c = a + b
                stack.append(c)
            else:
                state = 1
                break
        elif data == '-':
            if len(stack) <= 1:
                state = 1
                break
            b = stack.pop()
            a = stack.pop()
            if str(b).isdigit() and str(a).isdigit():
                c = a - b
                stack.append(c)
            else:
                state = 1
                break
        else:
            break
    if state == 1:
        print('#{} error'.format(cnt_t))
    else:
        if len(stack) == 1:
            result = stack.pop()
            print('#{} {}'.format(cnt_t, result))
        else:
            print('#{} error'.format(cnt_t))
```

# 6. N Castle

```
체스에서  Castle은 다음 그림과 같이 가로, 세로 방향으로 자유롭게 이동할 수 있습니다.


N x N 체스판에 N 개의 캐슬을 배치시켜 나올 수 있는 경우의 수를 출력해주세요

단, 배치할때 서로 공격하지 않아야합니다. 만약 Castle을 배치해서 이동할 수 있는 곳에 또 다른 Castle이 있다면, 이는 공격가능한걸로 간주합니다.

아래 이미지는 N = 4 인 경우, 가능한 배치의일부입니다.


N 이 주어졌을 때, 서로 공격이 불가능하도록배치할 수 있는 경우의 수를 출력해 주세요

백트래킹으로 문제를 풀어주세요 

[입력]
10개의 테스트 케이스가 입력됩니다. 각 테스트 케이스별로 N 값이 주어집니다.  (1 <= N <= 10)

[출력]
각 테스트케이스별로
#T A 형태로 출력해주세요 (T는 테스트케이스 번호 1 <= T <= 10 , A는 경우의수를 의미한다 )
```

```
입력
1
2
3
4
5
6
7
8
9
10

출력
#1 1
#2 2
#3 6
#4 24
#5 120
#6 720
#7 5040
#8 40320
#9 362880
#10 3628800
```

```
def chess(y):
    global n
    global cnt
    if y >= 0:
        for x in range(n):
            if chess_pan[y][x] == 0 and check[x] == 0:
                chess_pan[y][x] = 1
                check[x] = 1
                if check == [1]*n:
                    cnt += 1
                chess(y-1)
                chess_pan[y][x] = 0
                check[x] = 0
    else:
        return


t = 10

for cnt_t in range(1, t+1):
    n = int(input())
    chess_pan = list()
    for _ in range(n):
        chess_pan.append([0]*n)
    check = [0]*n
    cnt = 0
    chess(n-1)
    print('#{} {}'.format(cnt_t, cnt))
```

# 7. 부분집합의 합2

```
1부터 20까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
 

예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
 

테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 20, 1 ≤ K ≤ 210 )

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력
3
3 6
5 15
5 10

출력
#1 1
#2 1
#3 0	
```

```
a = list()
for num in range(1, 20+1):
    a.append(num)
def dfs(n, k):
    global result
    if n == 0 :
        return
    check = 0
    sum_num = sum(num_lst)
    for a_num in a:
        if sum_num + a_num <= k:
            for num_lst_data in num_lst:
                if num_lst_data == a_num:
                    check = 1
        else :
            return
        if check == 1 :
            return
        else :
            num_lst.append(a_num)
            if sum(num_lst) == k :
                if n == 1 :
                    result += 1
            dfs(n-1, k)
            num_lst.pop()

t = int(input())

for cnt_t in range(1, t+1):
    n, k = map(int, input().split())
    num_lst = list()
    result = 0
    dfs(n, k)
    print('#{} {}'.format(cnt_t, result))
```

# 8. 계산기2

```
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+56*+7+"

변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
```

```
priority = {'*': 2, '+': 1}

t = 10

for cnt_t in range(1, t+1) :
    tsh = input()

    lst = list(input().strip())

    stack = list()

    new_lst = list()

    for data in lst:
        if ord('0') <= ord(data) <= ord('9'):
            new_lst.append(data)
        elif stack == list():
            stack.append(data)
        else:
            cnt = 1
            while cnt :
                cnt = 0
                if priority[data] > priority[stack[len(stack)-1]]:
                    stack.append(data)
                    break
                else:
                    new_lst.append(stack.pop())
                    stack.append(data)
                    if len(stack) == 2:
                        if stack[0] == stack[1] :
                            new_lst.append(stack.pop())

    while stack != list():
        new_lst.append(stack.pop())

    str_lst = ''

    for tmp_str in new_lst:
        str_lst += tmp_str

    result_lst = list(str_lst)

    cnt = 1
    while cnt :
        cnt = 0
        for cnt1 in range(len(result_lst)) :
            if result_lst[cnt1] == '*':
                data = int(result_lst[cnt1-2])*int(result_lst[cnt1-1])
                del result_lst[cnt1-2]
                del result_lst[cnt1-2]
                del result_lst[cnt1-2]
                result_lst.insert(cnt1-2, data)
                cnt = 1
                break

    cnt = 1
    while cnt :
        cnt = 0
        for cnt2 in range(len(result_lst)) :
            if result_lst[cnt2] == '+':
                data = int(result_lst[cnt2-2])+int(result_lst[cnt2-1])
                del result_lst[cnt2-2]
                del result_lst[cnt2-2]
                del result_lst[cnt2-2]
                result_lst.insert(cnt2-2, data)
                cnt = 1
                break

    print('#{} {}'.format(cnt_t, int(result_lst[0])))
```

# 9. 계산기3

```
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+(4+5)*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"345+6*+7+"

변환된 식을 계산하면 64를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.

이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.

피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
```

```
priority = {'*': 2, '/': 2, '-': 1, '+': 1, '(': 0}

t = 10

for cnt_t in range(1, t + 1):

    length = int(input())

    datas = list(input())

    stack = list()

    new_datas = list()

    for data in datas:
        if data == '(':
            stack.append(data)
        elif ord('0') <= ord(data) <= ord('9'):
            new_datas.append(data)
        elif data == ')':
            while 1:
                tmp = stack.pop()
                if tmp == '(':
                    break
                new_datas.append(tmp)
        else:
            if stack == list():
                stack.append(data)
            elif priority[data] > priority[stack[-1]]:
                stack.append(data)
            elif priority[data] == priority[stack[-1]]:
                new_datas.append(stack.pop())
                stack.append(data)
            else:
                new_datas.append(stack.pop())
                if stack == list() or stack[-1 == '(']:
                    stack.append(data)
                elif priority[stack[-1]] == priority[data]:
                    new_datas.append(stack.pop())
                    stack.append(data)

    while 1:
        if stack == list():
            break
        else:
            new_datas.append(stack.pop())

    result_lst = list(new_datas)

    while 1:
        if len(result_lst) == 1:
            break
        for cnt in range(len(result_lst)):
            if result_lst[cnt] == '*':
                b = int(result_lst[cnt-1])
                a = int(result_lst[cnt-2])
                tmp = a * b
                del result_lst[cnt - 2]
                del result_lst[cnt - 2]
                del result_lst[cnt - 2]
                result_lst.insert(cnt-2, tmp)
                break

            elif result_lst[cnt] == '/':
                b = int(result_lst[cnt - 1])
                a = int(result_lst[cnt - 2])
                tmp = a // b
                del result_lst[cnt - 2]
                del result_lst[cnt - 2]
                del result_lst[cnt - 2]
                result_lst.insert(cnt - 2, tmp)
                break

            elif result_lst[cnt] == '+':
                b = int(result_lst[cnt - 1])
                a = int(result_lst[cnt - 2])
                tmp = a + b
                del result_lst[cnt - 2]
                del result_lst[cnt - 2]
                del result_lst[cnt - 2]
                result_lst.insert(cnt - 2, tmp)
                break

            elif result_lst[cnt] == '-':
                b = int(result_lst[cnt - 1])
                a = int(result_lst[cnt - 2])
                tmp = a - b
                del result_lst[cnt - 2]
                del result_lst[cnt - 2]
                del result_lst[cnt - 2]
                result_lst.insert(cnt - 2, tmp)
                break

    print('#{} {}'.format(cnt_t, int(result_lst[0])))
```

