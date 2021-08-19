# 1. 스택 연습

```
스택을 구현하고 명령어에 맞도록 처리해주는 프로그램을 작성해 주세요.

<명령어>
1. "i a"는 a라는 수를 스택에 넣는 명령이다. a 는 10000 이하의 자연수이다.
2. "o" 은 스택에서 데이터를 빼고, 그 데이터를 출력합니다. 만약 스택이 비어있으면, "empty"를 출력합니다.
3. "c" 는 스택에 쌓여있는 데이터의 수를 출력합니다. 

[입력]
첫번째줄에는 테스트케이스의 수가 입력됩니다. 그 다음줄에 이어서 총 T 개의 테스트케이스가 입력됩니다. 
각 테스트케이스별로 첫 줄에 N이 주어집니다. N은 명령어의 수입니다. (1 <= N <= 100)
다음 줄부터는 N개의 명령어가 입력되고 한줄에 하나가 입력됩니다.

[출력]
각 테스트케이스별로 첫째줄에는 #T 를 출력합니다 (T는 테스트케이스번호이고 1번부터 시작)
두번째 줄부터는
각 명령어에대해 올바르게 처리하여 한줄에 하나를 출력합니다.
출력내용이 하나도 없는 경우는 주어지지 않습니다. 
```

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
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,
 


N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.


[제약 사항]

파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.

삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```

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

