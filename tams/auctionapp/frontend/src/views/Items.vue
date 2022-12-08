<template>
</template>
  
<script lang="ts">

export default {
  data() {
    return {
      products: [],
    };
  },
  methods: {
    async fetch_products() {
      let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
      let data = await response.json();
      this.products = data.products;
    },
  },
}
</script>