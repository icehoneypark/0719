# 1. 앞글자따기

```
[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 입력될 문자열의 개수 N 이 주어진다 ( 1 <= N <= 5)
두 번째줄에는 영어 소문자로 이루어진 N 개의 문자열이 주어진다.
각 문자열의 길이는 1이상 20이하이다.

[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
각 테스트 케이스 마다 입력으로 주어진 문자열의 앞글자를 대문자로 바꿔 순서대로 출력한다.
```

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
‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.

예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.

 

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 ‘b’, ‘d’, ‘p’, ‘q’만으로 이루어진 하나의 문자열이 주어진다. 문자열의 길이는 1이상 1000이하이다.

 

[출력]

각 테스트 케이스마다 주어진 문자열을 거울에 비춘 문자열로 출력한다.
```

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
불의의 교통사고를 당한 당신은 얼마 후 자신의 인식 속에서 모음이라는 것이 사라진 것을 알게 되었다.

알파벳 소문자 만으로 이루어진 단어를 당신은 어떤 식으로 보게 될까?

알파벳에서 모음은 ‘a’, ‘e’, ‘i’, ‘o’, ‘u’의 다섯가지로 예를 들어 “congratulation”이라는 단어를 당신이 보게 되면 “cngrtltn”으로 인식하게 될 것이다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 길이가 50이하이고 알파벳 소문자만으로 이루어진 단어가 주어진다. 이 단어에 모음이 아닌 문자(자음)이 적어도 하나는 들어있다는 것이 보장된다.

[출력]

테스트 케이스 T에 대한 결과는 “#T ”을 찍고,  각 테스트 케이스마다 주어진 단어를 당신이 어떻게 인식하는지를 출력한다.
```

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
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

위 문장에서 ti 를 검색하면, 답은 4이다.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.

문장의 길이는 1000자를 넘어가지 않는다.

한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.

한 문장에서는 하나의 문자열만 검색한다. 

[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
```

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
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.

그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.

그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.
```

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

