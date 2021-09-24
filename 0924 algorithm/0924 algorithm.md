# 1. 탈주범 검거

```
교도소로 이송 중이던 흉악범이 탈출하는 사건이 발생하여 수색에 나섰다.

탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,

지하 터널 어딘가에서 은신 중인 것으로 추정된다.

터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산하여야 한다.

탈주범은 시간당 1의 거리를 움직일 수 있다.

지하 터널은 총 7 종류의 터널 구조물로 구성되어 있으며 각 구조물 별 설명은 [표 1]과 같다.


[그림 1-1] 은 지하 터널 지도의 한 예를 나타낸다.

이 경우 지도의 세로 크기는 5, 가로 크기는 6 이다.

맨홀 뚜껑의 위치가 ( 2, 1 ) 으로 주어질 경우, 이는 세로 위치 2, 가로 위치 1을 의미하며 [그림 1-2] 에서 붉은 색으로 표기된 구역이다.

탈주범이 탈출 한 시간 뒤 도달할 수 있는 지점은 한 곳이다.

탈주범이 2시간 후 도달할 수 있는 지점은, [그림 1-3] 과 같이 맨홀 뚜껑이 위치한 붉은 색으로 표시된 지하도 와 파란색으로 표기된 지하도까지 총 3개의 장소에 있을 수 있다.

3시간 후에는 [그림 1-4] 과 같이 총 5개의 지점에 있을 수 있다.
       

[그림 2-1] 에서 맨홀뚜껑이 위치한 지점이 ( 2, 2 ) 이고 경과한 시간이 6 으로 주어질 경우,

[그림 2-2] 에서 맨홀뚜껑이 위치한 지점은 붉은 색, 탈주범이 있을 수 있는 장소가 푸른색으로 표기되어 있다.

탈주범이 있을 수 있는 장소는, 맨홀뚜껑이 위치한 지점을 포함하여 총 15 개 이다.
       

지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산하는 프로그램을 작성하라.


[제약 사항]

1. 시간 제한 : 최대 50개 테이트 케이스를 모두 통과하는데, C/C++/Java 모두 1초

2. 지하 터널 지도의 세로 크기 N, 가로 크기 M은 각각 5 이상 50 이하이다. (5 ≤ N, M ≤ 50)

3. 맨홀 뚜껑의 세로 위치 R 은 0 이상 N-1이하이고 가로 위치 C 는 0 이상 M-1이하이다. (0 ≤ R ≤ N-1, 0 ≤ C ≤ M-1)

4. 탈출 후 소요된 시간 L은 1 이상 20 이하이다. (1 ≤ L ≤ 20)

5. 지하 터널 지도에는 반드시 1개 이상의 터널이 있음이 보장된다.

6. 맨홀 뚜껑은 항상 터널이 있는 위치에 존재한다.

[입력]

첫 줄에 총 테스트 케이스의 개수 T가 주어진다.

두 번째 줄부터 T개의 테스트 케이스가 차례대로 주어진다.

각 테스트 케이스의 첫 줄에는 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.

그 다음 N 줄에는 지하 터널 지도 정보가 주어지는데, 각 줄마다 M 개의 숫자가 주어진다.

숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미하며 숫자 0 은 터널이 없는 장소를 의미한다.

[출력]

테스트 케이스의 개수만큼 T줄에 T개의 테스트 케이스 각각에 대한 답을 출력한다.

각 줄은 “#x”로 시작하고 공백을 하나 둔 다음 정답을 기록한다. (x는 1부터 시작하는 테스트 케이스의 번호이다)

출력해야 할 정답은 탈주범이 위치할 수 있는 장소의 개수이다.
```

```python
t = int(input())

for cnt_t in range(1, t+1):
    n, m, hy, hx, time = map(int, input().split())

    pipe_map = list()
    visited = list()

    for _ in range(n):
        pipe_map.append(list(map(int, input().split())))
        visited.append([0]*m)

    visited[hy][hx] = 1

    for cnt in range(2, time + 1):
        for y in range(n):
            for x in range(m):
                if visited[y][x] == cnt - 1:
                    if pipe_map[y][x] == 1:
                        #상
                        if y - 1 >= 0:
                            if pipe_map[y - 1][x] == 1 or pipe_map[y - 1][x] == 2 or pipe_map[y - 1][x] == 5 or pipe_map[y - 1][x] == 6:
                                if visited[y - 1][x] == 0:
                                    visited[y - 1][x] = cnt
                        #하
                        if y + 1 < n:
                            if pipe_map[y + 1][x] == 1 or pipe_map[y + 1][x] == 2 or pipe_map[y + 1][x] == 4 or pipe_map[y + 1][x] == 7:
                                if visited[y + 1][x] == 0:
                                    visited[y + 1][x] = cnt
                        #좌
                        if x - 1 >= 0:
                            if pipe_map[y][x - 1] == 1 or pipe_map[y][x - 1] == 3 or pipe_map[y][x - 1] == 4 or pipe_map[y][x - 1] == 5:
                                if visited[y][x - 1] == 0:
                                    visited[y][x - 1] = cnt
                        #우
                        if x + 1 < m:
                            if pipe_map[y][x + 1] == 1 or pipe_map[y][x + 1] == 3 or pipe_map[y][x + 1] == 6 or pipe_map[y][x + 1] == 7:
                                if visited[y][x + 1] == 0:
                                    visited[y][x + 1] = cnt
                    elif pipe_map[y][x] == 2:
                        # 상
                        if y - 1 >= 0:
                            if pipe_map[y - 1][x] == 1 or pipe_map[y - 1][x] == 2 or pipe_map[y - 1][x] == 5 or pipe_map[y - 1][x] == 6:
                                if visited[y - 1][x] == 0:
                                    visited[y - 1][x] = cnt
                        #하
                        if y + 1 < n:
                            if pipe_map[y + 1][x] == 1 or pipe_map[y + 1][x] == 2 or pipe_map[y + 1][x] == 4 or pipe_map[y + 1][x] == 7:
                                if visited[y + 1][x] == 0:
                                    visited[y + 1][x] = cnt
                    elif pipe_map[y][x] == 3:
                        # 좌
                        if x - 1 >= 0:
                            if pipe_map[y][x - 1] == 1 or pipe_map[y][x - 1] == 3 or pipe_map[y][x - 1] == 4 or pipe_map[y][x - 1] == 5:
                                if visited[y][x - 1] == 0:
                                    visited[y][x - 1] = cnt
                        # 우
                        if x + 1 < m:
                            if pipe_map[y][x + 1] == 1 or pipe_map[y][x + 1] == 3 or pipe_map[y][x + 1] == 6 or pipe_map[y][x + 1] == 7:
                                if visited[y][x + 1] == 0:
                                    visited[y][x + 1] = cnt
                    elif pipe_map[y][x] == 4:
                        # 상
                        if y - 1 >= 0:
                            if pipe_map[y - 1][x] == 1 or pipe_map[y - 1][x] == 2 or pipe_map[y - 1][x] == 5 or pipe_map[y - 1][x] == 6:
                                if visited[y - 1][x] == 0:
                                    visited[y - 1][x] = cnt
                        # 우
                        if x + 1 < m:
                            if pipe_map[y][x + 1] == 1 or pipe_map[y][x + 1] == 3 or pipe_map[y][x + 1] == 6 or pipe_map[y][x + 1] == 7:
                                if visited[y][x + 1] == 0:
                                    visited[y][x + 1] = cnt

                    elif pipe_map[y][x] == 5:
                        # 하
                        if y + 1 < n:
                            if pipe_map[y + 1][x] == 1 or pipe_map[y + 1][x] == 2 or pipe_map[y + 1][x] == 4 or pipe_map[y + 1][x] == 7:
                                if visited[y + 1][x] == 0:
                                    visited[y + 1][x] = cnt
                        # 우
                        if x + 1 < m:
                            if pipe_map[y][x + 1] == 1 or pipe_map[y][x + 1] == 3 or pipe_map[y][x + 1] == 6 or pipe_map[y][x + 1] == 7:
                                if visited[y][x + 1] == 0:
                                    visited[y][x + 1] = cnt
                    elif pipe_map[y][x] == 6:
                        # 하
                        if y + 1 < n:
                            if pipe_map[y + 1][x] == 1 or pipe_map[y + 1][x] == 2 or pipe_map[y + 1][x] == 4 or pipe_map[y + 1][x] == 7:
                                if visited[y + 1][x] == 0:
                                    visited[y + 1][x] = cnt
                        # 좌
                        if x - 1 >= 0:
                            if pipe_map[y][x - 1] == 1 or pipe_map[y][x - 1] == 3 or pipe_map[y][x - 1] == 4 or pipe_map[y][x - 1] == 5:
                                if visited[y][x - 1] == 0:
                                    visited[y][x - 1] = cnt
                    elif pipe_map[y][x] == 7:
                        # 상
                        if y - 1 >= 0:
                            if pipe_map[y - 1][x] == 1 or pipe_map[y - 1][x] == 2 or pipe_map[y - 1][x] == 5 or pipe_map[y - 1][x] == 6:
                                if visited[y - 1][x] == 0:
                                    visited[y - 1][x] = cnt
                        # 좌
                        if x - 1 >= 0:
                            if pipe_map[y][x - 1] == 1 or pipe_map[y][x - 1] == 3 or pipe_map[y][x - 1] == 4 or pipe_map[y][x - 1] == 5:
                                if visited[y][x - 1] == 0:
                                    visited[y][x - 1] = cnt

    result = 0
    for y in range(n):
        for x in range(m):
            if visited[y][x] >= 1:
                result += 1

    print('#{} {}'.format(cnt_t, result))
```



# 2. 수영장

```
김 프로는 수영장을 이용한다.

김 프로는 지출이 너무 많아 내년 1년 동안 각 달의 이용 계획을 수립하고 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 있다.

수영장에서 판매하고 있는 이용권은 아래와 같이 4 종류이다.

   ① 1일 이용권 : 1일 이용이 가능하다.

   ② 1달 이용권 : 1달 동안 이용이 가능하다. 1달 이용권은 매달 1일부터 시작한다.

   ③ 3달 이용권 : 연속된 3달 동안 이용이 가능하다. 3달 이용권은 매달 1일부터 시작한다.
       (11월, 12월에도 3달 이용권을 사용할 수 있다 / 다음 해의 이용권만을 구매할 수 있기 때문에 3달 이용권은 11월, 12월, 1윌 이나 12월, 1월, 2월 동안 사용하도록 구매할 수는 없다.)

   ④ 1년 이용권 : 1년 동안 이용이 가능하다. 1년 이용권은 매년 1월 1일부터 시작한다.

각 달의 이용 계획은 [Table 1]의 형태로 수립된다.

이용 계획에 나타나는 숫자는 해당 달에 수영장을 이용할 날의 수를 의미한다.

각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,

가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램을 작성하라.


[예시]

수영장에서 판매하는 1일 이용권, 1달 이용권, 3달 이용권, 1년 이용권의 요금은 각각 10원, 40원, 100원, 300원이다.

이 때 수영장을 이용할 수 있는 방법은 [Table 2]와 같이 다양한 경우를 생각할 수 있다.

 
이용하는 방법

이용권

비용

1번 경우)
모두 1일 이용권으로만 이용한다.

1일 이용권 17개 :
17 * 10원 = 170원

170원

2번 경우)
모두 1달 이용권으로만 이용한다.

1달 이용권 4개 :
4 * 40원 = 160원

160원

3번 경우)

3월은 1일 이용권으로 이용하고
4월, 5월, 6월은 3달 이용권으로 이용한다.

1일 이용권 2개, 3달 이용권 1개 :
2 * 10원 + 1 * 100원 = 120원

120원

4번 경우)

3월과 5월은 1일 이용권으로 이용하고
4월과 6월은 1달 이용권으로 이용한다.

1일 이용권 3개, 1달 이용권 2개 :
3 * 10원 + 2 * 40원 = 110원

110원

5번 경우)

1년 이용권으로 이용한다.

1년 이용권 1개 :
1 * 300원 = 300원

300원

[Table 2]


다른 경우도 가능하지만, 가장 적은 비용으로 수영장을 이용한 경우는 4번 경우이다.

따라서, 정답은 110이 된다.


[제약 사항]

1. 시간 제한 : 최대 50개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초

2. 모든 종류의 이용권 요금은 10 이상 3,000 이하의 정수이다.

3. 각 달의 이용 계획은 각 달의 마지막 일자보다 크지 않다.

[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 1일 이용권의 요금, 1달 이용권의 요금, 3달 이용권의 요금, 1년 이용권의 요금이 순서대로 한 칸씩 띄고 주어진다.

그 다음 줄에는 1월부터 12월까지의 이용 계획이 주어진다.

[출력]

테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.

각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t는 1부터 시작하는 테스트 케이스의 번호이다)

출력해야 할 정답은 이용 계획대로 수영장을 이용하는 경우 중 가장 적게 지출하는 비용이다.
```

```
t = int(input())

for cnt_t in range(1, t+1):

    day, month, month3, year = map(int, input().split())

    schedule = list(map(int, input().split()))

    low_price = [0] * len(schedule)

    for m in range(len(schedule)):
        if m == 0:
            p1 = day * schedule[m]
            p2 = month
            if p1 < p2:
                low_price[m] = p1
            else:
                low_price[m] = p2
        elif m == 1:
            p1 = low_price[m - 1] + day * schedule[m]
            p2 = low_price[m - 1] + month
            if p1 < p2:
                low_price[m] = p1
            else:
                low_price[m] = p2
        elif m == 2:
            p1 = low_price[m - 1] + day * schedule[m]
            p2 = low_price[m - 1] + month
            p3 = month3
            if p1 < p2:
                s1 = p1
            else:
                s1 = p2
            if p2 < p3:
                s2 = p2
            else:
                s2 = p3
            if s1 < s2:
                low_price[m] = s1
            else:
                low_price[m] = s2
        else:
            p1 = low_price[m - 1] + day * schedule[m]
            p2 = low_price[m - 1] + month
            p3 = low_price[m - 3] + month3
            if p1 < p2:
                s1 = p1
            else:
                s1 = p2
            if p2 < p3:
                s2 = p2
            else:
                s2 = p3
            if s1 < s2:
                low_price[m] = s1
            else:
                low_price[m] = s2
    if low_price[-1] < year:
        result = low_price[-1]
    else:
        result = year
    print('#{} {}'.format(cnt_t, result))
```

