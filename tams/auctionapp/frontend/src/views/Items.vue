<template>
  <div class="card item-page-container row g-0">
   
    <!-- comment -->
    <div class="d-flex">
      <h5 class="question-header">Questions</h5>
    </div>

  </div>
</template>
  
<script lang="ts">

export default {
  props: ['pid'],
  data() {

  },
  methods: {
    // async fetch_products() {
    //   let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
    //   let data = await response.json();
    //   this.products = data.products;
    // },

  },
  // async mounted () {

  // }
}
</script>

<style>

  body {
    /* background: linear-gradient(90deg, #a4def9, #c1e0f7, #fffffa); */
    background-color: #a4def9;
  }

  .question-header {
    color: #c59fc9;
  }

  .item-btn {
    background-color: #c59fc9;
    color: white;
    display: inline;
    float: left;
  }

  .item-btn:hover {
    background-color: #c1e0f7;
  }

  .item-page-container {
    margin: 0 auto !important;
    display: flex;
    flex-direction: row;
    min-height: 93vh;
    width: 60vw;
    padding: 60px;
  }

</style>