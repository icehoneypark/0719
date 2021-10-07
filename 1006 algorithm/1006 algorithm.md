# 1. 트리 순회

```
예제 입력
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

예제 출력
ABDCEFG
DBAECFG
DBEGFCA
```

```python
def finder(node):
    global finder1
    global finder2
    global finder3
    if node =='.':
        return
    finder1 += node
    finder(left_lst[parents.index(node)])
    finder2 += node
    finder(right_lst[parents.index(node)])
    finder3 += node


n = int(input())

parents = list()
left_lst = list()
right_lst = list()

finder1 = ''
finder2 = ''
finder3 = ''

for _ in range(n):
    tmp1, tmp2, tmp3 = input().split()
    parents.append(tmp1)
    left_lst.append(tmp2)
    right_lst.append(tmp3)

finder(parents[0])

print(finder1)
print(finder2)
print(finder3)
```

