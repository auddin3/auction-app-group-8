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
          <th>Description</th>
          <th>Start Price(£)</th>
          <th>Active?</th>
          <th>Owner</th>
          <th>Bid</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products">
          <!-- <td>{{ product['id'] }}</td> -->
          <td>{{ product['product_image'] }}</td>
          <td>{{ product['product_name'] }}</td>
          <td>{{ product['description'] }}</td>
          <td>{{ product['start_price'] }}</td>
          <td>{{ product['is_active'] }}</td>
          <td>{{ product['owner'] }}</td>
          <td><a href="#">bid</a></td>
        </tr>
      </tbody>
    </table>
  </template>

<script lang="ts">
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
  },
  components: { }
}
</script>