<template>
  <div class="card item-page-container row g-0">
   
    <!-- comment -->
    <div class="d-flex">
      <p>{{pid}}</p>
      <p>{{product_name}}</p>
      <p>{{product_description}}</p>
      <p>{{start_price}}</p>
      <p>{{end_of_bid}}</p>
      <p>{{owner}}</p>
    </div>

  </div>
</template>
  
<script lang="ts">

export default {
  props: ['pid'],
  data() {
    return {
      product_name: null,
      product_description: null,
      start_price: null,
      bid: null,
      end_of_bid: null,
      owner: null,
      comments: []
    }
  },
  computed: {
    filteredComments() {
      const filteredComments = JSON.parse(JSON.stringify(this.comments))
      return filteredComments
    }
  },
  methods: {
    // async fetch_products() {
    //   let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
    //   let data = await response.json();
    //   this.products = data.products;
    // },

    async getItemComments() {
      try {
        let response = await fetch("http://localhost:8000/auctionapp/api/comments/" + this.pid);
        let data = await response.json();
        const rawComments = data.comments
        const filteredComments = JSON.parse(JSON.stringify(rawComments))
        this.comments = filteredComments
      } catch (e) {
        alert(e);
      }
    },

    async getProductData(){
      let response = await fetch("http://localhost:8000/auctionapp/api/items/" + this.pid);
      let rawData = await response.json()
      let data = rawData.product
      this.product_name = data.product_name
      this.product_description = data.product_description
      this.start_price = data.start_price
      this.bid = data.bid
      this.end_of_bid = data.end_of_bid
      this.owner = data.owner

    }

    

  },
  async mounted () {
    this.getProductData()
    this.getItemComments()
  }
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