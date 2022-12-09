<template>
  <NavBar />
  <div :style="{ 'margin-left': navbarWidth }">
    <router-view />
    <p></p>
  </div>
</template>


<script lang="ts">
import NavBar from './components/navbar/NavBar.vue';
import { navbarWidth } from './components/navbar/state';
export default {
  created() {
    this.fetchUserData()
  },
  components: { NavBar },
  data() {
    return {
      user: null,
    }
  },
  setup() {
    return { navbarWidth }
  },
  methods: {
    async fetchUserData(){
      let response = await fetch("http://localhost:8000/auctionapp/user",
      {
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
        method: "GET"
      });
      let data = await response.json()
      console.log(data.user_id)

    }
  }
}
</script>