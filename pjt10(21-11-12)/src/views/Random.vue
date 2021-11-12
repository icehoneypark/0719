<template>
  <div>
    <button @click="getOne" style="margin: 30px 0 30px;">Pick</button>
    <div v-if="movieItem.poster_path" style="justify-content: center; display: flex;">
      <div style="border: solid; width: 336px;">
        <!-- 기존 str에 poster_path를 더하여 src에 입력 -->
        <img :src="'https://image.tmdb.org/t/p/w500' + movieItem.poster_path" alt="Image" class="rounded-0" style="width: 330px;">
        <h2>{{ movieItem.title }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Random',
  methods: {
    // 버튼 클릭 시 getOne함수 실행
    getOne: function () {
      this.$store.dispatch('getOne')
    }
  },
  // 시작 시 영화 리스트를 가져오는 함수 실행
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  // state에서 다음과 같은 값을 가져옴
  computed: {
    ...mapState([
      'movieCards',
      'movieItem'
    ]),
  }
}
</script>
<style>

</style>