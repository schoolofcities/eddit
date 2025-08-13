<script>
	import "../assets/global-styles.css";

	const cards = [
		{
			image: "./landing/card-images/abq-title.jpg",
			title: "From tracks to trail: Planning for equitable (re)development",
			subtitle: "Albuquerque, New Mexico.",
			url: "/eddit/albuquerque-nm" 
		},
		{
			image: "./landing/card-images/bridgeport-title.jpg",
			title: "Increasing tree cover for equity and climate resilience",
			subtitle: "Bridgeport, Connecticut",
			url: "/eddit/bridgeport-ct"
		},
		{
			image: "https://picsum.photos/id/1035/320/270",
			title: "City Lights",
			subtitle: "The beauty of urban nights",
			url: "/eddit/bridgeport-ct"
		},
		{
			image: "https://picsum.photos/id/1045/320/270",
			title: "Forest Path",
			subtitle: "Wander through the woods",
			url: "/eddit/bridgeport-ct"
		},
		{
			image: "https://picsum.photos/id/1055/320/270",
			title: "Desert Dunes",
			subtitle: "Adventure in the sand",
			url: "/eddit/bridgeport-ct"
		},
		{
			image: "https://picsum.photos/id/1065/320/270",
			title: "Snowy Peaks",
			subtitle: "A winter wonderland",
			url: "/eddit/bridgeport-ct"
		},
		{
			image: "https://picsum.photos/id/1075/320/270",
			title: "Golden Sunset",
			subtitle: "End your day with warmth",
			url: "/eddit/bridgeport-ct"
		},
		{
			image: "https://picsum.photos/id/1085/320/270",
			title: "Autumn Leaves",
			subtitle: "A palette of fall colors",
			url: "/eddit/bridgeport-ct"
		},
		{
			image: "https://picsum.photos/id/1095/320/270",
			title: "Lakeside Cabin",
			subtitle: "Tranquility by the water",
			url: "/eddit/bridgeport-ct"
		},
		{
			image: "https://picsum.photos/id/1105/320/270",
			title: "Countryside Road",
			subtitle: "Journey through the fields",
			url: "/eddit/bridgeport-ct"
		}
	];
</script>

<div class="cards-container">
	{#each cards as card}
		<a href={card.url} class="card">
			<img src={card.image} alt={card.title} loading="lazy" />
			<div class="card-text">
				<h2>{card.title}</h2>
				<h3>{card.subtitle}</h3>
			</div>
		</a>
	{/each}
</div>

<style>
	.cards-container {
		display: flex;
		flex-wrap: wrap;
		gap: 20px;
		justify-content: center;
		padding: 20px;
		margin-top: 100px;
		margin-bottom: 100px;
	}

	.card {
		width: 320px;
		height: 480px;
		display: flex;
		flex-direction: column;
		background-color: var(--brandWhite, white);
		box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
		border-radius: 0;
		overflow: hidden;
		text-decoration: none; /* remove underline */
		color: inherit; /* keep text color */
	}

	.card:hover {
		opacity: 0.7;
	}

	.card img {
		width: 100%;
		height: 60%;
		object-fit: cover;
	}

	.card-text {
		height: 40%;
		background-color: var(--brandDarkBlue);
		color: white;
		padding: 15px;
		display: flex;
		flex-direction: column;
	}

	.card-text h2,
	.card-text h3 {
		margin: 0;
	}

	.card-text h2 {
		font-family: TradeGothicBold;
		font-weight: normal;
		font-size: 28px;
		margin-bottom: 5px;
		color: var(--brandWhite);
		padding-bottom: 10px;
		border-bottom: solid 2px var(--brandYellow);
	}

	.card-text h3 {
		font-family: SourceSerifItalic;
		font-weight: normal;
		font-size: 20px;
		opacity: 1;
		color: var(--brandWhite);
	}
</style>
