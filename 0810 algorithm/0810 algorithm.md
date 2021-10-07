# 1. 숫자카드

```
입력 : 
3
5
49679
5
08271
10
7797946543

출력 :
#1 9 2
#2 8 1
#3 7 3 
```

```
t = int(input())

for j in range(t) :

    jang = int(input())

    j += 1
    a = list(map(int,input().strip()))
    card_num_list = [0]*10
    for i in range(10) :
        for num in a :
            if i == num :
                card_num_list[i] += 1
        max_value = 21e-8
        for value in card_num_list :
            if max_value < value :
                max_value = value
    index_max = 0
    for i in range(10) :
        if card_num_list[i] == max_value :
            index_max = i


    print('#{} {} {}'.format(j, index_max, max_value))
```

# 2. 구간합

```
입력 : 
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

출력 :
#1 21
#2 11088
#3 1090
```

```
t = int(input())

for j in range(t) :
    j += 1

    tmp = list(map(int,input().split()))

    n = tmp[0]

    m = tmp[1]

    a = list(map(int,input().split()))

    sum_min = 21e9
    sum_max = 21e-9
    sum_list = []

    for i in range(len(a) - m + 1):
        sum_m = 0
        for k in range(m) :
            sum_m += a[i+k]
        sum_list.append(sum_m)

    for sum_value in sum_list :
        if sum_value > sum_max :
            sum_max = sum_value
        if sum_value < sum_min :
            sum_min = sum_value

    sub_value = sum_max - sum_min

    print('#{} {}'.format(j, sub_value))
```

# 3. 전기버스

```
입력 :
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

출력 :
#1 3
#2 0
#3 4
```

```
t = int(input())

i = 0

while i < t :
    i += 1

    a = list(map(int, input().split()))

    k_copy = k = a[0]
    n = a[1]
    m = a[2]

    can_charge_bus_stop_list = list(map(int, input().split()))

    can = 0

    for j in range(m - 1) :
        cnt_len_bus_stop = can_charge_bus_stop_list[j+1] - can_charge_bus_stop_list[j]
        if cnt_len_bus_stop > k :
            can = 1
            break;

    position = 0
    charge_cnt = 0

    while 1 :
        if can == 1 :
            break
        position += 1
        k -= 1
        if position == n :
            break
        if k == 0 :
            for for_charge in range(k_copy) :
                for can_charge in can_charge_bus_stop_list :
                    if position - for_charge == can_charge :
                        k = k_copy
                        position = position - for_charge
                        charge_cnt += 1
                        break
                if k == k_copy :
                    break
    print('#{} {}'.format(i, charge_cnt))
```

# 4. min max

```
입력 :
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

출력 :
#1 630739
#2 740510
#3 838110
```

```
t = int(input())

for i in range(t):
    plus_value_cnt = int(input())
    a = list(map(int, input().split()))

    max_value = 0
    min_value = 21e9

    for value in a :
        if value > max_value :
            max_value = value
        if value < min_value :
            min_value = value

    max_minus_min = max_value - min_value
    print('#{} {}'.format(i+1, max_minus_min))
```

# 5. 현주의 상자 바꾸기

```
입력 :
1
5 2
1 3
2 4	// Test Case 개수
// 첫 번째 Test Case, N=5, Q=2
// i = 1일 때, L=1, R=3
// i = 2일 때, L=2, R=4

출력 :
#1 1 2 2 2 0	//첫 번째 테스트케이스 결과
```

```
t = int(input())

for j in range(t) :
    j += 1
    tmp1 = list(map(int,input().split()))

    n = tmp1[0]
    q = tmp1[1]

    box_list = [0]*n

    for i in range(q) :

        i += 1
        tmp2 = list(map(int,input().split()))

        l = tmp2[0]
        r = tmp2[1]

        for change in range(l-1, r) :
            box_list[change] = i

    print('#{}'.format(j), end=' ')
    for k in range(len(box_list)) :
        print(box_list[k], end=' ')
    print('')
```

# 6. 간단한 소인수분해

```
입력 :
10  
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750

출력 :
#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0
```

```
t = int(input())

for i in range(t) :
    i += 1
    a = int(input())

    # index -> [0] = 2 [1] = 3 [2] = 5 [3] = 7 [4] = 11
    insu_list = [0]*5
    while 1 :
        if a % 2 == 0 :
            insu_list[0] += 1
            a //= 2
        if a % 3 == 0 :
            insu_list[1] += 1
            a //= 3
        if a % 5 == 0 :
            insu_list[2] += 1
            a //= 5
        if a % 7 == 0 :
            insu_list[3] += 1
            a //= 7
        if a % 11 == 0 :
            insu_list[4] += 1
            a //= 11
        if a == 1 :
            break
    print('#{} {} {} {} {} {}'.format(i, insu_list[0], insu_list[1], insu_list[2], insu_list[3], insu_list[4]))
```

# 7. Flatten

```
i = 1
 
while i <= 10 :
    dump = int(input())
 
    box_list = list(map(int, input().split()))
 
    cnt = 0
    for _ in range(dump) :
        sorted_box_list = sorted(box_list)
        j = 0
        while 1 :
            if box_list[j] == sorted_box_list[0] :
                box_list[j] += 1
                k = 0
                while 1 :
                    if box_list[k] == sorted_box_list[len(sorted_box_list) - 1]:
                        box_list[k] -= 1
                        cnt += 1
                        break
                    k += 1
                break
            j += 1
    sorted_box_list = sorted(list(set(box_list)))
    result = sorted_box_list[len(sorted_box_list) - 1] - sorted_box_list[0]
    print('#{} {}'.format(i, result))
 
    i += 1
```

