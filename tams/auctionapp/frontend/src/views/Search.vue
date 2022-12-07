<template>
    <div class="auctions">
      <h1>Products</h1>
    </div>
    <div id="search-products">
      <h3 style="text-align:left;">Search Products</h3>

      <form @submit.prevent="performSearch()" style="text-align:left;">
        <div class="columns">
          <div class="column is-4">
            <div class="field">
              <label>Query</label>
              <div class="control">
                <input type="text" name="query" class="input" v-model="query">
              </div>
            </div>

            <div class="field">
              <div class="control">
                <button class="button is-secondary">Search</button>
              </div>
            </div>

          </div>
        </div>
      </form>

      <div v-if="products.length">
        <hr/>

        <div
          v-for="product in products"
          :key="product.id"
          class="notification mt-2"
        >
          <h4 class="is-size-4">{{ product.product_name }}</h4>
          <p>{{ product.description }}</p>

          <!-- <a :href="product.url">View Product</a> -->

          
        </div>
      </div>
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