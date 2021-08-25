# 1. 회전

```
N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

 
     


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
```

```
입력
3
3 10
5527 731 31274 
5 12
18140 14618 18641 22536 23097 
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907

출력
#1 731
#2 18641
#3 2412
```

```
t = int(input())

for cnt_t in range(1, t+1):
    n, m = map(int, input().split())

    queue_list = list(map(int, input().split()))

    front = 0
    rear = -1
    for_use_list = [0 for _ in range(2000)]

    for queue_data in queue_list:
        rear += 1
        for_use_list[rear] = queue_data

    for _ in range(m):
        rear += 1
        for_use_list[rear] = for_use_list[front]
        for_use_list[front] = 0
        front += 1

    print('#{} {}'.format(cnt_t, for_use_list[front]))
```

# 2. 암호생성기

```
다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

- 8개의 숫자를 입력 받는다.

- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.
 


[1 사이클]

 
 
[암호 도출]
 
[제약 사항]

주어지는 각 수는 integer 범위를 넘지 않는다.

마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.
 
[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고, 그 다음 줄에는 8개의 데이터가 주어진다.
 
[출력]

#부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
```

```
from collections import deque

t = 10

for _ in range(1, t + 1):
    cnt_t = int(input())
    numbers = list(map(int, input().split()))

    result_queue = deque()

    for number in numbers:
        result_queue.append(number)

    tmp = 1
    while tmp:
        submit_value = 1
        for _ in range(5):
            tmp = result_queue.popleft()
            tmp -= submit_value
            submit_value += 1
            if tmp <= 0:
                tmp = 0
                result_queue.append(tmp)
                break
            result_queue.append(tmp)
    result_queue = list(result_queue)
    print('#{}'.format(cnt_t), end = ' ')
    print(*result_queue)
```

