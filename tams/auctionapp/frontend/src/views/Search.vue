<template>
    <div class="auctions">
      <h1>My Inventory</h1>
    </div>

  </template>

<script lang="ts">
export default {
  data() {
    return {
      query: '',
      products: [],
    };
  },
  delimiters: ['[[', ']]'],
  methods: {
    // async fetch_products() {
    //   let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
    //   let data = await response.json();
    //   this.products = data.products;
    // },
    performSearch() {
      var data = {
        'query': this.query,
      }
      fetch('/auctionapp/api/search/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          //  no csrf token line
          // 'X-CSRFToken': {{ csrf_token }}
        },
        body: JSON.stringify(data)
      })
      .then((response) => {
        console.log(data)
        return response.json()
      })
      .then((result) => {
        console.log(result.products)
        this.products = result.products
      })
      .catch((error) => {
        console.log('Error', error)
      })
    },
  },
  components: { }
}
</script>