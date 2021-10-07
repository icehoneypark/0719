# 1. 앞글자따기

```
입력 :
3
5
samsung software academy for youth
4
as soon as possible
3
bang tan sonyundan

출력 :
#1 SSAFY
#2 ASAP
#3 BTS
```

```
t = int(input())

for cnt_t in range(1, t+1) :

    length = int(input())
    text = input()

    cp_text = text.title()
    result = ''
    for i in cp_text:
        if 'Z'>= i >= 'A' :
            result += i

    print('#{} {}'.format(cnt_t, result))
```



# 2. 문자열의 거울상

```
입력 :
2
bdppq
qqqqpppbbd	//전체 테스트 케이스 수
//첫 번째 테스트 케이스
//두 번째 테스트 케이스

출력 :
#1 pqqbd
#2 bddqqqpppp	// 첫 번째 테스트 케이스의 답
// 두 번째 테스트 케이스의 답
```

```
t = int(input())

for cnt_t in range(1, t+1) :

    text = list(input())

    half_length = len(text) // 2
    result = ''
    if len(text) % 2 :
        for cnt in range(half_length) :
            text[cnt], text[len(text)-1-cnt] = text[len(text)-1-cnt], text[cnt]
        for txt in text :
            result += txt
    else :
        for cnt in range(half_length):
            text[cnt], text[len(text) - 1 - cnt] = text[len(text) - 1 - cnt], text[cnt]
        for txt in text:
            result += txt
        pass

    result2 = ''

    for txt in result :
        if txt == 'q' :
            result2 += 'p'
        elif txt == 'p' :
            result2 += 'q'
        elif txt == 'b' :
            result2 += 'd'
        else :
            result2 += 'b'


    print('#{} {}'.format(cnt_t, result2))
```

# 3. 모음이 보이지 않는 사람

```
입력 :
3
congratulation
synthetic
fluid	// 테스트 케이스 개수
// 첫 번째 테스트케이스


출력 :
#1 cngrtltn
#2 synthtc
#3 fld	// 첫 번째 테스트케이스 답
```

```
t = int(input())

for cnt_t in range(1, t+1) :

    text = list(input())

    result = ''

    for i in text :
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
            pass
        else :
            result += i

    print('#{} {}'.format(cnt_t, result))
```



# 4. String1

```
def is_pattern(lst_list, list):

    cnt = 0
    result_cnt = 0


    for lst in lst_list :
        for i in range(len(lst)) :
            cnt = 0
            for j in range(len(list)) :
                if i+j<len(lst) :
                    if lst[i+j] == list[j] :
                        cnt += 1
                    if cnt == len(list) :
                        result_cnt += 1
    return result_cnt

t = 10

for cnt_t in range(1, t+1) :

    test = int(input())

    list2 = list(input())

    lst = input().split(',')

    result = is_pattern(lst, list2)

    print('#{} {}'.format(cnt_t, result))
```

# 5. GNS

```
t = int(input())

for _ in range(1, t+1) :

    trash = input().split()

    cnt_t = trash[0]

    num_en_list = list(input().split())

    zro_cnt = one_cnt = two_cnt = thr_cnt = for_cnt = fiv_cnt = six_cnt = svn_cnt = egt_cnt = nin_cnt = 0

    result = []

    for num_en in num_en_list :
        if num_en =='ZRO':
            zro_cnt += 1
        elif num_en =='ONE':
            one_cnt += 1
        elif num_en =='TWO':
            two_cnt += 1
        elif num_en =='THR':
            thr_cnt += 1
        elif num_en =='FOR':
            for_cnt += 1
        elif num_en =='FIV':
            fiv_cnt += 1
        elif num_en =='SIX':
            six_cnt += 1
        elif num_en =='SVN':
            svn_cnt += 1
        elif num_en =='EGT':
            egt_cnt += 1
        # elif num_en =='NIN':
        else :
            nin_cnt += 1

    for _ in range(zro_cnt) :
        result.append('ZRO')
    for _ in range(one_cnt) :
        result.append('ONE')
    for _ in range(two_cnt) :
        result.append('TWO')
    for _ in range(thr_cnt) :
        result.append('THR')
    for _ in range(for_cnt) :
        result.append('FOR')
    for _ in range(fiv_cnt) :
        result.append('FIV')
    for _ in range(six_cnt) :
        result.append('SIX')
    for _ in range(svn_cnt) :
        result.append('SVN')
    for _ in range(egt_cnt) :
        result.append('EGT')
    for _ in range(nin_cnt) :
        result.append('NIN')

    print(cnt_t)
    print(*result)
```

