<template>
    <article>
      <h3>{{ product.title }}</h3>
      <p>{{product.body}}</p>
    </article>
  </template>

  <script lang="ts">
  export default {
    props: ["product"]
  };
  </script>