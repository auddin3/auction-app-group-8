<template>
  <NavBar />
  <div :style="{ 'margin-left': navbarWidth }">

    <router-view />
  </div>
</template>


<script lang="ts">
import NavBar from './components/navbar/NavBar.vue';
import { navbarWidth } from './components/navbar/state';
export default {
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
      let response = await fetch("http://localhost:8000/auctionapp/",
      {
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
        method: "GET"
      });
      console.log(response)

    }
  }
}
</script>