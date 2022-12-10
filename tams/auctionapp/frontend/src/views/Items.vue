<template>
	<div class="card item-page-container row g-0">
		<!-- comment -->
		<div class="">
			<div>
				<h5 class="question-header">Comments</h5>
			</div>

			<div v-if="comments.length > 0">
				<div v-for="comment in filteredComments">
					<div class="card-group">
						<!-- <div class="card mt-4">
              <img class="" src="../assets/vue.svg" alt="profile picture" />
            </div> -->
						<div class="card mt-4 bg-light" style="width: 60rem">
							<div class="card-body">
								<div class="d-flex justify-start">
									<h4 class="card-title username">{{ comment.sender }}</h4>
									<small class="text-muted"> asked about {{ comment.product }} </small>
								</div>
								<div>
									<p class="card-text question-text">{{ comment.question }}</p>
								</div>
								<div v-if="comment.answer.length < 1">
									<div class="card-text question-reply">
										<input type="text" placeholder="Reply" class="w-full" />
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
						<h4 class="card-title comment-as">Commenting as</h4>
					</div>
          <div>
            
          </div>
					<div class="card-text question-reply">
						<input type="text" placeholder="Add a comment..." class="w-full" />
					</div>
					<div class="d-flex flex-row-reverse">
						<button class="btn btn-primary comment-btn">Comment</button>
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
		};
	},
	computed: {
		filteredComments() {
			const filteredComments = JSON.parse(JSON.stringify(this.comments));
			return filteredComments;
		},
	},
	methods: {
		// async fetch_products() {
		//   let response = await fetch("http://127.0.0.1:8000/auctionapp/api/products/");
		//   let data = await response.json();
		//   this.products = data.products;
		// },

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
	},
	async mounted() {
		this.getItemComments();
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
}

.w-full {
	width: 100%;
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
