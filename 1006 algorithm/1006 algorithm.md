# 1. 트리 순회

```
문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.



예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
```

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

