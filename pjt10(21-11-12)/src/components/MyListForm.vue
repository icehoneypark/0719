<template>
  <div id="form">
    <h1>My Movie List</h1>
    <div>
      <!-- inputData를 양방향으로 연결, trim으로 공백 제거 -->
    <input type="text" v-model.trim="inputData" @keyup.enter="addMyList">
    <button @click="addMyList">Add</button>
    </div>
  </div>
</template>

<script>
export default {
  name:"MyListForm",
  data () {
    return {
      inputData: '',
    }
  },
  methods: {
    addMyList () {
      // 길이가 0 초과일 때 실행(입력값이 있음)
      if (this.inputData.length) {
        // actions에서 addMyList 함수 실행, inputData를 data로 전송
        this.$store.dispatch('addMyList', this.inputData)
        this.inputData=""
      }
      else {
        alert('영화를 입력해주세요')
      }
    }
  }
}
</script>

<style>
 #form {
  border-radius: 20px 20px 0 0;
  margin-top: 30px;
  width: 1400px;
  padding: 15px 0 15px;
  background-color: rgb(244, 239, 250);
 }
</style>