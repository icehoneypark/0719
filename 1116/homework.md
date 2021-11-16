# Vue with server

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- DRF Server는 단순히 요청에 따라 데이터 및 인증을 처리하는 등의 역할만 담당할 뿐 반드시 Vue가 Client일 필요는 없다.
- Vue & DRF가 기존에 Django만 사용했을 때와 다른 점은 Django의 MTV 중 Template 부분을 Vue가 대체한 것이다. 
- 같은 localhost에서 활성화 되어있는 Django와 Vue.js 서버는 서로 제약없이 리소스를 요청하고 응답 받을 수 있다. 

```
(1) : T
(2) : T
(3) : F (port가 다르다)
```



### 2. Server-Client 구조의 애플리케이션에서 사용자 인증 기능을 구현하고자 한다. Client는 Vue 그리고 Server는 DRF를 이용하여 구현했다고 할 때, DRF에서 지원하는 세션 인증 방식과 토큰 인증 방식의 차이점을 서술하시오. 

```
세션 인증 방식 : session_id를 받아와 쿠키로 Browser에 전달한다. -> session_id 저장공간 필요, 저장 정보가 한정적이다.

토큰 인증 방식 : 저장정보를 가지고 있음, 서명정보 위변조 사실 확인가능, 확장성이 좋다.
```



### 3. DRF Server에서 JWT 인증 방식을 이용하여 사용자 인증 기능을 구현했다고 하자. 이 때, Client에서 인증이 필요한 API endpoint로 요청을 보내기 위해서는 JWT 값을 HTTP __(a)__ request header에 실어서 요청을 보내야 한다. __(a)__ request header의 이름과 특징을 작성하시오.

```
(a) Authorization
(Authorization: Bearer <token>)
서버의 자원에 대한 인증
```

