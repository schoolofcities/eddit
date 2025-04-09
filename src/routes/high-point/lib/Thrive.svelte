<script>

	const data = [
		{
			"text": "THRIVE has assisted me with many resources such as leadership HP and also business coaching. I am fairly a new member and look forward to learning and growing with THRIVE.",
			"photo": "location-12-and-i-still-rise.png"
		},
		{
			"text": "(Thrive) has been a source of amazing networking in the area",
			"photo": "location-8-mt-zion.png"
		},
		{
			"text": "I received a Thrive grant which was monumental to supporting my business. I also network frequently within the Thrive family.",
			"photo": "location-10-washington-street-park.png"
		}
	]

	let id = 0;

	$: text = data[id].text;
	$: photo_url = "/eddit/high-point/" + data[id].photo;

	$: console.log(id);

	function getNextImage() {
		if (id === data.length - 1) {
			id = 0
		} else {
			id = id + 1
		}
	}
	function getPreviousImage() {
		if (id === 0) {
			id = data.length - 1
		} else {
			id = id - 1
		}
	}

</script>



<div id="info-wrapper">
	<div id="switch-place">
		<div on:click={getPreviousImage} class="items">
			<svg width="24" height="24">
				<line
					x1="19"
					y1="6"
					x2="5"
					y2="13"
					stroke="#F1F7F7"
					stroke-width="4"
					stroke-linecap="round"
				/>
				<line
					x1="5"
					y1="13"
					x2="19"
					y2="20"
					stroke="#F1F7F7"
					stroke-width="4"
					stroke-linecap="round"
				/>
			</svg>
		</div>
		<div on:click={getNextImage} class="items">
			<svg width="24" height="24">
				<line
					x1="5"
					y1="6"
					x2="19"
					y2="13"
					stroke="#F1F7F7"
					stroke-width="4"
					stroke-linecap="round"
				/>
				<line
					x1="19"
					y1="13"
					x2="5"
					y2="20"
					stroke="#F1F7F7"
					stroke-width="4"
					stroke-linecap="round"
				/>
			</svg>
		</div>
	</div>

	<div id="place-text">
		<p>" {text} "</p>
	</div>

	<div id="place-photo">
		<img src={photo_url} alt="Photo" />
	</div>
</div>



<style>

	#info-wrapper {
		margin: 0 auto;
		min-height: 330px;
		/* height: 330px; */
		/* overflow: hidden; */
	}

	#switch-place {
		width: 100%;
		height: 40px;
		border-bottom: solid 1px var(--e-global-color-green);
		margin: 0 auto;
		margin-bottom: 20px;
		display: flex;
		justify-content: center; /* Center items horizontally */
		align-items: center; /* Center items vertically */
	}

	.items {
		/* display: block; */
		/*position: relative;*/

		padding-bottom: 3px;

		font-size: 23px;
		width: 24px;
		height: 24px;

		overflow: hidden;
		overflow-y: hidden;

		background-color: var(--e-global-color-green);
		color: var(--brandGray80);

		border: solid 1px var(--e-global-color-lightblue);
		/*border-radius: 24px;*/

		/* text-align: center; */

		margin: 0px;
		margin-left: 10px;

		/* margin-top: 5px;
		margin-bottom: 0px;
		margin-left: 10px; */
		/* margin: 0 auto; */
		/* float: left; */
		z-index: 2;
	}
	.items:hover {
		cursor: pointer;
		background-color: var(--brandYellow);
	}


	#place-text {
		float: left;
		padding-top: 0px;
		margin-top: 5px;
		width: 100%;
		max-width: 480px;
	}

	#place-text p {
		margin-top: -20px;
		padding: 10px;
		font-size: 26px;
		line-height: 38px;
		font-style: italic;
		color: var(--e-global-color-darkblue);
	}

	#place-photo {
		overflow: hidden;
		max-width: 480px;
		max-height: 270px;
		border: solid 1px var(--e-global-color-green);
		margin: 0px;
		margin-bottom: 10px;
		opacity: 0.8;
	}

	#place-photo img {
		max-width: 480px;
		width: 500px;
		height: 333px;
	}

	@media screen and (max-width: 960px) {
		#place-text {
			margin: 0 auto;
			max-width: 520px;
		}
		#info-wrapper {
			display: flex;
			flex-wrap: wrap;
		}
		#place-photo {
			overflow: hidden;
			max-width: 600px;
			border: solid 2px "red";
			margin: 0 auto;
			opacity: 0.8;
			padding-bottom: 60px;
			margin-bottom: 10px;
		}
		#place-photo img {
			max-width: 600px;
			padding-bottom: 10px;
		}
	}

</style>