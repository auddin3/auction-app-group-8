<template>
	<div class="card container row g-0 p-0 item-container">
		<div class="col-md-5 header rounded">
			<div class="profile-photo-container">
				<img
					:src="`http://localhost:8000${imgpath}`"
					class="rounded-circle img-thumbnail mx-auto d-block profile-photo"
					alt="User-Profile-Image"
				/>
			</div>
			<h2 class="card-text text-white font-weight-bold m-t-40">{{ name }}</h2>
			<p class="card-text text-muted">@{{ username }}</p>
		</div>
		<div class="col-md-7 bg-light rounded">
			<div class="card-block">
				<div class="bg-white b-b-default item-container rounded">
					<h6 class="f-w-400 text-justify title">Basic info</h6>
					<div class="row b-b-default g-0">
						<div class="col-sm-4">
							<p class="m-b-10 subtitle">Name</p>
						</div>
						<div class="col-sm-8">
							<div v-if="edit" class="row gx-4 gx-lg-5">
								<input
									type="text"
									class="datapoint input-box"
									id="name"
									name="name"
									v-model="name"
								/>
							</div>
							<h6 v-else class="datapoint">{{ name }}</h6>
						</div>
					</div>
					<div class="row b-b-default g-0">
						<div class="col-sm-4">
							<p class="m-b-10 subtitle">Username</p>
						</div>
						<div class="col-sm-8">
							<div v-if="edit" class="row gx-4 gx-lg-5">
								<input
									type="text"
									class="datapoint input-box"
									id="username"
									name="username"
									v-model="username"
								/>
							</div>
							<h6 v-else class="datapoint">{{ username }}</h6>
						</div>
					</div>
					<div class="row g-0">
						<div class="col-sm-4">
							<p class="m-b-10 subtitle">Birthday</p>
						</div>
						<div class="col-sm">
							<div v-if="edit" class="row gx-4 gx-lg-5">
								<input type="text" class="datapoint input-box" id="dob" name="dob" v-model="dob" />
							</div>
							<h6 v-else class="datapoint">{{ dob }}</h6>
						</div>
					</div>
				</div>
				<div class="bg-white b-b-default item-container rounded m-t-40">
					<h6 class="f-w-400 text-justify title">Contact info</h6>
					<div class="row g-0">
						<div class="col-sm-4">
							<p class="m-b-10 subtitle">Email</p>
						</div>
						<div class="col-sm-8">
							<div v-if="edit" class="row gx-4 gx-lg-5">
								<input
									type="text"
									class="datapoint input-box"
									id="email"
									name="email"
									v-model="email"
								/>
							</div>
							<h6 v-else class="datapoint">{{ email }}</h6>
						</div>
					</div>
				</div>
				<div class="row g-0">
					<div class="bg-white b-b-default item-container rounded m-t-40 col-sm-5">
						<h6 class="f-w-400 text-justify title">Your Bids</h6>
						<div class="row g-0">
							<div>
								<p class="m-b-10 info-text">You currently have {{ bids }} bids</p>
							</div>
						</div>
					</div>
					<div class="bg-white b-b-default item-container m-l-auto rounded m-t-40 col-sm-5">
						<h6 class="f-w-400 text-justify title">Your Items</h6>
						<div class="row g-0">
							<div>
								<p class="m-b-10 info-text">You currently own {{ items }} items</p>
							</div>
						</div>
					</div>
				</div>
				<div class="d-grid gap-2 m-t-40">
					<button v-if="edit" type="button" class="btn btn-lg f-w-600" v-on:click="editOff()"
						>Submit profile</button
					>
					<button v-else type="button" v-on:click="editOn()" class="btn btn-lg f-w-600"
						>Change profile</button
					>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
export default {
	data() {
		let date = new Date();
		const TODAY = new Date(date.getFullYear(), date.getMonth(), date.getDate());

		return {
			name: " ",
			username: " ",
			email: " ",
			dob: TODAY.toISOString().slice(0, 10),
			bids: 0,
			items: 0,
			imgpath: "/media/profile-photos/default-dp.png",
			edit: false,
		};
	},
	methods: {
		async editOff() {
			let fullname = this.name.split(" ");
			if (fullname.length == 1) {
				fullname.push("");
			}

			await fetch("http://localhost:8000/auctionapp/api/profile/" + 1 + "/", {
				method: "PUT",
				body: JSON.stringify({
					fname: fullname[0],
					lname: fullname[1],
					username: this.username,
					email: this.email,
					dob: new Date(this.dob).toLocaleDateString("fr-CA"),
				}),
			})
				.then((response) => {
					this.refreshData();
				})
				.catch((e) => {
					alert(e);
				});
			this.edit = false;
		},

		async editOn() {
			this.edit = true;
		},

		async refreshData() {
			try {
				let response = await fetch("http://localhost:8000/auctionapp/api/profile/" + 1);
				let rawData = await response.json();
				let data = rawData.user;
				this.name = data.fname + " " + data.lname;
				this.username = data.username;
				this.email = data.email;
				this.dob = new Date(data.dob).toLocaleDateString("en-GB", {
					day: "numeric",
					year: "numeric",
					month: "long",
				});

				this.imgpath = data.imgpath;

				this.bids = rawData.bids;
				this.items = rawData.items;
			} catch (e) {
				alert(e);
			}
		},
	},

	async mounted() {
		//Fetch user data
		try {
			let response = await fetch("http://localhost:8000/auctionapp/api/profile/" + 1);
			let rawData = await response.json();
			let data = rawData.user;
			this.name = data.fname + " " + data.lname;
			this.username = data.username;
			this.email = data.email;
			this.dob = new Date(data.dob).toLocaleDateString("en-GB", {
				day: "numeric",
				year: "numeric",
				month: "long",
			});

			this.imgpath = data.imgpath;

			this.bids = rawData.bids;
			this.items = rawData.items;
		} catch (e) {
			alert(e);
		}
	},
};
</script>

<style>
body {
	/* background: linear-gradient(90deg, #a4def9, #c1e0f7, #fffffa); */
	background-color: #a4def9;
}

.profile-photo-container {
	height: 40%;
	margin-top: 85px;
}

.profile-photo {
	height: 100%;
	width: 70%;
	margin-left: auto;
	margin-right: auto;
}

.btn {
	background-color: #c59fc9;
	color: white;
}

.btn:hover {
	background-color: #c1e0f7;
}

.title {
	padding-top: 24px;
	padding-bottom: 16px;
	padding-left: 24px;
	font-size: 22px;
	text-align: start;
	color: #c59fc9;
}

.subtitle {
	font-size: 12px;
	color: grey;
	font-weight: 500;
	text-align: start;
	padding-left: 24px;
	max-width: 156px;
	padding-right: 24px;
	margin-top: 10px;
}

.input-box {
	width: 88%;
	border: 1px solid #e0e0e0;
	margin-top: 3.5px !important;
	margin-left: -1px;
}

.input-box:hover {
	background-color: #e8e8e8;
}

.info-text {
	font-size: 14px;
	color: grey;
	font-weight: 500;
	text-align: start;
	padding-left: 24px;
	padding-right: 5px;
	margin-top: 10px;
	padding-bottom: 24px;
}

.datapoint {
	color: black;
	font-weight: 500;
	text-align: start;
	padding-right: 24px;
	margin-top: 8px;
}

.container {
	display: flex;
	flex-direction: row;
	min-height: 93vh;
	min-width: 72vw;
}

.item-container {
	border: 1px solid #e0e0e0;
}

.header {
	background: linear-gradient(180deg, #9795ef, #f9c5d1);
	/* background-color: #A4DEF9; */
	/* background: linear-gradient(to bottom, #A4DEF9, #C1E0F7); */
}

.card-block {
	padding: 1.25rem;
}

.b-b-default {
	border-bottom: 1px solid #e0e0e0;
}

.m-b-20 {
	margin-bottom: 20px;
}

.p-b-5 {
	padding-bottom: 5px !important;
}

.p-x-0 {
	padding-right: 0px;
	padding-left: 0px;
}

.m-t-40 {
	margin-top: 40px;
}

.m-b-10 {
	margin-bottom: 10px;
}

.m-l-auto {
	margin-left: auto;
}

.f-w-600 {
	font-weight: 600;
}

.f-w-400 {
	font-weight: 400;
}
</style>
