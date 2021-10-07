# 1. 특별한 정렬

```
입력 :
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11 
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

출력 :
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21
```

```
t = int(input())

for cnt_t in range(t) :

    n = int(input())

    get_data = list(map(int, input().split()))

    result = []

    for _ in range(5) :

        max = 21e-8
        min = 21e8

        for data in get_data :
            if max < data :
                max = data
            if min > data :
                min = data
        get_data.remove(max)
        get_data.remove(min)
        result.append(max)
        result.append(min)
    print('#{} '.format(cnt_t+1), end='')
    print(*result)
```

# 2. 이진탐색

```
입력 :
3
400 300 350
1000 299 578
1000 222 888

출력 :
#1 A
#2 0
#3 A
```

```
t = int(input())

for cnt_t in range(t) :

    get_data = list(map(int, input().split()))

    left_A = left_B = 1
    right_A = right_B = get_data[0]
    target_A = get_data[1]
    target_B = get_data[2]

    lst_A = [0]
    lst_B = [0]

    for page in range(1, right_A + 1) :
        lst_A.append(page)
    for page in range(1, right_B + 1) :
        lst_B.append(page)

    cnt_A = 0
    cnt_B = 0

    success_A = 0
    success_B = 0

    while left_A <= right_A :
        mid = (left_A + right_A) // 2
        cnt_A += 1
        if target_A == lst_A[mid]:
            success_A = 1
            break
        elif target_A < lst_A[mid] :
            right_A = mid
        elif target_A > lst_A[mid] :
            left_A = mid
    while left_B <= right_B :
        mid = (left_B + right_B) // 2
        cnt_B += 1
        if target_B == lst_B[mid]:
            success_B = 1
            break
        elif target_B < lst_B[mid] :
            right_B = mid
        elif target_B > lst_B[mid] :
            left_B = mid

    if success_A == 1 :
        if success_B == 1 :
            if cnt_A > cnt_B :
                print('#{} B'.format(cnt_t + 1))
            elif cnt_A < cnt_B :
                print('#{} A'.format(cnt_t + 1))
            else :
                print('#{} 0'.format(cnt_t + 1))
        else :
            print('#{} A'.format(cnt_t + 1))
    else :
        if success_B == 0 :
            print('#{} 0'.format(cnt_t + 1))
        else :
            print('#{} B'.format(cnt_t + 1))
```

# 3. 부분집합의 합

```
입력 :
3
3 6
5 15
5 10

출력 :
#1 1
#2 1
#3 0	
```

```
n = [1,2,3,4,5,6,7,8,9,10,11,12]

t = int(input())

for cnt_t in range(t) :

    tmp = list(map(int,input().split()))

    ans = 0
    
    for bit in range(1<<12) :
        sum = 0
        cnt = 0
        for j in range(12) :
            if bit & (1 << j):
                sum += n[j]
                cnt += 1
        if cnt == tmp[0] and sum == tmp[1]:
            ans += 1
    print('#{} {}'.format(cnt_t+1, ans))
```

# 4. 색칠하기

```
입력 :
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

출력 :
#1 4
#2 5
#3 7
```

```
t = int(input())

for cnt_t in range(t) :
    n = int(input())
    red_fixel = []
    blue_fixel = []
    for cnt_n in range(n) :
        colors = list(map(int,input().split()))
        # color_y1 = colors[0]
        # color_x1 = colors[1]
        # color_y2 = colors[2]
        # color_x2 = colors[3]
        # color = colors[4]

        for y in range(colors[0], colors[2] + 1) :
            for x in range(colors[1], colors[3] + 1) :
                if colors[4] == 1:
                    red_fixel.append([y,x])
                else :
                    blue_fixel.append([y,x])
    # if ['tmp'] in red_fixel :
    #     red_fixel.remove(['tmp'])
    # if ['tmp'] in blue_fixel :
    #     red_fixel.remove(['tmp'])
    # set(red_fixel)
    # set(blue_fixel)

    result = 0

    for red in red_fixel :
        for blue in blue_fixel :
            if red == blue :
                result += 1
    print('#{} {}'.format(cnt_t + 1, result))
```

# 5. 파리퇴치

```
t = int(input())
for cnt_t in range(1, t+1) :

    tmp1 = list(map(int, input().split()))  # 1차원 리스트 (한줄)

    n = tmp1[0]
    m = tmp1[1]
    data = []

    area_sum_list = []

    for _ in range(n) :
        tmp2 = list(map(int, input().split()))  # 1차원 리스트 (한줄)
        data.append(tmp2)

    for w in range(n-m+1) :
        for z in range(n-m+1) :
            tmp_sum = 0
            for y in range(m) :
                for x in range(m) :
                    tmp_sum += data[y+w][x+z]

            area_sum_list.append((tmp_sum))

    max_sum = 21e-8
    for value in area_sum_list :
        if max_sum < value :
            max_sum = value

    print('#{} {}'.format(cnt_t, max_sum))
```

# 6. 어디에 단어가 들어갈 수 있을까

```
t = int(input())

for cnt_t in range(t) :
    tmp = list(map(int,input().split()))

    n = tmp[0]
    k = tmp[1]
    lst = []
    for _ in range(n) :
        tmp2 = list(map(int,input().split()))
        lst.append(tmp2)

    a1 = [0]*n
    a2 = [0]*n
    lst.insert(0, a1)
    lst.insert(len(lst), a2)

    for lst_data in lst :
        lst_data.insert(0, 0)
        lst_data.insert(len(lst_data), 0)
        # print(lst_data)

    cnt = 0
    result = 0
    for y_tmp in range(1, n+1) :
        for x in range(1, n-k+2) :
            if lst[y_tmp][x] == 1 :
                if lst[y_tmp][x-1] == 0 :
                    if lst[y_tmp][x+k] == 0 :
                        for tmp in range(k) :
                            if lst[y_tmp][x+tmp] == 1 :
                                cnt += 1
                            else :
                                cnt = 0
                                break
                            if cnt == k :
                                cnt = 0
                                result += 1
    for x_tmp in range(1, n+1) :
        for y in range(1, n-k+2) :
            if lst[y][x_tmp] == 1 :
                if lst[y-1][x_tmp] == 0 :
                    if lst[y+k][x_tmp] == 0 :
                        for tmp in range(k) :
                            if lst[y+tmp][x_tmp] == 1 :
                                cnt += 1
                            else :
                                cnt = 0
                                break
                            if cnt == k :
                                cnt = 0
                                result += 1


    print('#{} {}'.format(cnt_t+1, result))
```

# 7. 숫자를 정렬하자

```
t = int(input())

for cnt_t in range(1, t+1) :

    n = int(input())

    lst = list(map(int, input().split()))  # 1차원 리스트 (한줄)

    for i in range(n-1) :
        for j in range(1, n-i) :
            if lst[i] > lst[i+j] :
                lst[i], lst[i+j] = lst[i+j], lst[i]

    print('#{} '.format(cnt_t), end='')
    print(*lst)
```

# 8. Ladder1

```
for cnt_t in range(1, 11):

    cnt_t = int(input())

    ladder = []

    for _ in range(100) :
        tmp = list(map(int,input().split()))
        ladder.append(tmp)

    for x in range(100) :
        y = 0
        if ladder[y][x] == 1 :
            start = x
            while y < 100 :
                if x == 0 :
                    if ladder[y][x+1] == 0 :
                        y += 1
                    if ladder[y][x+1] == 1 :
                        while 1 :
                            x += 1
                            if x == 99:
                                break
                            if ladder[y][x+1] == 0 :
                                break
                        y += 1
                elif x == 99 :
                    if ladder[y][x-1] == 0 :
                        y += 1
                    if ladder[y][x-1] == 1 :
                        while 1 :
                            x -= 1
                            if x == 0:
                                break
                            if ladder[y][x-1] == 0 :
                                break
                        y += 1
                else :
                    if ladder[y][x+1] == 0 and ladder[y][x-1] == 0 :
                        y += 1
                    if ladder[y][x+1] == 1 :
                        while 1:
                            x += 1
                            if x == 99:
                                break
                            if ladder[y][x+1] == 0:
                                break
                        y += 1
                    if ladder[y][x-1] == 1:
                        while 1:
                            x -= 1
                            if x == 0:
                                break
                            if ladder[y][x-1] == 0:
                                break
                        y += 1
                if ladder[y][x] == 2 :
                    print('#{} {}'.format(cnt_t, start))
                if y == 99 :
                    break
```

