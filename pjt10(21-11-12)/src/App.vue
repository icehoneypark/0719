<template>
  <div id="app">
    <div id="nav" style="display: flex; justify-content: space-between; padding: 0;">
      <!-- logo를 다른 것으로 변경해서 넣음 -->
      <img src="../src/assets/logo.png" alt="" style="height: 90px;">
      <div style="line-height: 90px;, height: 90px; padding: 0 10px 0;">
        <router-link to="/">Home</router-link>
        <router-link to="/random">Random</router-link>
        <router-link to="/my-movie-list">MyMovieList</router-link>
      </div>
    </div>
    <router-view/>
  </div>
</template>


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
  background-color: rgb(244, 239, 250);
}

#nav div a {
  font-weight: bold;
  color: #2c3e50;
  padding: 0 10px 0;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
