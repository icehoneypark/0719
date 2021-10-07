# 1. View

```
test_case = 10

i = 0

while i < test_case :
    i += 1
    sub_sum = 0
    length = int(input())
    lst = list(map(int,input().split()))

    for number in range(length) :
        if number > 1 and number < length-2 :
            if lst[number] > lst[number-1] and lst[number] > lst[number-2] and lst[number] > lst[number+1] and lst[number] > lst[number+2] :
                sub1 = lst[number] - lst[number-1]
                sub2 = lst[number] - lst[number-2]
                sub3 = lst[number] - lst[number+1]
                sub4 = lst[number] - lst[number+2]
                sub_min = sorted([sub1, sub2, sub3, sub4])[0]
                sub_sum += sub_min
    print(f'#{i} {sub_sum}')
```



# 2. Baby Gin

```
입력 : 
3
667767
054060
101123

출력 : 
#1 Baby Gin
#2 Baby Gin
#3 Lose
```

```
try_count = int(input())

for count in range(try_count) :
    answer = 0
    num = list(map(int, input().strip()))
    lst = [0]*10
    for cnt in num :
        lst[cnt] += 1

    i = 0

    for cnt2 in lst :
        if cnt2 == 6:
            lst[i] -= 6
            answer += 2
            print(f'#{count+1} Baby Gin')
            
        if 6 > cnt2 >= 3:
            lst[i] -= 3
            answer += 1
            if answer == 2 :
                print(f'#{count+1} Baby Gin')
        i += 1
    for j in range(len(lst)-2) :
        if lst[j] > 0 and lst[j+1] > 0 and lst[j+2] > 0 :
            lst[j] -= 1
            lst[j+1] -= 1
            lst[j+2] -= 1
            answer += 1
            if answer == 2 :
                print(f'#{count+1} Baby Gin')
    if answer != 2 :
        print(f'#{count+1} Lose')
```

# 3. Gravity

```
입력 : 
1
9
7 4 2 0 0 6 0 7 0

출력 : 
#1 7
```

```
# t입력
t = int(input())
# n 입력

for i in range(t):

    n = int(input())
    # h 입력

    h = list(map(int, input().split()))
    # t 횟수만큼 동작

    # 1부터 시작하고 계속 1씩 더함
    i += 1
    # 각 블록의 낙차를 다 구해서 리스트로 정리
    fall_length_list = []
    # 첫 번째 칸 부터 마지막 칸 까지 (x축 값)
    for tmp1 in range(n):

        if h[tmp1] == 0:
            pass
        else:
            # 해당 x축 값의 각 상자의 낙차를 구함(높이가 1에서 최대 높이까지)
            for tmp2 in range(1, h[tmp1] + 1):
                # 낙차 저장 변수
                higher_cnt = 0
                # 비교하려는 상자 이후의 x축의 상자들의 높이와 비교해서 낙차 카운트
                for tmp3 in range(tmp1 + 1, n):
                    # 해당 x축의 상자가 이후의 상자의 높이가 같거나 높을 때 1씩 더하기
                    if tmp2 <= h[tmp3]:
                        higher_cnt += 1
                # 같거나 높은 상자, index값을 너비에서 뺌 (-1은 index가 칸보다 1이 적어서)
                fall_length_list.append(n - 1 - tmp1 - higher_cnt)

    # 낙차 중 가장 큰 값 변수 지정
    find_max = 0

    # 낙차가 가장 큰 값을 저장
    for minus in fall_length_list:
        if find_max <= minus:
            find_max = minus

    print('#{} {}'.format(i, find_max))
```

