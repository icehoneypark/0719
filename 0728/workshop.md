# 1. pip

```
$ pip install faker

(1) 무엇을 위한 명령인지 : faker 패키지를 설치하기 위한 명령이다.
(2) 실행은 어디에서 해야하는지 : 사용하기 위한 환경(가상환경)에서 실행해야한다.
 - cli 환경에서 실행
```



# 2. Basic Usages

## (https://github.com/joke2k/faker#basic-usage)

```
from faker import Faker # 1 faker패키지의 Faker클래스 사용준비를 실행하기 위한 코드이다.
fake = Faker() # 2 Faker는 호출되는 함수, fake는 호출하는 객체이다.
fake.name() # 3 name()은 fake의 메서드이다.
```



# 3. Localization

## (https://github.com/joke2k/faker#localization)

```
class Faker() :
    def __init__(self, locale = 'en_US') :
        pass
        
__init__은 인스턴스 메서드이다. -> self를 첫 변수로 가져온다.
locale 정보니깐 locale로 설정하자. 그리고 기본설정인 'en_US'를 해준다.

1) 생정자 => 인스턴스 생성할 때 실행
2) 인스턴스 method => 첫번째 인자는 self이다.
3) 인스턴스가 생성될 때 인자가 있으면 그 값은 생성자로 들어간다.
```



# 4. Seeding the Generator

## (https://github.com/joke2k/faker#seeding-the-generator)

```
from faker import Faker

fake = Faker('ko_KR') # fake는 인스턴스 메서드
Faker.seed(4321) # Faker는 파스칼케이스 pascal == class => seed는 클래스 메서드

print(fake.name()) # 이도윤, name()은 인스턴스 메서드

fake2 = Faker('ko_KR')
print(fake2.name()) # 이지후
```

![image-20210728182809162](workshop.assets/image-20210728182809162.png)

```
seed(x)는 x 값에 따라 랜덤으로 형성되는 것의 기준을 잡는다. 이로 인해 seed(4321)로 줄 경우, 첫 랜덤이름은 이도윤, 그 다음은 이지후로 고정이 된다.
```

## 

```
from faker import Faker

fake = Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name()) # 이도윤

fake2 = Faker('ko_KR')
print(fake2.name()) # 이름이 계속해서 바뀜
```

```
seed(x)는 x 값에 따라 랜덤으로 형성되는 것의 기준을 잡는다. 이 기준은 이후의 랜덤에도 적용된다.
seed_instance(x)는 x 값에 따라 랜덤으로 형성되는 것의 기준을 잡는다. 이 기준은 다음에 나오는 랜덤 한번만 적용이 된다.

# seed()는 클래스 method => 클래스 변수가 변경되어 모든 인스턴스에 적용
# seed_instance()는 인스턴스 method => 인스턴스 변수가 변경되어 해당 인스턴스에 적용
```

