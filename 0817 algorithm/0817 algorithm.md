# 1. 글자 수

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

