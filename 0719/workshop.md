# 1. 세로로 출력하기

```
number = int(input('자연수를 입력해주세요 : '))

number = range(1, number+1)

count = 0

for count in number:
    print(count)
```

# ![workshop 1](workshop.assets/workshop 1.png)

# 2. 거꾸로 세로로 출력하기

```
number = int(input('자연수를 입력해주세요 : '))

number = range(number, -1, -1)

sum = 0

count = 0

for count in number:
    print(count)
```

![workshop 2](workshop.assets/workshop 2.png)

# 3. N줄 덧셈

```
number = int(input('자연수를 입력해주세요 : '))

number = range(number+1)

sum = 0

count = 0

for count in number:
    sum = sum+count
    
else : print(sum)
```

![workshop 3](workshop.assets/workshop 3.png)

