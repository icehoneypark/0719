<template>
  <div id='items'>
    <!-- 영화 리스트에 따라 자식요소 출력 -->
    <!-- 반복문에는 key값이 필수, movie요소를 movie라는 이름으로 props -->
    <my-list-item
      v-for="(movie, idx) in movieList"
      :key="idx"
      :movie="movie"
    ></my-list-item>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MyListItem from '@/components/MyListItem'

export default {
  name:"MyList",
  components: {
    MyListItem,
  },
  // state에서 movieList값을 가져옴
  computed: {
    ...mapState([
      'movieList'
    ])
  },
}
</script>

<style>
  #items {
    margin-top: 0px;
    width: 1400px;
    background-color: rgb(255, 193, 247);
  }
</style>