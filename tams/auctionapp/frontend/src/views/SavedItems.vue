<template>

<div>
    <h2>Your Items</h2>
    <div class="p-3 mb-2 bg-light text-dark">
    <br>
    <button @click="fetchItems">Your Items</button>
    <br>
    <div>


    <!-- <div v-for="item in items" v-bind:key="item.id">

    </div> -->










      <!-- <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Item's name</th>
            <th scope="col">Item's description</th>
            <th scope="col">Starting Price</th>
            <th scope="col">End of Bid</th>
            <th scope="col">Owner</th>

        </tr>
        </thead> -->
        

        
        <!-- <tbody>
        <tr v-for="item in items" v-bind:key="item.id">
          
          <td>{{item.product_name}}</td>

          <td>
            <span v-if="song.top_hit">
              Top Hit
            </span>
            <span v-else="!song.top_hit">
              Old Hit
            </span>
          </td>

          <td>{{song.song_length}} minutes</td>

          <td>{{song.release_date}}</td>

          <td>
            <div cclass="btn-group" role="group" aria-label="Third group">
              <button type="button" @click="changeForm(song.id)" class="btn btn-outline-primary"><b>Update</b></button>
            </div>
          </td>

          <td>
            <div cclass="btn-group" role="group" aria-label="Third group">
              <button @click="deleteSong(song.id)" type="button" class="btn btn-outline-danger"><b>Delete</b></button>
            </div>
          </td>
        </tr>

        </tbody> -->


    <!-- </table>  -->


    </div>
  </div>


</div>





</template>

<script lang="ts" >
export default{

    data() {
    let date = new Date();
    const TODAY = new Date(date.getFullYear(), date.getMonth(), date.getDate());
    return {
      items:[],
      id: 0,
      product_name: "",
      product_image: "/media/product-images",
      description: "",
      start_price: 0,
      end_of_bid: TODAY.toISOString().slice(0, 10),
      owner: "",
    };
  },
    methods:{

     async fetchItems(){
      console.log('hello')
      let response = await fetch("http://localhost:8000/auctionapp/api/products/",
      {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET"
			});
      let data = await response.json()
      console.log(data.items)
      this.items = data.items
    },

    }
}


</script>

