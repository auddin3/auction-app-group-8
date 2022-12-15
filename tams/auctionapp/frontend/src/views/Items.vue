<template>
	<div class="card item-page-container row g-0">
    <!-- item section-->
    <div class="d-flex">
		<div class="card mt-4 border: 1px solid #e0e0e0" style="width: 40rem; ">
        	<img class="card-img-top product-image" :src="`http://localhost:8000${imgpath}`" alt="Item image" />
      	</div>
		<div class="card mt-4 border: 1px solid #e0e0e0" style="width: 60rem;">
			<div class="card-body">
			<h4 class="card-title">{{ product_name}}</h4>
			<p class="card-text">{{description}}</p>
			<p class="card-text price-colour"><strong>Start Price: £{{start_price }}</strong></p>
			<p class="card-text">End of Bid: {{endOfBidFormatted}}</p>
			<p class="card-text">Owner: {{owner}}</p>
			</div>
      	</div>
    </div>
		
		<!-- bid section (copy into item) -->
		<div class="row g-0 bid-container p-4">
			<div class="col-sm-6">
				<div class="row g-1">
					<h5 class="col-sm-5">Best offer: </h5>
					<div class="col-sm-1"></div>
					<div class="col-sm-6 d-flex flex-column align-items-start">
						<h3>£{{ win_price }}</h3>
						<input
							type="number"
							placeholder="Bid amount"
							class="bid-input p-2"
							v-model="bid_entry"
							step="0.01"
						/>
						<small class="text-muted">Enter £{{ start_price }} or more</small>
					</div>
				</div>
			</div>
			<div class="col-sm-6 d-flex flex-column align-items-end">
				<small class="text-muted">[{{ bid_total }} bids]</small>
				<button class="btn btn-primary bid-btn" v-on:click="addBid" min="{{ start_price }}">Submit Bid</button>
			</div>
		</div>
		<!-- comment section-->
		<div class="m-t-40">
			<div>
				<h5 class="question-header">Comments</h5>
			</div>
			<div v-if="comments.length > 0">
				<div v-for="comment in filteredComments">
					<div class="card-group">
						<div class="card mt-4 rounded" style="width: 60rem">
							<div class="card-body">
								<div class="d-flex justify-start">
									<h4 class="card-title username">{{ comment.sender }}</h4>
									<small class="text-muted"> asked about {{ comment.product.slice(0, 55) }} </small>
								</div>
								<div>
									<p class="card-text question-text">{{ comment.question }}</p>
								</div>
								<div v-if="comment.answer.length < 1">
									<div class="card-text question-reply">
										<input
											type="text"
											v-model="comment.answer"
											placeholder="Reply"
											class="w-full rounded p-2"
										/>
									</div>
									<div class="d-flex flex-row-reverse">
										<button class="btn btn-primary comment-btn" v-on:click="replyComment(comment)"
											>Reply</button
										>
									</div>
								</div>
								<div v-else class="p-r-4">
									<div class="d-flex justify-start question-reply">
										<h4 class="card-title username">{{ comment.recipient }}</h4>
										<small class="text-muted"> replied to {{ comment.sender }} </small>
									</div>
									<div class="d-flex justify start">
										<p class="card-text question-text">{{ comment.answer }}</p>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="card-group">
				<div class="card mt-4 bg-light" style="width: 60rem">
					<div class="d-flex justify-start">
						<small class="text-muted"> Comment as </small>
						<h4 class="card-title username">&nbsp {{ loggedUsername }}</h4>
					</div>

					<div class="card-text question-reply">
						<textarea
							v-model="newComment"
							type="text"
							placeholder="Add a comment..."
							class="w-full rounded p-3"
							rows="5"
						></textarea>
					</div>
					<div class="d-flex flex-row-reverse">
						<button class="btn btn-primary comment-btn" v-on:click="addComment()">Comment</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
export default {
	props: ["pid"],
	data() {
		return {
			comments: [],
			loggedUsername: "",
			loggedUserFullName: "",
			loggedUserId: 0,
			newComment: "",

			product_name: "",
			description: "",
			start_price: 0,
			owner: "",
			endOfBid: "",
			noOfSecsLeft: 5,
			endOfBidFormatted: "",
			period: 0,
			imgpath: "/media/product-images/stock-image.png",

			bid_entry: 0,
			bid_total: 0,
			win_price: 0,
			user_id: 0,
			user_email: "",
		};
	},
	computed: {
		filteredComments() {
			const filteredComments = JSON.parse(JSON.stringify(this.comments));
			return filteredComments;
		},
	},
	methods: {
		async getLoggedInUser() {
			let response = await fetch("http://localhost:8000/auctionapp/user", {
				credentials: "include",
				mode: "cors",
				referrerPolicy: "no-referrer",
				method: "GET",
			});
			let data = await response.json();
			const userId = data.user_id;
			this.loggedUserId = userId;

			response = await fetch("http://localhost:8000/auctionapp/api/profile/" + userId);
			let rawData = await response.json();
			let userData = rawData.user;
			this.loggedUsername = userData.username;
			this.loggedUserFullName = userData.fname + " " + userData.lname;
		},

		async getItemComments() {
			try {
				let response = await fetch("http://localhost:8000/auctionapp/api/comments/" + this.pid);
				let data = await response.json();
				const rawComments = data.comments;
				const filteredComments = JSON.parse(JSON.stringify(rawComments));
				this.comments = filteredComments;
			} catch (e) {
				alert(e);
			}
		},

		async addComment() {
			await fetch("http://localhost:8000/auctionapp/api/comments/" + this.pid, {
				method: "POST",
				body: JSON.stringify({
					question: this.newComment,
					sender: this.loggedUserId,
					answer: "",
				}),
			})
				.then((response) => {
					this.getItemComments();
					this.newComment = "";
				})
				.catch((e) => {
					alert(e);
				});
		},

		async replyComment(comment: { answer: string; question: string }) {
			await fetch("http://localhost:8000/auctionapp/api/comments/" + this.pid, {
				method: "PUT",
				body: JSON.stringify({
					answer: comment.answer,
					recipient: this.loggedUserId,
					question: comment.question,
				}),
			})
				.then((response) => {
					this.getItemComments();
				})
				.catch((e) => {
					alert(e);
				});
		},

		async getProductData() {
			let response = await fetch("http://localhost:8000/auctionapp/api/items/" + this.pid);
			let data = await response.json();
			let product = data.product;
			this.product_name = product.product_name;
			this.description = product.description;
			this.start_price = product.start_price;
			this.owner = product.owner;
			this.endOfBid = product.end_of_bid;
			this.imgpath = product.product_image;

			var date = new Date();
			var endDateTime = new Date(this.endOfBid)
			this.noOfSecsLeft = (endDateTime.valueOf()-date.valueOf())/1000; //should return milliseconds left
			console.log("no of secs left ",this.noOfSecsLeft,"s")

		},

		async getBidCount() {
			let response = await fetch("http://localhost:8000/auctionapp/api/bidCount/" + this.pid);
			let data = await response.json();
			this.bid_total = data.total
			this.win_price = data.win
			if (data.win == 0){
				this.bid_entry = this.start_price
			}
			else {
				this.bid_entry = data.win
			}
		},

		async addBid() {
			let response = await fetch("http://localhost:8000/auctionapp/api/bids/" + this.pid, {
				method: "POST",
				body: JSON.stringify({
					bidder: this.loggedUserId,
					bid_price: this.bid_entry,
				}),
			})
				.then((response) => {
					this.bid_entry = this.start_price;
					this.getBidCount();
				})
				.catch((e) => {
					alert(e);
				});
		},

		async formatTime(){
			let res = await this.getProductData()

			console.log("secondss",this.noOfSecsLeft)
			if (this.noOfSecsLeft > 0){
				let seconds = this.noOfSecsLeft
				let days = Math.floor(seconds/(24*3600))
				seconds = seconds % (24*3600)
				let hours = Math.floor(seconds/3600)
				seconds = seconds % 3600
				let minutes = Math.floor(seconds/60)
				this.endOfBidFormatted = (days+' Days '+hours+' Hours '+minutes+' Minutes ')
				return
			}
			else{
				this.endOfBidFormatted = ("0 Days 0 Hours 0 Minutes")
				//this.getWinner()
				//this.emailWinner()
				this.deleteProduct()
				return
			}



		},

		async getWinner(){
			let response = await fetch("http://localhost:8000/auctionapp/api/getWinner/"+this.pid)
			let data = await response.json()
			this.user_id = data.user_id
			this.user_email = data.user_email
			console.log("email",this.user_email,this.user_id)
		},

		async emailWinner(){
			await this.getWinner()
			let response = await fetch("http://localhost:8000/auctionapp/api/emailWinner/"+this.user_id+"/"+this.pid)
			let data = await response.json()
			console.log("email sent to",data.useremail)
		},

		async deleteProduct(){
			await this.getWinner()
			await this.emailWinner()
			let response = await fetch("http://localhost:8000/auctionapp/api/deleteProduct/"+this.pid, {
				method:'DELETE'
			})
			await this.viewSearch()
		},

		async viewSearch() {
		try {
			this.$router.push({ name: 'Auctions', path: '', params: {} })
		} catch (e) {
			console.log(e)
		}
		},



	},
	async mounted() {
		this.getItemComments();
		this.getLoggedInUser();
		this.getProductData();
		this.getBidCount();
		this.formatTime();
		//this.getWinner();
		//this.emailWinner();
	},

};
</script>

<style>
body {
	/* background: linear-gradient(90deg, #a4def9, #c1e0f7, #fffffa); */
	background-color: #a4def9;
}

.card-title{
	color: #c59fc9;
}

.bid-container {
	border-bottom: 1px solid #e0e0e0;
	border-top: 1px solid #e0e0e0;
}

.bid-input {
	width: 150px;
	margin-bottom: 5px;
}

.comment-as {
	font-size: 14px;
}

.m-t-40 {
	margin-top: 50px;
}

.comment-btn {
	margin-top: 20px;
	font-weight: 700;
	border-radius: 80px;
	padding: 8px 15px;
	background-color: #c59fc9;
	color: white;
}

.bid-btn {
	margin-top: 15px;
	font-weight: 700;
	border-radius: 80px;
	padding: 8px 15px;
	background-color: #c59fc9;
	color: white;
	width: 70%;
}

.w-full {
	width: 100%;
}

.p-l-1 {
	padding-left: 10px;
}

.p-r-4 {
	padding-left: 32px;
}

.question-text {
	margin: 10px 0;
	display: flex;
	justify-content: start;
	font-size: 14px;
}

.question-reply {
	padding-top: 20px;
	display: flex;
	justify-content: start;
	font-size: 16px;
}

.username {
	font-size: 16px;
	padding-right: 5px;
}

.question-header {
	color: #c59fc9;
	display: flex;
	justify-content: start;
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
