<template>
  <div>
    <div id="card">
      <!-- 부트스트랩을 사용하여 카드 내용을 출력 -->
      <b-card no-body class="overflow-hidden" style="max-width: 300px;  height: 700px;">
        <b-row no-gutters>
          <!-- 기존 str에 poster_path를 추가하여 src에 입력 -->
            <b-card-img :src="'https://image.tmdb.org/t/p/w500' + movieCard.poster_path" alt="Image" class="rounded-0" style="width: 330px;"></b-card-img>
            <b-card-body :title="movieCard.title">
              <!-- style에서 글자수가 제한 높이를 초과할 시 생략하는 overflow: hidden 사용 -->
              <b-card-text class="fw-bold text-align-start" style="overflow: hidden; font-size: 15px;">
                {{ movieCard.overview }}
              </b-card-text>
            </b-card-body>
        </b-row>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object
  },
}
</script>

<style>
</style>