<template>
	<div class="card-group">
		<div v-if="filteredItems.length > 0">
			<div v-for="item in filteredItems">
				<div class="card mt-4" style="width: 50rem">
					<div v-if="edit" class="product_name">
						<input type="text" id="product_name" v-model="product_name" />
					</div>
					<div v-else class="card-title">
						{{ item.product_name }}
					</div>
					<div class="card mt-4" style="width: 12rem">
						<div v-if="item.product_image.length < 0">
							<img
								class="card-img-top product-image"
								:src="`http://localhost:8000${product_image}`"
								alt="MyItems"
							/>
						</div>
						<div v-else>
							<img
								class="card-img-top product-image"
								:src="`http://localhost:8000${item.product_image}`"
								alt="MyItems"
							/>
						</div>
					</div>
				</div>
			</div>

			<!-- <div class="card mt-4" style="width: 50rem">
			<div v-if="edit" class="product_name">
				<input type="text" id="product_name" v-model="product_name" />
			</div>
			<div v-else class="card-title">
				{{ item.product_name }}
			</div> -->

			<!-- <div v-if="edit" class="description">
          <input type = "text" id="description" v-model="description"/>
        </div>
        <div v-else class="card-title">
          {{description}}
        </div>

        <div v-if="edit" class="description">
          <input type = "text" id="description" v-model="description"/>
        </div>
        <div v-else class="card-text price-colour">
          <b>Start Price: £{{ start_price }}</b>
        </div>

        <div v-if="edit" class="start_price">
          <input type = "number" id="start_price" v-model="start_price"/>
        </div>
        <div v-else class="card-text price-colour">
          <b>Start Price: £{{ start_price }}</b>
        </div>

        <div v-if="edit" class="end_of_bid">
          <input type = "date" id="end_of_bid" v-model="end_of_bid"/>
        </div>
        <div v-else class="card-text">
          <b>End of Bid: {{ end_of_bid }}</b>
        </div>

        <div v-if="edit" class="end_of_bid">
          <input type = "date" id="end_of_bid" v-model="end_of_bid"/>
        </div>
        <div v-else class="card-text">
          <b>End of Bid: {{ end_of_bid }}</b>
        </div>

        <div v-if="edit" class="owner">
          <input type = "text" id="owner" v-model="owner"/>
        </div>
        <div v-else class="card-text">
          <b>Owner:{{ owner }}</b>
        </div>

        <button v-if="edit" type="button" @click=editItemOff() class="btn btn-secondary">View My Items</button>

        <button v-else type="button" v-on:click=editItemOn() class="btn btn-secondary">Change My Items</button>

        <button @click="deleteItem()" type="button" class="btn btn-outline-danger"><b>Delete Item</b></button> -->
		</div>
	</div>

	<h2>Add your item!</h2>
	<div>
		<form @submit.prevent="saveNewItem">
			<fieldset>
				<div>
					<label for="product_name"><b>Item Name</b></label>
					<input type="text" id="product_name" class="form-control" v-model="product_name" />
				</div>

				<div class="item-photo-container">
					<div>
						<input
							v-on:change="onFileSelected"
							type="file"
							id="upload-file"
							name="upload-file"
							ref="myFileInput"
							accept="image/gif, image/jpeg, image/png"
							hidden
						/>
						<label
							type="button"
							for="upload-file"
							refs="upload-file"
							class="profile-pic-button btn-lg"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								xmlns:xlink="http://www.w3.org/1999/xlink"
								enable-background="new 0 0 32 32"
								height="20px"
								id="Layer_1"
								version="1.1"
								viewBox="0 0 32 32"
								width="20px"
								xml:space="preserve"
								class="btn-icon"
							>
								<g id="camera">
									<path
										clip-rule="evenodd"
										d="M16,10.001c-4.419,0-8,3.581-8,8c0,4.418,3.581,8,8,8   c4.418,0,8-3.582,8-8C24,13.583,20.418,10.001,16,10.001z M20.555,21.906c-2.156,2.516-5.943,2.807-8.459,0.65   c-2.517-2.156-2.807-5.944-0.65-8.459c2.155-2.517,5.943-2.807,8.459-0.65C22.42,15.602,22.711,19.391,20.555,21.906z"
										fill="#ffffff"
										fill-rule="evenodd"
									/>
									<path
										clip-rule="evenodd"
										d="M16,14.001c-2.209,0-3.999,1.791-4,3.999v0.002   c0,0.275,0.224,0.5,0.5,0.5s0.5-0.225,0.5-0.5V18c0.001-1.656,1.343-2.999,3-2.999c0.276,0,0.5-0.224,0.5-0.5   S16.276,14.001,16,14.001z"
										fill="#ffffff"
										fill-rule="evenodd"
									/>
									<path
										clip-rule="evenodd"
										d="M29.492,9.042l-4.334-0.723l-1.373-3.434   C23.326,3.74,22.232,3,21,3H11C9.768,3,8.674,3.74,8.214,4.886L6.842,8.319L2.509,9.042C1.055,9.283,0,10.527,0,12v15   c0,1.654,1.346,3,3,3h26c1.654,0,3-1.346,3-3V12C32,10.527,30.945,9.283,29.492,9.042z M30,27c0,0.553-0.447,1-1,1H3   c-0.553,0-1-0.447-1-1V12c0-0.489,0.354-0.906,0.836-0.986l5.444-0.907l1.791-4.478C10.224,5.25,10.591,5,11,5h10   c0.408,0,0.775,0.249,0.928,0.629l1.791,4.478l5.445,0.907C29.646,11.094,30,11.511,30,12V27z"
										fill="#ffffff"
										fill-rule="evenodd"
									/>
								</g>
							</svg>
							<p class="d-inline btn-text">Add item's picture</p>
						</label>
					</div>
				</div>

				<div>
					<label for="description"><b>Item Description</b></label>
					<input type="text" id="description" class="form-control" v-model="description" />
				</div>

				<div>
					<label for="start_price"><b>Starting Price</b></label>
					<input
						type="number"
						step="0.01"
						id="start_price"
						class="form-control"
						v-model="start_price"
					/>
				</div>

				<div>
					<label for="end_of_bid"><b>End of Bid</b></label>
					<input type="date" id="end_of_bid" class="form-control" v-model="end_of_bid" />
				</div>

				<br />
				<div>
					<button type="submit"><b>Submit</b></button>
				</div>
			</fieldset>
		</form>
	</div>

	<!-- <SavedBids/> -->
	<!-- <SavedItems/> -->
</template>

<script lang="ts">
// import SavedBids from './SavedBids.vue'
// import SavedItems from './SavedItems.vue'
export default {
	// components:{
	//   SavedBids,
	//   SavedItems,
	// },
	data() {
		let date = new Date();
		const TODAY = new Date(date.getFullYear(), date.getMonth(), date.getDate());
		return {
			items: [],
			user_id: 0,
			product_name: "",
			product_image: "/media/product-images/stock-image.png",
			description: "",
			start_price: 0,
			end_of_bid: TODAY.toISOString().slice(0, 10),
			owner: "",
			edit: false,
      new_product_image: "/media/product-images/stock-image.png"
		};
	},
	computed: {
		filteredItems() {
			const filteredItems = JSON.parse(JSON.stringify(this.items));
			return filteredItems;
		},
	},
	methods: {
		async fetchItems() {
			let response = await fetch("http://localhost:8000/auctionapp/api/items/" + this.user_id, {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			this.items = data.items;
		},

		async saveNewItem() {
			let response = await fetch("http://localhost:8000/auctionapp/api/items/" + +this.user_id, {
				headers: {
					"Content-Type": "application/json",
				},
				method: "POST",
				body: JSON.stringify({
					product_name: this.product_name,
					product_image: this.new_product_image,
					description: this.description,
					start_price: this.start_price,
					end_of_bid: this.end_of_bid,
				}),
			});

			let data = await response.json();
      
			this.fetchItems()
		},

		async onFileSelected(e: any,) {
			const selectedFile = e.target.files[0];
			const fd = new FormData();

			fd.append("image", selectedFile);
			fd.append("name", selectedFile.name);

			let response = await fetch("http://localhost:8000/auctionapp/api/productPic/", {
				method: "POST",
				body: fd,
			})
			let data = await response.json()
      this.new_product_image = data.path
		},
	},
	async mounted() {
		//Fetch user data
		let response = await fetch("http://localhost:8000/auctionapp/user", {
			credentials: "include",
			mode: "cors",
			referrerPolicy: "no-referrer",
			method: "GET",
		});
		let data = await response.json();
		this.user_id = data.user_id;
		this.fetchItems();
	},
};
</script>

<style>
body {
	background-color: #a4def9;
}

h2 {
	font-size: 2em;
	line-height: 1;
}

button {
	border-radius: 6px;
	font-size: 1em;
	font-weight: 500;
	font-family: inherit;
	background-color: #c59fc9;
	border: #c59fc9;
	cursor: pointer;
	transition: background-color 0.25s;
}
button:hover {
	background-color: #c1e0f7;
	border: #c1e0f7;
}
</style>
