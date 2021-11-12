<template>
  <div class="home">
    <div style="justify-content: center; display: flex;">
      <div class="d-flex row" style="width: 1200px;">
        <!-- 부트스트랩 사용으로 카드형식으로 출력 -->
        <movie-card class="col-4"
          v-for="movieCard in movieCards"
          :key="movieCard.id"
          :movieCard="movieCard"
          style="padding-top: 30px;"
        >
        </movie-card>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  // 시작 시 LoadMovieCards 함수 실행
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  // state에서 movieCards값을 가져옴
  computed: {
    ...mapState(['movieCards'])
  }
}
</script>
