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
    </div>

  <table class="table table-striped mt-4 mb-4">
    <thead class="table-secondary">
      <tr>
        <!-- <th>ID</th> -->
        <th>Product Image</th>
        <th>Product Name</th>
        <th></th>
        <th>Description</th>
        <th>Start Price(£)</th>
        <th>Active?</th>
        <th>Owner</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="product in products">
        <!-- <td>{{ product['id'] }}</td> -->
        <td>{{ product['product_image'] }}</td>
        <td>{{ product['product_name'] }}</td>
        <td><button @click=view_item_details(product)>View Item Details</button></td>
        <td>{{ product['description'] }}</td>
        <td>{{ product['start_price'] }}</td>
        <td>{{ product['is_active'] }}</td>
        <td>{{ product['owner'] }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import router from '../router';

export default {
  mounted() {
    this.fetch_products()
  },
  data() {
    return {
      products: [],
      query: '',
    };
  },
  delimiters: ['[[', ']]'],
  methods: {
    async fetch_products() {
      let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
      let data = await response.json();
      this.products = data.products;
    },
    view_item_details(product: any) {
      // this.$router.push({ path: '/items' });
      try {
        this.$router.push( {name: 'Items', path: '/items/:pid', params: { pid: product.id }})
      } catch (e) {
        console.log(e)
      }
    },
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
  components: {}
}
</script>