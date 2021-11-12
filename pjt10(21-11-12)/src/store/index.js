import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // TOP20 카드 리스트
    movieCards: [],
    // MyMovieList 영화 리스트
    movieList: [],
    // Random에서 사용된 영화
    movieItem: {}
  },
  mutations: {
    // movieList에 요소 append
    ADD_MY_LIST (state, data){
      const movie = {
        title: data,
        isCompleted: false,
      }
      state.movieList.push(movie)
    },
    
    // url에서 가져온 데이터를 movieCards에 대입
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    // 클릭에 따른 isCompleted 반전
    UPDATE_MOVIE (state, data){
      state.movieList = state.movieList.map(movie => {
        if (movie === data) {
          return {
            ...movie,
            isCompleted: !movie.isCompleted
          }
        }
        else {
          return movie
        }
      })
    },
    // Random에서 사용된 함수, movieCards 중 1개를 랜덤으로 선택
    GET_ONE(state){
      state.movieItem = _.sample(state.movieCards)
    }
  },
  // mutations에서 함수를 호출
  actions: {
    addMyList (context, data){
      context.commit("ADD_MY_LIST", data)
    },
    updateMovie (context, data){
      context.commit("UPDATE_MOVIE", data)
    },
    getOne(context) {
      context.commit("GET_ONE")
    },
    // axios를 사용하여 url에서 데이터를 가져옴
    LoadMovieCards: function ({commit}) {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: '6163fbe091536a27c8951c10ecb40d6c',
          language: 'ko-KR',
        }
      }).then((res) => {
        // 올바른 응답 시 가져온 데이터의 데이터의 결과들을 LOAD_MOVIE_CARDS에 data로 준 후 호출
        commit('LOAD_MOVIE_CARDS', res.data.results)
      })
    }
  },
  modules: {
  }
})
