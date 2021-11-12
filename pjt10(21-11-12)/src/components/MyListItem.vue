<template>
  <div>
    <!-- isComplete 유무에 따라 class 변경 -->
    <h3 class="item" :class="{ 'completed': movie.isCompleted }" @click="updateMovie(movie)">{{ movie.title }}</h3>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name:"MyListItem",
  // 부모에서 movie값을 가져옴
  props: {
    movie: Object,
  },
  // actions를 map으로 가져옴
  methods: {
    ...mapActions([
      'updateMovie'
    ])
  }
}
</script>

<style>
/* isComplete가 True일 때 폰트 무게가 가벼워지고, 배경색이 변함 */
  .completed {
    font-weight: lighter;
    background-color: rgb(255, 246, 246);
  }
  .item  {
    margin: 0;
    line-height: 50px;
    font-size: 20px;
    height: 50px;
    width: 1400px;
  }
</style>