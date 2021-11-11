# Vuex

### - Background

```
* Vue
```

### - Goal

```
* Vuex에 대한 이해
```

### - Problem

❖ Vue CLI 및 Vuex를 활용하여 아래 구조에 맞는 todo 프로젝트를 완성하시오. (각 todo는 브라우저 새로고침 시 사라지지 않음)

```js
// index.js
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todoList: [
      // Todo dummy Data
      // {
      //   content: '할 일 1',
      //   isCompleted: false,
      // },
      // {
      //   content: '할 일 2',
      //   isCompleted: true,
      // },
    ]
  },
  // 금고관리인
  mutations: {
    // CREATE_TODO: function (state, todoItem) {
    //   state.todoList.push(todoItem)
    // },
    // todoList가 array니깐 push
    ADD_TODO: function (state, data) {
      const todo = {
        content: data,
        isCompleted: false,
      }
      state.todoList.push(todo)
    },
    DELETE_TODO (state, data){
      const idx = state.todoList.indexOf(data)
      state.todoList.splice(idx, 1)
    },
    UPDATE_TODO (state, data){
      state.todoList = state.todoList.map(todo => {
        if (todo === data) {
          return {
            ...todo, // Spread Syntas
            // content: todoItem.content,
            isCompleted: !todo.isCompleted
          }          
        } else {
          return todo
        }        
      })
    }
  },
  // 데스크 은행원
  actions: {
    // createTodo: function (context, todoItem) {
    //   context.commit('CREATE_TODO', todoItem)
    // },
    addTodo: function (context, data) {
      context.commit("ADD_TODO", data)
    },
    deleteTodo({commit}, data) {
      commit("DELETE_TODO", data)
    },
    // updateTodo ({commit}, data){
    //   commit('UPDATE_TODO', data)
    // },
    updateTodo: function (context, data) {
      context.commit('UPDATE_TODO', data)
    }
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todoList.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todoList.filter(todo => {
        return todo.isCompleted === false
      }).length
    },
    allTodosCount: function (state) {
      return state.todoList.length
    }
  },
  modules: {
  },
})
```

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <todo-list></todo-list>
    <todo-form></todo-form>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
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
  margin-top: 60px;
}
</style>
```

```vue
<!-- TodoListItem.vue -->
<template>
  <div>
    <!-- <span class="mx-3" :class="{'completed': todo.isCompleted}" @click="updateTodo">{{ todo.content }}</span> -->
    <span class="mx-3" :class="{'completed': todo.isCompleted}" @click="updateTodo(todo)">{{ todo.content }}</span>
    <!-- <button @click="deleteTodo">Delete</button> -->
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name:'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    ...mapActions([
      'deleteTodo',
      'updateTodo',
    ]),
    // deleteTodo: function () {
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
    // updateTodo () {
    //   this.$store.dispatch('updateTodo', this.todo)
    // }
  }
}
</script>

<style scoped>
  .completed {
    text-decoration: line-through;
  }
</style>
```

```vue
<!-- TodoList.vue -->
<template>
  <div>
    <h1>TodoList</h1>
    <h2>All Todo: {{ allTodosCount }}</h2>
    <h2>Completed Todo: {{ completedTodosCount }}</h2>
    <h2>Uncompleted Todo: {{ uncompletedTodosCount }}</h2>
      <!-- v-for="(todo, idx) in $store.state.todoList" -->
    <todo-list-item
      v-for="(todo, idx) in todoList"
      :key="idx"
      :todo="todo"
    ></todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
// import TodoListItem from './TodoListItem.vue'
import { mapState } from 'vuex'
import { mapGetters } from 'vuex'

export default {
  name: 'TodoList',
  components: { 
    TodoListItem ,
  },
  computed: {
    ...mapState([
      'todoList',
    ]),
    ...mapGetters([
      'allTodosCount',
      'completedTodosCount',
      'uncompletedTodosCount'
    ])
    // todos: function () {
    //   return this.$store.state.todoList
    // },
    // completedTodosCount: function () {
    //   return this.$store.getters.completedTodosCount
    // },
    // uncompletedTodosCount: function () {
    //   return this.$store.getters.uncompletedTodosCount
    // },
    // allTodosCount: function () {
    //   return this.$store.getters.allTodosCount
    // },
  }
}
</script>

<style>

</style>
```

```vue
<!-- TodoForm.vue -->
<template>
  <div>
    <input class="my-3" type="text" v-model.trim="inputData" @keyup.enter="addTodo">
    <!-- <input class="my-3" type="text" v-model.trim="todoContent" @keyup.enter="createTodo"> -->
    <!-- <button @click="createTodo">Add</button> -->
    <button @click="addTodo">Add</button>
  </div>
</template>

<script>
export default {
  name:'TodoForm',
  data: function () {
    return {
      inputData: '',
    }
  },
  methods: {
    // createTodo: function () {
    //   const todoItem = {
    //     content: this.todoContent,
    //     isCompleted: false,
    //   }
    //   if (todoItem.content) {
    //     this.$store.dispatch('createTodo', todoItem)
    //   }
    // },
    // addTodo () {},
    addTodo: function () {
      // vuex에 저장하도록 한다.
      if (this.inputData.length) {
      this.$store.dispatch('addTodo', this.inputData)
      // 저장했으면 입력값 초기화
      this.inputData = ''
      } else {
        alert('할 일을 입력해주세요.')
      }
    }
  }
}
</script>

<style scoped>
  .my-3 {
    margin-top: 20px;
  }
</style>
```





