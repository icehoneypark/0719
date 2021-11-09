# Vue CLI

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Vue의 Life Cycle Hook에서 created Hook은 Vue template에 작성한 요소들이 DOM에 모두 그려지는 시점에 실행된다.
- npm은 Node Package Manager의 약자이며, npm을 통해 설치한 package 목록은 package.json 파일에 자동으로 작성된다.
- Vue CLI를 통해 만든 프로젝트는 브라우저가 아닌 node.js 환경이기 때문에 DOM 조작이나 Web API 호출 등 Vanilla JS에서의 기능을 사용할 수 없다. 

```
(1) : F (Vue template 생성 시기가 created Hook이며 DOM에 그려지는(합쳐지는) 시기는 mounted 이다.)
(2) : T
(3) : F (Vue CLI를 통해 만든 프로젝트는 브라우저 환경이다.)
```



### 2. Vue Router에서 설정하는 history mode가 무엇을 뜻하는지 서술하시오. 

```
HTML History API를 사용해서 router를 구현한 것
브라우저의 히스토리는 남기지만 실제 페이지는 이동하지 않는 기능을 지원
Vue Router에는  Hash(default)모드와 History모드가 있는데 Hash는 #를 사용하여 사용자들에게 익숙하지 않는 형태라 History모드를 사용한다.
History모드는 url을 입력하여 요청하면 실제 페이지 이동없이 (새로고침 없이)페이지 변환이 가능하다. 그리고 log가 남기 때문에 전 페이지, 후 페이지 이동이 가능하다.
```



### 3. Vue Life Cycle Hook을 참고하여, 다음 Vue application을 실행했을 때, console 창에 출력되는 메시지를 작성하시오.

![image-20211108173822723](homework.assets/image-20211108173822723.png)

```
created!
mounted!
```

