<template>
  <div style="justify-content: center; display: flex;">
    <div>
      <!-- 사용하기 -->
      <my-list-form></my-list-form>
      <my-list></my-list>
    </div>
  </div>
</template>

<script>
// 가져오기
import MyListForm from '@/components/MyListForm'
import MyList from '@/components/MyList'
export default {
  name:"MyMovieList",
  components: {
    // 등록하기
    MyListForm,
    MyList,
  }
}
</script>

<style>
</style>