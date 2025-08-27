<script>
	import "../assets/global-styles.css";

	const cards = [
    {
        image: "./landing/card-images/abq-title.jpg",
        title: "From tracks to trail: Planning for equitable (re)development",
        subtitle: "Albuquerque, New Mexico",
        url: "/eddit/albuquerque-nm"
    },
    {
        image: "./landing/card-images/bridgeport-title.jpg",
        title: "Increasing tree cover for equity and climate resilience",
        subtitle: "Bridgeport, Connecticut",
        url: "/eddit/bridgeport-ct"
    },
    {
        image: "./landing/card-images/champaign-title.jpg",
        title: "Building safe communities: Infrastructure investments for gun violence prevention",
        subtitle: "Champaign, Illinois",
        url: "/eddit/champaign-il"
    },
    {
        image: "./landing/card-images/cook-county-title.jpg",
        title: "Cross-community Approaches to Climate Action: Transitioning to sustainable landscape practices",
        subtitle: "Cook County, Illinois",
        url: "/eddit/cook-county-il"
    },
    {
        image: "./landing/card-images/eau-claire-title.jpg",
        title: "Connecting the Dots: Showcasing the Benefits of Public Transportation",
        subtitle: "Eau Claire, Wisconsin",
        url: "/eddit/eau-claire-wi"
    },
    {
        image: "./landing/card-images/greensboro-title.jpg",
        title: "Increasing the availability of healthy food",
        subtitle: "Greensboro, North Carolina",
        url: "/eddit/greensboro-nc"
    },
    {
        image: "./landing/card-images/halifax-title.jpg",
        title: "Becoming “Canada’s Favourite Downtown”: Encouraging investments in the core",
        subtitle: "Halifax, Nova Scotia",
        url: "/eddit/halifax-ns"
    },
    {
        image: "./landing/card-images/high-point-title.jpg",
        title: "Revitalizing historic main streets through entrepreneurship",
        subtitle: "High Point, North Carolina",
        url: "/eddit/high-point-nc"
    },
    {
        image: "./landing/card-images/wood-buffalo-title.jpg",
        title: "Seeking a new definition of affordability in a resource economy",
        subtitle: "Wood Buffalo, Alberta",
        url: "/eddit/wood-buffalo-ab"
    },
    {
        image: "./landing/card-images/worcester-title.jpg",
        title: "Investing in affordable housing to support inclusive downtowns",
        subtitle: "Worcester, Massachusetts",
        url: "/eddit/worcester-ma"
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
		height: 65%;
		object-fit: cover;
	}

	.card-text {
		height: 35%;
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
		font-size: 23px;
		margin-bottom: 5px;
		color: var(--brandWhite);
		padding-bottom: 10px;
		border-bottom: solid 2px var(--brandYellow);
	}

	.card-text h3 {
		font-family: SourceSerifItalic;
		font-weight: normal;
		font-size: 18px;
		opacity: 1;
		color: var(--brandWhite);
	}
</style>
