# 1. MTV

```
Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의
약자이며, 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는
역할을 간략히 서술하시오.
```

```
MTV(model-template-view)
```

```
MVC의 M(model) : MTV의 M(model) : 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
MVC의 V(view) : MTV의 T(template) : 파일의 구조나 레이아웃을 정의, 실제 내용을 보여주는데 사용(presentation)
MVC의 C(controller) : MTV의 V(view) : HTTP 요청을 수신하고 HTTP 응답을 반환, Model을 통해 요청을 충족시키는데 필요한 데이터에 접근, template에게 응답의 서식 설정을 맡김
```



# 2. URL

```
__(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을
의미한다. __(a)__는 무엇인지 작성하시오.
```

```
Variable Routing
```



# 3. Django template path

```
Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에
등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다.
__(a)__에 들어갈 폴더 이름을 작성하시오.
```

```
DIRS
```



# 4. Django Template Language

```
1) menu
2) forloop.counter0
3) empty
4) else
5) length, title
6) r
```



# 5. Form tag with Django

```
1) 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오.
2) 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.
3) input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.
```

```
1) action : 입력 데이터가 전송될 URL 지정
2) text
3) /안녕하세요/반갑습니다/파이팅/
```

