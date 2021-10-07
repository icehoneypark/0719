# 1. 스택 연습

```
입력
1 // 테스트케이스 수
7 // 첫번째 테스트케이스의 명령어 수
i 7
i 5
c
o
o
o
c

출력
#1
2
5
7
empty
0
```

```
t = int(input())

for cnt_t in range(1, t+1) :
    print('#{}'.format(cnt_t))
    n = int(input())

    stack_list = []

    for _ in range(n) :
        data = input()
        data = list(data)
        if data[0] == 'i' :
            stack_list.append([data[2]])
        elif data[0] == 'c' :
            print(len(stack_list))
        else :
            if len(stack_list) == 0 :
                print('empty')
            else :
                print(*stack_list.pop())
```

# 2. 파스칼의 삼각형

```
입력
1
4
 
출력
#1
1
1 1
1 2 1
1 3 3 1
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    n = int(input())
    tree = []
    for _ in range(n) :
        tree.append([1])
    if n <= 1 :
        pass
    else :
        tree[1].append(1)
        if n == 2 :
            pass
        else :
            for y in range(2, n) :
                for x in range(1, y) :
                    tmp = tree[y-1][x-1] + tree[y-1][x]
                    tree[y].append(tmp)
                tree[y].append(1)

    print('#{}'.format(cnt_t))
    for tree_val in tree :
        print(*tree_val)
```

