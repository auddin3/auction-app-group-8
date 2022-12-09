<template>
  <NavBar />
  <div :style="{ 'margin-left': navbarWidth }">
    <router-view this.user="user" this.user_id="user_id" />
/>
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
      user_id: null,
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
      this.user = data.user
      this.user_id = data.user_id
      console.log(data.user_id)

    }
  }
}
</script>