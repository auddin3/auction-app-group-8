<template>
  <div class="auctions"
    style="background-color:#C59FC9; padding: 10px; border-radius: 10px; width: 100%; margin:auto; color:white;">
    <h1 class="">Auctions</h1>
  </div>

  <div id="search" style="">
    <div style="background-color: #CFBAE1; width: 60%; margin: auto; border-radius: 10px;" class="p-4 mt-4">
      <h3 class="" style="color:white">Search</h3>
      <input type="text" v-model="search" class="" style="background-color: white; color: black;" />
    </div>
    <div class="">
      <div v-for="product in filteredProducts" :key="product.id" class="mt-4">
        <Product :product="product"></Product>

      </div>
    </div>
  </div>

  <div v-for="product in products">
    <div class="card-group">
      <div class="card mt-4" style="width: 10rem;">
        <img class="card-img-top" src="../assets/vue.svg" style="height: 200px; width: 200px; margin:auto;"
          alt="Item image" />
      </div>
      <div class="card mt-4" style="width: 60rem;">
        <div class="card-body">
          <h4 class="card-title" style="">{{ product['product_name'] }}</h4>
          <p class="card-text">{{ product['description'] }}</p>
          <p class="card-text" style="color:#7354B5"><strong>Start Price: £{{ product['start_price'] }}</strong></p>
          <p class="card-text">End of Bid: {{ product['end_of_bid'] }}</p>
          <p class="card-text">Owner: {{ product['owner'] }}</p>
          <button @click=view_item_details(product) class="btn btn-secondary">View Item Details</button>
        </div>
      </div>

    </div>
  </div>


</template>

<script lang="ts">
import router from '../router';
import Product from './Product.vue';

export default {
  mounted() {
    this.fetch_products()
  },
  data() {
    return {
      products: [],
      query: '',
      search: "",
      products2: [
        {
          id: 1,
          title: "iphone",
          body: "iphone"
        },
        {
          id: 2,
          title: "laptop",
          body: "hp"
        }
      ]
    };
  },
  computed: {
    filteredProducts() {
      return this.products2.filter(product =>
        product.body.toLowerCase().includes(this.search.toLowerCase())
      );
    }
  },
  methods: {
    async fetch_products() {
      let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
      let data = await response.json();
      this.products = data.products;
    },
    view_item_details(product: any) {
      try {
        this.$router.push({ name: 'Items', path: '/items/:pid', params: { pid: product.id } })
      } catch (e) {
        console.log(e)
      }
    },
  },
  components: {
    Product
  }
}
</script>