# 1. Type Class

```
1. <class 'int'>
2. <class ' float'>
3. <class 'str'>
4. <class 'list'>
5. <class 'tuple'>
```



# 2. Magic Method

```
1. __init__ : 생성자(constructor) - 인스턴스 객체가 생성될 때 호출되는 메서드
2. __del__ : 소멸자(destructor) - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드
3. __str__ : str(object)와 내장 함수 format(), print()에 의해 호출되어 객체(비형식적인) 또는 보기 좋게 인쇄 가능한 문자열 표현을 계산하는 메서드
 - print()할 때 보여지는 문자열 반환, 외부노출 (사용자한테도 보임, all())
4. __repr__ : repr() 내장 함수에 의해 호출되어 객체(형식적인)의 문자열 표현을 계산하는 메서드
 - 인스턴스의 정보에 대한 값을 반환(개발자가 개발 중 인스턴스의 값을 확인할 때), 내부용(only develop)
```



# 3. Instance Method

```
1. items() : 딕셔너리의 Key와 Value값을 반환한다.
2. get(x) : 딕셔너리의 Key(x)의 Value값을 반환한다.
3. clear() : 딕셔너리의 Key와 Value값 모두 지운다.

string : upper, lower, title, split, joinm strip
list : count, pop, reverse, index, append, extend, sort
dict : update, items, 
```



# 4. Module Import

```
from fibo import fibo_recursion as recursion

from (모듈, 패키지) import (모듈에 포함된 함수) as (이 함수의 별명)



fibo.py = 파이썬 파일로 된 모듈

```



