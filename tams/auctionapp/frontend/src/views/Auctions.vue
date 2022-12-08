<template>
  <div class="auctions">
    <h1>Products</h1>
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
    };
  },
  methods: {
    async fetch_products() {
      let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
      let data = await response.json();
      this.products = data.products;
    },
    view_item_details(product) {
      // this.$router.push({ path: '/items' });
      this.$router.push( {name: 'items', params: { product }})
    },
  },
  components: {}
}
</script>