# 1. 반복문자 지우기

```
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
 

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
 

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
 

다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

 

[출력]
 

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다
```

```
입력
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

출력
#1 1
#2 4
#3 11
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    problem = list(input())
    state = 1
    while state :
        cnt = 0
        if len(problem) >= 2 :
            for cnt_p in range(len(problem)-1) :
                if problem[cnt_p] == problem[cnt_p+1] :
                    del problem[cnt_p]
                    del problem[cnt_p]
                    cnt = 1
                    break
                if cnt_p == len(problem) - 2 :
                    state = 0
        else :
            state = 0
    print('#{} {}'.format(cnt_t, len(list(problem))))
```

# 2. 그래프 경로

```
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
 

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
 


 

노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
 

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
 

E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

출력
#1 1
#2 1
#3 1
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    v, e = map(int, input().split())

    adj = [
        [0 for _ in range(v+1)] for _ in range(v+1)
    ]
    for _ in range(e) :
        y, x = map(int, input().split())
        adj[y][x] = 1

    def dfs(now):
        global find
        global destination
        # 자식노드 찾기
        for next in range(v+1):
            if adj[now][next] == 1 and visited[next] == 0:  # 연결? 방문안함?
                visited[next] = 1  # 다시 재귀호출 방지
                if next == destination :
                    find = 1
                    break
                dfs(next)
        return

    parent, destination = map(int, input().split())
    find = 0
    visited = [0]*(v+1)
    visited[0] = 1  # 시작노드 0번 방문체크 (이후의 재귀호출에서 다시 재귀호출 방지가능)
    dfs(parent)
    print('#{} {}'.format(cnt_t, find))


    def dfs(now):
        for next in range(4):
            if adj[now][next] == 1 and visited[next] == 0:  # 연결? 방문안함?
                visited[next] = 1  # 다시 재귀호출 방지
                dfs(next)

        return
```

# 3. 괄호 검사

```
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
 

예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
 

정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
 

print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.


 

[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

출력
#1 1
#2 1
#3 0
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    problem = list(input())
    lst = [0]
    ret = 0
    for val in problem :
        if val == '{' :
            lst.append(val)
        elif val == '}' :
            if lst.pop() == '{':
                pass
            else :
                ret = 0
                lst.append('error')
                break
        elif val == '(' :
            lst.append(val)
        elif val == ')' :
            if lst.pop() == '(' :
                pass
            else :
                ret = 0
                lst.append('error')
                break
    if lst == [0] :
        ret = 1
    print('#{} {}'.format(cnt_t, ret))
```

# 4. 종이붙이기

```
어린이 알고리즘 교실의 선생님은 경우의 수 놀이를 위해, 그림처럼 가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비했다.

   


그리고 교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다. N이 30인 경우 다음 그림처럼 종이를 붙일 수 있다.





10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오. 직사각형 종이가 모자라는 경우는 없다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력
3
30
50
70

출력
#1 5
#2 21
#3 85
```

```
def box_cnt(w) :
    if w == 10 :
        return 1
    elif w == 20 :
        return 3
    else :
        return box_cnt(w-10) + box_cnt(w-20)*2

t = int(input())
for cnt_t in range(1, t+1) :
    n = int(input())
    print('#{} {}'.format(cnt_t, box_cnt(n)))
```

# 5. 비밀번호

```
평소에 잔머리가 발달하고 게으른 철수는 비밀번호를 기억하는 것이 너무 귀찮았습니다.

적어서 가지고 다니고 싶지만 누가 볼까봐 걱정입니다. 한가지 생각을 해냅니다.
 
0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만드는 것입니다.

번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거 할 수 있습니다.

예를 들어 아래의 번호 열을 철수의 방법으로 소거하고 알아낸 비밀 번호입니다.
 


 
[입력]

10개의 테스트 케이스가 10줄에 걸쳐, 한 줄에 테스트 케이스 하나씩 제공된다.

각 테스트 케이스는 우선 문자열이 포함하는 문자의 총 수가 주어지고, 공백을 둔 다음 번호 문자열이 공백 없이 제공된다.

문자열은 0~9로 구성되며 문자열의 길이 N은 10≤N≤100이다. 비밀번호의 길이는 문자열의 길이보다 작다.
 
[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답(비밀번호)을 출력한다.
```

```
t = 10
for cnt_t in range(1, t+1) :
    tsh, problem = input().split()
    problem = list(problem)
    state = 1
    while state :
        cnt = 0
        if len(problem) >= 2 :
            for cnt_p in range(len(problem)-1) :
                if problem[cnt_p] == problem[cnt_p+1] :
                    del problem[cnt_p]
                    del problem[cnt_p]
                    cnt = 1
                    break
                if cnt_p == len(problem) - 2 :
                    state = 0
        else :
            state = 0
    ret = ''
    for dat in problem :
        ret += str(dat)

    print('#{} {}'.format(cnt_t, ret))

    # ABCCB
    # NNNASBBSNV
    # UKJWHGGHNFTCRRCTWLALX
```

# 6. 길찾기

```
그림과 같이 도식화한 지도에서 A도시에서 출발하여 B도시로 가는 길이 존재하는지 조사하려고 한다.

길 중간 중간에는 최대 2개의 갈림길이 존재하고, 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다.

다음과 같이 길이 주어질 때, A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하여라.

 - A와 B는 숫자 0과 99으로 고정된다.

 - 모든 길은 순서쌍으로 나타내어진다. 위 예시에서 2번에서 출발 할 수 있는 길의 표현은 (2, 5), (2, 9)로 나타낼 수 있다.

 - 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.

 - 단 화살표 방향을 거슬러 돌아갈 수는 없다.



[제약 사항]

출발점은 0, 도착점은 99으로 표현된다.

정점(분기점)의 개수는 98개(출발점과 도착점 제외)를 넘어가지 않으며, 한 개의 정점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않는다.

아래 제시된 가이드 라인은 제안사항일 뿐 강제사항은 아니다.

[데이터 저장 가이드]

정점(분기점)의 개수가 최대 100개 이기 때문에, size [100]의 정적 배열 2개을 선언하여, 각 정점의 번호를 주소로 사용하고, 저장되는 데이터는 각 정점에서 도착하는 정점의 번호를 저장한다.

위 그림을 저장하였을 때 결과는 다음과 같다.
 


[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호와 길의 총 개수가 주어지고 그 다음 줄에는 순서쌍이 주어진다.

순서쌍의 경우, 별도로 나누어 표현되는 것이 아니라 숫자의 나열이며, 나열된 순서대로 순서쌍을 이룬다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.
```

```
def search_line(start) :
    global ret
    if start == 99 :
        ret = 1
        return 0
    
    for destination in range(100) :
        if line_arr[start][destination] == 1 and check_list[destination] == 0:
            check_list[destination] = 1
            search_line(destination)
    return 0

# t = int(input())
t = 10
for cnt_t in range(1, t+1) :
    tsh, long = map(int, input().split())
    line = list(map(int,input().split()))
    line_arr = []
    for _ in range(100) :
        line_arr.append([0]*100)
    for idx in range(0, long*2, 2) :
        line_arr[line[idx]][line[idx+1]] = 1

    ret = 0

    check_list = [0] * 100

    check_list[0] = 1

    search_line(0)

    print('#{} {}'.format(cnt_t, ret))
```

