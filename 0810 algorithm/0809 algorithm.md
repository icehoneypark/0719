# 1. 숫자카드

```
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
```

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
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
 

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.

이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6

이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
 
답은 12와 6의 차인 6을 출력한다.

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )


다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

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
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 


[예시]



다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

 

[입력]
 

첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 

[출력]


#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
```

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
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

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
현주는 1번부터 N번까지 N개의 상자를 가지고 있다. 각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0으로 적혀있다.

숫자가 너무 단조로웠던 현주는 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 한다. 변경하는 방법은 다음과 같다.

   ·  i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경

현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램을 작성하라.



[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백으로 구분되어 주어진다.

다음 Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)이 주어진다.

 

[출력]

각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

각 테스트 케이스마다 Q개의 작업을 수행한 다음 1번부터 N번까지의 상자에 적혀있는 값들을 순서대로 출력한다.
```

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
숫자 N은 아래와 같다.

N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.


[제약 사항]

N은 2 이상 10,000,000 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```

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
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
 

가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의한다.

위의 예시에서 제1회 덤프를 수행한 이후 화면은 다음과 같다.

A부분의 상자를 가장 낮은 B부분에 덤프하였으며, A대신 A’부분의 상자를 사용해도 무방하다.

다음은 제2회 덤프를 수행한 이후의 화면이다. 

A’부분의 상자를 옮겨서, C부분에 덤프하였다. 이때 C 대신 C’부분에 덤프해도 무방하다.

2회의 덤프 후, 최고점과 최저점의 차이는 8 – 2 = 6 이 되었다 (최초덤프 이전에는 9 – 1 = 8 이었다).

덤프 횟수가 2회로 제한된다면, 이 예시 문제의 정답은 6이 된다.

[제약 사항]

가로 길이는 항상 100으로 주어진다.

모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

덤프 횟수는 1이상 1000이하로 주어진다.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

[입력]

총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.
```

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

