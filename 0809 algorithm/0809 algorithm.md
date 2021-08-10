# 1. View

```
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
 
아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.

A와 B로 표시된 세대의 경우는 왼쪽 조망은 2칸 이상 확보가 되었지만 오른쪽 조망은 한 칸 밖에 확보가 되지 않으므로 조망권을 확보하지 못하였다.

C의 경우는 반대로 오른쪽 조망은 2칸이 확보가 되었지만 왼쪽 조망이 한 칸 밖에 확보되지 않았다.
 
[제약 사항]

가로 길이는 항상 1000이하로 주어진다.

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)

각 빌딩의 높이는 최대 255이다.
 
[입력]

입력 파일의 첫 번째 줄에는 테스트케이스의 길이가 주어진다. 그 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.
 
[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 조망권이 확보된 세대의 수를 출력한다.
```

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
0~9 사이의 숫자카드에서 임의의 카드 6장을 뽑았을때, 
3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
3장의 카드가 동일한 번호를 갖는 경우를 tripletes이라고 한다. 

그리고, 6장의 카드가 run과 tripletes로만 구성된 경우를 Baby-Gin이라고 하는데,  
6자리의 숫자를 입력받아 Baby-Gin 여부를 판단하는 프로그램을 작성해보자.

예) 
667767은 두 개의 triplet이므로 Baby-Gin이다. (666,777) 
054060은 한 개의 run과 한 개의 triplet이므로 Baby-Gin이다. (456,000)
101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 Baby-Gin이 아니다.

[입력]
첫 번째 줄에 Test Case의 수 T가 주어집니다.
T개의 줄에 걸쳐 각 Baby-Gin인지 확인할 TestCase가 6자리 수로 주어집니다.

[출력]
각 TestCase에 대하여 '#'과 TestCase번호, Baby Gin의 여부를 출력합니다.
Baby Gin의 여부로 Baby Gin인 경우 Baby Gin을 출력하고, 아닌 경우 Lose를 출력합니다.
```

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
상자들이 쌓여있는 방이있다. 
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 
낙차가 가장 큰 상자를 구하여 그 낙차를 출력하여 보자.
위의 예시에서 총 26개의 상자가 회전 후, 오른쪽 그림의 상태가 된다. 

A상자의 낙차가 7로 가장 크므로 7을 출력하면 된다. 

회전결과, B상자의 낙차는 6, C상자의 낙차는 1이다.
중력은 회전이 완료된 후 적용된다.
상자들은 모두 한 쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.

[입력]
첫 번째 줄에 test case의 수 T(1≤T≤100)가 주어진다. 
각 케이스의 첫 째줄에 방의 가로 길이 N(2≤N≤100)가 주어진다. 
다음 줄에는 N개의 상자들이 쌓여있는 높이 H(0≤H≤M)가 주어진다.

[출력]
낙차가 가장 큰 값을 출력한다.
```

```
입력 : 
1
9
7 4 2 0 0 6 0 7 0

출력 : 
#1 7
```

```
```

