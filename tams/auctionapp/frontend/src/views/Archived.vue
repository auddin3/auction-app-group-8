// if want to toggle navbar from inside a page
// not sure if needed, extra feature from tutorial


<template>
    <h1>The navbar is {{ collapsed ? 'closed' : 'open' }}</h1>
    <button @click="toggleNavBar">Toggle navbar</button>
  </template>
  
  <script lang="ts">
  import { collapsed, toggleNavBar } from '../components/navbar/state'
  export default {
    setup() {
      return { collapsed, toggleNavBar }
    }
  }
  </script>