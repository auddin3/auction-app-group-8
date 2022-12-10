<template>
	<div class="card item-page-container row g-0">
    <!-- item section-->
    <div class="d-flex">
      <p>{{product_name}}</p>
      <p>{{start_price}}</p>
      <p>{{description}}</p>
        <img :src="`http://localhost:8000${imgpath}`" alt="item-image">
    </div>
		<!-- comment section-->
		<div class="">
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
											class="w-full rounded"
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
              <small class="text-muted"> Commenting as </small>
              <h4 class="card-title username">&nbsp @{{ loggedUsername }}</h4>
					</div>
			
					<div class="card-text question-reply">
            <textarea v-model="newComment" type="text" placeholder="Add a comment..." class="w-full rounded" rows="5"></textarea>
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
      start_price: "",
      owner: "",
      endOfBid: "",
      imgpath: "/media/product-images/stock-image.png",
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
          this.newComment = ""
				})
				.catch((e) => {
					alert(e);
				});
		},

		async replyComment(comment: { answer: string; question: string; }) {
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
    async getProductData(){
      let response = await fetch("http://localhost:8000/auctionapp/api/items/" + this.pid);
      let data = await response.json()
      let product = data.product
      this.product_name = product.product_name
      this.description = product.description
      this.start_price = product.start_price
      this.owner = product.owner
      this.endOfBid = product.end_of_bid
      this.imgpath = product.product_image
    },
	},
	async mounted() {
		this.getItemComments();
		this.getLoggedInUser();
    this.getProductData();
	},
};
</script>

<style>
body {
	/* background: linear-gradient(90deg, #a4def9, #c1e0f7, #fffffa); */
	background-color: #a4def9;
}

.comment-as {
	font-size: 14px;
}

.comment-btn {
	margin-top: 20px;
	font-weight: 700;
	border-radius: 80px;
	padding: 8px 15px;
	background-color: #c59fc9;
	color: white;
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
