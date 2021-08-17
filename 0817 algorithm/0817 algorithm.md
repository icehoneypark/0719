# 1. 글자 수

```
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력:
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
 
출력:
#1 2
#2 1
#3 3
```

```
t = int(input())

for cnt_t in range(1, t+1) :
    str1 = list(input())
    str2 = list(input())


    setlist_str1 = list(set(str1))

    str1_dict = {}

    for str_key in setlist_str1 :
        str1_dict[str_key] = 0
        for str2_value in str2 :
            if str_key == str2_value :
                str1_dict[str_key] += 1

    value_max = 21e-8
    for key in str1_dict :
        if value_max < str1_dict[key] :
            value_max = str1_dict[key]

    print('#{} {}'.format(cnt_t, value_max))
```

# 2. 회문

```
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
 

예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
 
[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ
 
출력
#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT
```

```
t = int(input())

for cnt_t in range(1, t+1) :
    n , m = map(int, input().split())

    lst = []
    tmp_lst = []
    for _ in range(n) :
        tmp = list(input())
        lst.append(tmp)

    result = 0
    result_value = ''


    for lst_value in lst :
        for cnt_cnt in range(n-m+1) :
            tmp_lst1 = []
            tmp_lst2 = []
            for cnt_tmp in range(m) :
                tmp_lst1.append(lst_value[cnt_tmp+cnt_cnt])
                tmp_lst2.insert(0, lst_value[cnt_tmp+cnt_cnt])
            if tmp_lst1 == tmp_lst2 :
                for lst2_value in tmp_lst2 :
                    result_value += lst2_value
                result = 1
                print('#{} {}'.format(cnt_t, result_value))


    if result == 0 :
        for x in range(n) :
            for cnt_cnt in range(n-m+1) :
                tmp_lst1 = []
                tmp_lst2 = []
                for cnt_tmp in range(m) :
                    tmp_lst1.append(lst[cnt_tmp+cnt_cnt][x])
                    tmp_lst2.insert(0, lst[cnt_tmp+cnt_cnt][x])
                if tmp_lst1 == tmp_lst2 :
                    for lst2_value in tmp_lst2 :
                        result_value += lst2_value
                    print('#{} {}'.format(cnt_t, result_value))
                    break
```

# 3. 문자열 비교

```
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
 

ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
 

ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
 

다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
```

```
입력
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

출력
#1 1
#2 0
#3 1
```

```
t = int(input())

for cnt_t in range(1, t+1) :
    str1 = input()
    str1 = list(str1)

    str2 = input()
    str2 = list(str2)

    result = 0

    for cnt in range(len(str2)-len(str1)+1) :
        if str2[cnt] == str1[0] :
            result_cnt = 0
            for cnt_2 in range(len(str1)) :
                if str2[cnt+cnt_2] == str1[cnt_2] :
                    result_cnt += 1
                else :
                    break
                if result_cnt == len(str1) :
                    result += 1

    print('#{} {}'.format(cnt_t, result))
```

# 4. 쇠막대기 자르기

```
여러 개의 쇠막대기를 레이저로 절단하려고 한다.

효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.

쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

 - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.

 - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.

 - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.

 - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

아래 그림은 위 조건을 만족하는 예를 보여준다.

수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향이다.

 

이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.

    1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 “()” 으로 표현된다. 또한, 모든 “()”는 반드시 레이저를 표현한다.

    2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현된다.

위 예의 괄호 표현은 그림 위에 주어져 있다.

쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고,

이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.

쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

[출력]

각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 잘려진 조각의 총 개수를 출력한다.
```

```
입력
2
()(((()())(())()))(())
(((()(()()))(())()))(()())	//전체 TC 개수
//첫 번째 TC
//두 번째 TC

출력
#1 17
#2 24	//첫 번째 TC의 출력
//두 번째 TC의 출력
```

```
# 반복문 하나만 쓴 코드
t = int(input())
for cnt_t in range(1, t+1):
    datas = list(input())
    length = len(datas)
    div_sum = 0
    count_open = 0
    result = 0
    for open_cnt in range(length) :
        if datas[open_cnt] == '(' :
            count_open += 1
        else :
            if count_open == 1 :
                if datas[open_cnt - 1] != '(':
                    div_sum += 1
                count_open = 0
            else :
                count_open -= 1
                if datas[open_cnt - 1] == '(' :
                    div_sum += count_open
                else :
                    div_sum += 1
    print('#{} {}'.format(cnt_t, div_sum))
```

```
# 반복문 두개 쓴 코드
t = int(input())
for cnt_t in range(1, t+1):
    datas = list(input())
    length = len(datas)
    div_sum = 0
    for open_cnt in range(length-1) :
        if datas[open_cnt] == '(' :
            if datas[open_cnt+1] == ')' :
                pass
            else:
                div = 1
                count = 1
                for close_cnt in range(open_cnt + 1, length) :
                    if datas[close_cnt] == '(' :
                        count += 1
                    else :
                        if datas[close_cnt-1]=='(' :
                            div += 1
                        count -= 1
                    if count == 0 :
                        div_sum += div
                        break
    print('#{} {}'.format(cnt_t, div_sum))
```



# 5. 가장 빠른 문자열 타이핑

```
어떤 문자열 A를 타이핑하려고 한다.

그냥 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 할 것이다.

여기에 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.

이미 타이핑 한 문자를 지우는 것은 불가능하다.

예를 들어 A=”asakusa”, B=”sa”일 때, 다음 그림과 같이 B를 두 번 사용하면 5번 만에 A를 타이핑 할 수 있다.
 


A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하여라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스마다 첫 번째 줄에 두 문자열 A, B가 주어진다. A의 길이는 1이상 10,000이하, B의 길이는 1이상 100이하이다.


[출력]

각 테스트 케이스마다 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 출력한다.
```

```
입력
2
banana bana
asakusa sa	//Test Case의 개수
//A=”banana”, B=”bana”
//A=”asakusa”, B=”sa”

출력
#1 3
#2 5	//Test Case 1번의 답
//Test Case 2번의 답
```

```
t = int(input())

for cnt_t in range(1, t+1) :
    a, b = input().split()
    a = list(a)
    b = list(b)

    same_cnt = 0
    cnt_switch = 1

    while cnt_switch :
        if len(a) < len(b) :
            break
        for cnt in range(len(a)-len(b)+1) :
            check = a[0+cnt : len(b)+cnt]
            if check == b :
                for _ in range(len(b)) :
                    del a[cnt]
                same_cnt += 1
                break
            if cnt == len(a) - len(b) :
                cnt_switch = 0

    result = len(a) + same_cnt

    print('#{} {}'.format(cnt_t, result))
```

# 6. 회문2

```
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
 

 

위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.

예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.

[제약사항]

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.

글자 판은 무조건 정사각형으로 주어진다.

ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.

가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다. 
 


[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.
```

```
for cnt_t in range(1, 11) :
    tsh = input()
    lst = []
    for i in range(100) :
        lst.append(list(input().strip('')))

    max_length = 21e-8
    for y in range(100) :
        for x in range(99) :
            x_list1 = []
            x_list2 = []
            for x_cnt in range(x, 100) :
                x_list1.append(lst[y][x_cnt])
                x_list2.insert(0, lst[y][x_cnt])
                # print(x_list1)
                # print(x_list2)
                if x_list1 == x_list2 :
                    if max_length < len(x_list2) :
                        max_length = len(x_list2)

    for x in range(100) :
        for y in range(99) :
            y_list1 = []
            y_list2 = []
            for y_cnt in range(y, 100) :
                y_list1.append(lst[y_cnt][x])
                y_list2.insert(0, lst[y_cnt][x])
                if y_list1 == y_list2 :
                    if max_length < len(y_list2) :
                        max_length = len(y_list2)

    print('#{} {}'.format(cnt_t, max_length))
```

# 7. 마법사의 사냥

```
N x N 사각형의 전투장에는 각 칸마다 몇 마리의 몬스터가 있는지 적혀 있다.

광대한 영역에 마법을 시전할 수 있는 마법사 baldMort 는 전투장에서 최대한 많은 몬스터를 잡으려한다.

 

마법사baldMort는 대각선 좌상, 우상 ,좌하 , 우하 방향으로 각 방향마다 K 칸 만큼 마법을 시전할 수 있다.

마법은 마법사가 있는 지점에서 마법을 시전한 위치를 제외하고

대각선 좌상, 우상 ,좌하 , 우하 방향으로 방향 변화 없이 시전된다.

예를들어 [그림1]와 같은 5 x 5 인 전투장에서

노란색으로 표시된 2번 행 2번 열에서 K = 2 인 마법을 시전하게되면

각 방향마다 2칸씩 , [그림2] 와 같이 몬스터를 공격하게 되며

총 1 + 10 + 7 + 2 + 2 + 2 + 1 + 1 = 26 마리를 처치하게 된다.

반면에 [그림3]와 같이 0번 행 2번 열에서 K = 2인 마법을 시전하면 [그림4] 와 같이 좌하, 우하 방향 K칸에 해당되는몬스터를 공격하게 되며

총 7 + 2 + 0 + 7 = 16 마리 몬스터를 처치할 수 있다.

 

마법사 baldMort 씨가마법을 한번 시전하여처치할수 있는 몬스터의 최대 수를 출력하시오.


[입력]
5개의 테스트 케이스가 입력됩니다.
각 테스트케이스별로 첫째줄에 전투장의 가로세로크기인 N 이 입력된다. (1 <= N <= 100)

다음 줄부터는 N 줄에 걸쳐 각줄마다 N개의 정수가 공백으로 구분되어 입력된다. ( 0<= 정수 <= 100000)

마지막 줄에는 마법의 시전범위 K 가 입력된다. (1 <= K <= 100)


[출력]
마법사가 잡을 수 있는 몬스터의 최대 수를 출력하시오.
출력은 #테스트케이스번호 정답 으로 출력합니다.
```

```
입력
5 // N
4 3 5 0 0
9 5 5 1 2
5 9 9 3 5
10 1 1 1 10
10 6 5 5 1
2 // K
5
10 10 10 4 1
2 0 10 0 9
1 4 0 8 9
4 7 5 3 2
4 9 7 8 6
2
7
5 4 3 2 4 0 5
2 4 5 2 0 2 5
4 1 3 3 1 4 5
0 3 5 4 5 1 4
5 5 2 4 3 2 1
1 0 0 2 3 4 5
3 2 5 4 4 3 4
100
20
21 4 15 19 61 48 20 79 55 37 64 61 68 78 39 33 79 29 57 55
60 10 48 72 57 85 42 38 12 4 22 82 99 24 44 46 57 1 92 18
56 71 57 70 26 6 13 79 65 61 49 56 43 29 56 24 32 23 60 39
37 51 85 11 34 23 30 19 74 58 95 2 1 20 7 9 3 90 37 0
89 14 69 99 2 49 25 70 84 92 70 84 75 75 25 84 68 57 70 98
71 9 71 29 20 50 61 14 17 51 28 0 19 64 80 93 17 100 45 30
51 31 11 35 69 83 97 88 26 18 6 42 43 65 32 17 46 69 81 47
83 60 78 60 76 83 93 17 62 30 47 90 84 80 54 14 98 6 46 37
0 31 37 86 82 96 73 28 31 5 54 2 90 29 63 100 10 58 58 58
40 48 91 24 74 75 14 79 62 47 11 62 59 33 81 44 100 54 83 55
28 73 4 3 7 9 27 100 0 15 86 62 3 21 62 62 53 33 94 46
54 59 62 4 12 35 30 43 94 25 23 53 71 33 84 1 38 51 100 56
80 87 4 31 26 85 71 54 11 39 76 32 49 84 66 40 71 23 48 44
8 57 75 26 52 51 56 57 68 79 97 76 6 66 9 15 39 20 41 42
89 81 63 50 5 39 0 83 89 1 0 28 36 43 63 82 57 63 73 52
45 33 46 17 10 33 57 3 23 58 93 79 95 86 93 38 72 12 96 8
39 28 80 94 43 88 46 38 26 36 45 3 73 3 8 81 9 61 59 52
88 50 49 5 21 39 17 24 75 35 96 24 41 66 62 86 89 35 49 52
10 13 100 23 40 35 1 31 93 12 97 4 98 8 56 2 47 55 37 53
54 15 86 98 2 100 66 34 65 84 22 91 76 64 82 61 3 98 10 28
5
20
9 59 18 17 25 17 86 95 1 84 86 1 24 3 74 47 13 92 59 5
40 10 50 48 61 69 85 28 22 68 34 41 21 43 70 90 85 19 88 48
14 76 32 87 5 3 49 32 80 44 57 62 80 4 85 76 25 86 100 100
23 51 97 82 27 68 1 2 84 43 87 87 29 94 90 8 47 95 1 73
23 22 1 17 64 16 90 100 39 11 15 100 62 92 16 28 31 99 36 8
82 91 10 84 91 71 90 19 90 54 55 62 80 96 12 84 95 5 43 25
87 84 28 18 14 81 4 40 22 53 38 41 87 28 97 18 15 1 44 11
31 27 4 10 52 11 20 60 6 14 74 4 81 73 47 92 30 86 45 93
44 7 43 18 36 83 64 55 17 12 66 85 87 90 36 20 61 17 44 31
66 67 45 42 100 22 69 9 62 63 9 88 40 31 26 36 30 40 79 92
25 48 94 96 63 21 7 22 40 62 3 26 38 82 37 55 85 10 7 72
78 84 58 98 30 52 43 15 39 18 66 73 84 60 70 87 55 58 5 44
53 14 34 68 3 92 5 16 6 84 25 14 84 83 43 18 44 46 7 15
74 16 74 87 11 98 10 30 67 79 95 5 64 18 63 97 41 20 93 12
89 64 52 10 5 47 81 36 5 39 60 14 100 22 70 3 97 32 46 77
80 47 43 63 7 35 57 10 29 13 55 92 27 72 62 10 88 17 72 42
0 4 95 45 10 28 18 65 4 49 47 38 68 3 52 27 1 31 76 17
2 46 81 58 81 58 31 61 81 52 98 67 53 82 76 22 24 8 18 98
58 7 13 32 37 60 100 82 63 18 65 24 62 45 6 75 97 5 22 23
62 47 91 2 12 21 68 16 98 36 85 57 69 38 28 3 31 23 70 37
12

출력
#1 35
#2 45
#3 38
#4 1224
#5 1881
```

```
for cnt_t in range(1, 6) :
    n = int(input())
    monster_list = []
    for _ in range(n) :
        monster_list.append(list(map(int, input().split())))
    k = int(input())

    max_damage = 21e-8

    for y in range(n) :
        for x in range(n) :
            damage = 0
            for dtn in range(1, k+1) :
                if y + dtn < n and x + dtn < n :
                    damage += monster_list[y + dtn][x + dtn]
                if y - dtn >= 0 and x + dtn < n :
                    damage += monster_list[y - dtn][x + dtn]
                if y + dtn < n and x - dtn >= 0 :
                    damage += monster_list[y + dtn][x - dtn]
                if y - dtn >= 0 and x - dtn >= 0 :
                    damage += monster_list[y - dtn][x - dtn]
            if max_damage < damage :
                max_damage = damage
    print('#{} {}'.format(cnt_t, max_damage))
```

# 8. 의석이의 세로로 말해요

```
아직 글을 모르는 의석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.

이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 의석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.

다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다. 아래에 의석이가 칠판에 붙여 만든 단어들의 예가 있다.
 

A A B C D D

a f z z

0 9 1 2 1

a 8 E W g 6

P 5 h 3 k x

 

만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.
 

심심해진 의석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.

세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다.

이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.

위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.

그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다.

위에서 의석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:

 

Aa0aPAf985Bz1EhCz2W3D1gkD6x

 

칠판에 붙여진 단어들이 주어질 때, 의석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하라.

 

[입력]
 

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
 

각 테스트 케이스는 총 다섯 줄로 이루어져 있다.

각 줄에는 길이가 1이상 15이하인 문자열이 주어진다. 각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.
 

[출력]
 

각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 의석이가 세로로 읽은 순서대로 글자들을 출력한다.
```

```
입력
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx


출력
#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x	//TC #1의 정답               
 
```

```
t = int(input())
for cnt_t in range(1, t+1) :
    words_list = []
    for _ in range(5) :
        words_list.append(list(input().strip(',')))

    result_list = []
    for _ in range(5) :
        result_list.append(['None']*15)

    for y in range(5) :
            for x in range(len(words_list[y])) :
                result_list[y][x] = words_list[y][x]

    speak = ''

    for x in range(15) :
        for y in range(5) :
            if result_list[y][x] != 'None' :
                speak += str(result_list[y][x])

    print('#{} {}'.format(cnt_t, speak))
```

