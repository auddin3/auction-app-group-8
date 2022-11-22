<template>
  <NavBar />
  <div :style="{ 'margin-left': navbarWidth }">

    <router-view />
  </div>
</template>


<script lang="ts">
import NavBar from './components/NavBar/NavBar.vue';
import { navbarWidth } from './components/NavBar/state';
export default {
  components: { NavBar },
  setup() {
    return { navbarWidth }
  }

}
</script>