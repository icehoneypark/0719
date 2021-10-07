# 1. 탈주범 검거

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

