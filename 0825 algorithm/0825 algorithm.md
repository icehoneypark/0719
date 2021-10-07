# 1. 회전

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

