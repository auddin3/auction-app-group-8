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
  setup() {
    return { navbarWidth }
  }

}
</script>