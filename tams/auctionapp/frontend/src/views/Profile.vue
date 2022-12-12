<template>
	<div class="card container row g-0 p-0 item-container">
		<div class="col-md-5 header rounded">
			<div class="profile-photo-container">
				<img
					:src="`http://localhost:8000${imgpath}`"
					class="rounded-circle img-thumbnail mx-auto d-block profile-photo"
					alt="User-Profile-Image"
				/>
				<div v-if="edit">
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
						<p class="d-inline btn-text">Add profile picture</p>
					</label>
				</div>
			</div>
			<h2 class="card-text text-white font-weight-bold m-t-40 name">{{ fullname }}</h2>
			<p class="card-text text-muted">@{{ username }}</p>
		</div>
		<div class="col-md-7 bg-light rounded">
			<div class="card-block">
				<div class="bg-white b-b-default item-container rounded">
					<h6 class="f-w-400 text-justify title">Basic info</h6>
					<div class="row b-b-default g-0">
						<div class="col-sm-4">
							<p v-if="edit" class="m-b-10 subtitle">First name</p>
							<p v-else class="m-b-10 subtitle">Name</p>
						</div>
						<div class="col-sm-8">
							<div v-if="edit" class="row gx-4 gx-lg-5">
								<input
									type="text"
									class="datapoint input-box"
									id="name"
									name="name"
									v-model="fname"
								/>
							</div>
							<h6 v-else class="datapoint">{{ fullname }}</h6>
						</div>
					</div>
					<div v-if="edit" class="row b-b-default g-0">
						<div class="col-sm-4">
							<p class="m-b-10 subtitle">Last name</p>
						</div>
						<div class="col-sm-8">
							<div v-if="edit" class="row gx-4 gx-lg-5">
								<input
									type="text"
									class="datapoint input-box"
									id="name"
									name="name"
									v-model="lname"
								/>
							</div>
							<h6 v-else class="datapoint">{{ fullname }}</h6>
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
				<div v-if="!edit" class="row g-0">
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
			fullname: " ",
			username: " ",
			email: " ",
			dob: TODAY.toISOString().slice(0, 10),
			bids: 0,
			items: 0,
			imgpath: "/media/profile-photos/default-dp.png",
			edit: false,
			fname: " ",
			lname: " ",
		};
	},
	methods: {
		async editOff() {
			await fetch("http://localhost:8000/auctionapp/api/profile/" + 1 + "/", {
				method: "PUT",
				body: JSON.stringify({
					fname: this.fname,
					lname: this.lname,
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
				this.fullname = data.fname + " " + data.lname;
				this.fname = data.fname;
				this.lname = data.lname;
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

		async onFileSelected(e: any) {
			const selectedFile = e.target.files[0];
			const fd = new FormData();

			fd.append("image", selectedFile)
			fd.append("name", selectedFile.name)

			await fetch("http://localhost:8000/auctionapp/api/picture/" + 1 + "/", {
				method: "POST",
				body: fd,
			})
				.then((response) => {
					this.refreshData();
					(this.$refs['myFileInput'] as any).value = '';
				})
				.catch((e) => {
					alert(e);
				});
		},
	},

	async mounted() {
		//Fetch user data
		try {
			let response = await fetch("http://localhost:8000/auctionapp/api/profile/" + 1);
			let rawData = await response.json();
			let data = rawData.user;
			this.fullname = data.fname + " " + data.lname;
			this.fname = data.fname;
			this.lname = data.lname;
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

.profile-pic-button {
	width: 70%;
	background: transparent !important;
	border: 1px solid #e0e0e0;
	color: white;
	margin-top: 20px;
	padding: 8px 0;
}

.name {
	margin-top: 80px !important;
}

.btn {
	background-color: #c59fc9;
	color: white;
}

.btn-icon {
	margin-right: 5px;
	margin-bottom: 5px;
}

.btn-text {
	margin-left: 5px;
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
