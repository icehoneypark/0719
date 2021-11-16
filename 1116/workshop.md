# Vue with server

### - Background

```
* Vue
* Django
```

### - Goal

```
* Django와 Vue를 활용한 Client/Server에 대한 이해
* JWT Based Authentication에 대한 이해
```

### - Problem

❖ 이전 workshop 프로젝트에 이어서 JWT를 사용해 아래 요구사항을 만족하는 프로젝트를 구현하시오. 

 	1. User(1)와 Todo(N)는 1:N model relationship을 가짐 
 	2. 회원가입, 로그인, 로그아웃 
 	3. 인증된 사용자만 Todo API를 모두 사용할 수 있음 (회원가입 예외)

❖ 참고 문서 

​	https://jpadilla.github.io/django-rest-framework-jwt/ 

​	https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User.set_password 

​	https://www.django-rest-framework.org/api-guide/fields/#write_only 

​	https://www.django-rest-framework.org/api-guide/settings/#api-reference

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> | 
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
        <router-link :to="'#'" @click.native="Logout">Logout</router-link> 
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </span>
    </div>
    <router-view @login="setLogin"/>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    setLogin: function () {
      this.isLogin = true
    },
    created: function () {
      if (localStorage.getItem('JWT')) {
        this.isLogin = true
      } else {
        this.$router.push({ name: 'Login' }).catch(()=> {})
      }
    },
    Logout: function () {
        localStorage.removeItem('JWT')
        this.isLogin = false
        this.$router.push({ name: 'Login'})
    }
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
```

```
<!-- TodoList.vue -->
<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span 
          @click="updateTodoStatus(todo)" 
          :class="{ completed: todo.completed }"
        >
        {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem('JWT')
      const header = {
        Authorization: `Bearer ${token}`
      }
      return header
    },
    getTodos: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
        headers: this.setHeader(),
      })
        .then(res => {
          console.log(res)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      // 3번 문제
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        headers: this.setHeader(),
      })
      .then(res => {
        console.log(res)
        this.getTodos()
      })
      .catch(err => {
        console.log(err)
      })
    },
        
    updateTodoStatus: function (todo) {
    // 4번 문제
      const todoItem = {
        ...todo,
        completed: !todo.completed
      }

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem,
        headers: this.setHeader(),
      })
      .then(res => {
        console.log(res)
        todo.completed = !todo.completed
      })
    }
  },
  created: function () {
    this.getTodos()
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
```

```vue
<!-- CreateTodo.vue -->
<template>
  <div>
    <input 
      type="text" 
      v-model="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem('JWT')
      const header = {
        Authorization: `Bearer ${token}`
      }
      return header
    },
    createTodo: function () {
      // 2번 문제
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/todos/',
        data: {
          title: this.title,
        },
        headers: this.setHeader(),
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'TodoList' })
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>
```

```vue
<!-- Signup.vue -->
<template>
  <div>
    <h2>Sign up</h2>
    <hr>
    <div>
      <label for="username">사용자 아이디:</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호:</label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="password2">비밀번호 확인 : </label>
      <input 
        type="password" 
        id="password2" 
        @keyup.enter="signup" 
        v-model="credentials.password2">
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        password2: '',
      }
    }
  },
  methods: {
    signup: function () {
      console.log('회원가입')
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/signup/`,
        data: this.credentials
      })
      .then (res => {
        console.log(res)
        this.$router.push({ name: 'Login' })
      })
      .catch (err => {
        console.log(err)
      })
    }
  }
}
</script>
```

```vue
<!-- Login.vue -->
<template>
<div>
  <h2>로그인</h2>
  <hr>
  <div><label for="username">아이디 :</label>
    <input type="text" id="username" v-model="credentials.username">
  </div>
  <div>
    <label for="password"> 비밀번호: </label>
    <input type="password" id="password" v-model="credentials.password"
    @keyup.enter="login">
  </div>
    <button @click="login">로그인</button>
</div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        errMsg: '',
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api/token/`,
        data: this.credentials
      })
      .then (res => {
        console.log(res)
        localStorage.setItem('JWT', res.data.access)
        this.$emit('login')
        this.$router.push({ name: 'TodoList' })
      })
      .catch (err => {
        console.dir(err.response.data)
        this.errMsg = err.response.data
      })
    }
  }
}
</script>
```

