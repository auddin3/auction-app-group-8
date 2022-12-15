<template>
  <div class="auctions">
    <h1 class="">Auctions</h1>
  </div>

  <div id="search">
    <div class="search-box p-3 mt-4">
      <!-- <h3 class="search-heading">Search</h3> -->
      <input type="text" v-model="search" class="input-box p-2" placeholder=" Search Upcoming Bids"/>
    </div>
  </div>

  <div v-for="product in filteredProducts">
    <div class="card-group">
      <div class="card mt-4">
        <div v-if="product.product_image.length > 0" class="img-div">
           <img class="card-img-top product-image" :src="`http://localhost:8000${product.product_image}`" alt="Item image" />
        </div>
        <div v-else class="img-div">
            <img class="card-img-top product-image" :src="`http://localhost:8000${imgpath}`" alt="Item image" />
        </div>
      </div>
      <div class="card mt-4" style="width: 60rem;">
        <div class="card-body">
          <h4 class="card-title">{{ product['product_name'] }}</h4>
          <p class="card-text">{{ product['description'] }}</p>
          <p class="card-text price-colour"><strong>Start Price: £{{ product['start_price'] }}</strong></p>
          <!-- <p class="card-text">End of Bid: {{ product['end_of_bid'] }}</p> -->
          <button @click=formatTime(product.end_of_bid) class="btn"><strong>Click to view End of Bid deadline</strong></button>
          <p v-if='endOfBidFormatted != ""'><strong>{{ endOfBidFormatted }} Left</strong></p>
          <p class="card-text mt-4"><strong>Owner:</strong> {{ product['owner'] }}</p>
          <button @click=view_item_details(product) class="btn btn-secondary"><strong>View Item Details</strong></button>
        </div>
      </div>

    </div>
  </div>


</template>

<script lang="ts">
import router from '../router';
import Product from './Product.vue';

export default {
  data() {
    return {
      products: [],
      query: '',
      search: "",
      imgpath: "/media/product-images/stock-image.png",
      endOfBidFormatted: "",
      noOfSecsLeft: 0,
    };
  },
  computed: {
    filteredProducts() {
      const filteredProducts = JSON.parse(JSON.stringify(this.products))
      return filteredProducts.filter((obj: { product_name: string, description: string }) =>
        obj.product_name.toLowerCase().includes(this.search.toLowerCase()) 
        || obj.description.toLowerCase().includes(this.search.toLowerCase()) 
      );
    }
  },
  methods: {
    // async fetch_products() {
    //   let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
    //   let data = await response.json();
    //   this.products = data.products;
    // },
    view_item_details(product: any) {
      try {
        this.$router.push({ name: 'Items', path: '/items/:pid', params: { pid: product.id } })
      } catch (e) {
        console.log(e)
      }
    },
    async formatTime(end_of_bid: any){
      let date = new Date();
			let endDateTime = new Date(end_of_bid)
			let noOfSecsLeft = (endDateTime.valueOf()-date.valueOf())/1000; //should return milliseconds left
			// console.log("no of secs left ",noOfSecsLeft,"s")

      let seconds = noOfSecsLeft
			let days = Math.floor(seconds/(24*3600))
			seconds = seconds % (24*3600)
			let hours = Math.floor(seconds/3600)
			seconds = seconds % 3600
			let minutes = Math.floor(seconds/60)
			this.endOfBidFormatted = (days+' Days '+hours+' Hours '+minutes+' Minutes ')
		}
  },

  async mounted() {
    let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
    let data = await response.json();
    this.products = data.products;
  },
  components: {
    Product
  }
}
</script>

<style>
body {
	background-color: #a4def9;
}

.btn {
	background-color: #c59fc9;
	color: white;
}

.btn:hover {
	background-color: #c1e0f7;
}

.input-box:hover {
	background-color: #e8e8e8;
}

.input-box {
  background-color: white;
  color: black;
  border-radius: 10px;
  width: 90%;
  border: none;
}

.auctions {
  background-color:#C59FC9;
  padding: 10px;
  border-radius: 10px;
  width: 100%;
  margin:auto;
  color:white;
}

.search-box {
  background-color: #c1e0f7;
  width: 60%;
  margin: auto;
  border-radius: 10px;
}

.search-heading {
  color:white;
}

.product-image {
  margin: auto 0;
}

.price-colour {
  color:#7354B5
}

</style>