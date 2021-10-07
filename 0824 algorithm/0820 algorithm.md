# 1. 스도쿠 검증

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

