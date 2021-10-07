# 1. N과 M(1)

```
예제 입력 1 
3 1
예제 출력 1 
1
2
3

예제 입력 2 
4 2
예제 출력 2 
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3

예제 입력 3 
4 4
예제 출력 3 
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1
```

```python
def su(m):
    if m == 0:
        print(*lst)
        return
    global n
    for num in range(1, n + 1):
        if num in lst:
            pass
        else:
            lst.append(num)
            su(m - 1)
            lst.pop()



n, m = map(int, input().split())
lst = list()
su(m)
```

# 2. N과 M(4)

```
예제 입력 1 
3 1
예제 출력 1 
1
2
3
예제 입력 2 
4 2
예제 출력 2 
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
예제 입력 3 
3 3
예제 출력 3 
1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3
```

```python
def su(m):
    global n
    global max_n
    if m == 0:
        print(*lst)
        return
    for num in range(1, n + 1):
        if num >= max_n:
            tmp = max_n
            max_n = num
            lst.append(num)
            su(m - 1)
            lst.pop()
            max_n = tmp


n, m = map(int, input().split())

lst = list()
max_n = 1
su(m)
```



# 3. 최대 상금

```python
def cng_num(cng_cnt):
    if cng_cnt == 0:
        return
    before_result_lst = list(result_lst)
    result_lst.clear()
    for lst_num in range(len(before_result_lst)):
        for left in range(len(before_result_lst[lst_num]) - 1):
            for right in range(left + 1, len(before_result_lst[lst_num])):
                before_result_lst[lst_num][left], before_result_lst[lst_num][right] = before_result_lst[lst_num][right], before_result_lst[lst_num][left]
                if not before_result_lst[lst_num] in result_lst:
                    result_lst.append(list(before_result_lst[lst_num]))
                before_result_lst[lst_num][left], before_result_lst[lst_num][right] = before_result_lst[lst_num][right], before_result_lst[lst_num][left]
    cng_num(cng_cnt - 1)


t = int(input())

for cnt_t in range(1, t+1):
    num, cng_cnt = input().split()

    num = list(map(int, num))

    cng_cnt = int(cng_cnt)

    result_lst = list()

    result_lst.append(num)

    before_result_lst = list()

    cng_num(cng_cnt)

    max_num = '0'
    for result_data in result_lst:
        num = ''
        for tmp in result_data:
            num += str(tmp)
            if int(max_num) < int(num):
                max_num = num
    print('#{} {}'.format(cnt_t, max_num))
```

