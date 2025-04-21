<script>
	import "../assets/global-styles.css"
	import uniLogos from "../assets/university-logos.svg"
	import edditLogo from "../assets/eddit-logo.svg"

	export let title = '';
	export let subtitle = '';
	export let image = '';
</script>

<div class="container">
	<div class="left">
		<img src={uniLogos} alt="UofT and UCB Logos" class="logo-top"  />
		<div>
			<h1>{title}</h1>
			<h2>{subtitle}</h2>
		</div>
		<img src={edditLogo} alt="EDDIT Logo" class="logo-bottom" />
	</div>
	<div class="right">
		<img src={image} alt="Image" />
	</div>
</div>

<style>
	.container {
		display: flex;
		height: 100vh;
		width: 100%;
		border-bottom: solid 1px var(--brandLightBlue);
	}

	.left {
		flex: 1;
		background-color: var(--brandDarkBlue);
		border-right: solid 1px var(--brandLightBlue);
		display: flex;
		justify-content: center;
		align-items: center;
		text-align: center;
		position: relative;
	}

	.logo-top {
		width: 275px;
		height: auto;
		position: absolute;
		top: 8px;
	}

	.logo-bottom {
		width: 200px;
		height: auto;
		position: absolute;
		bottom: 12px;
	}

	.right {
		flex: 1;
		display: flex;
		justify-content: center;
		align-items: center;
		object-fit: cover;
	}

	.right img {
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	h1 {
		font-family: TradeGothicBold;
		font-size: 60px;
		color: var(--brandWhite);
		text-decoration: none;
		font-weight: normal;
		margin-top: 0px;
		margin-bottom: 0px;
		border-bottom: solid 2px var(--brandYellow);
		padding: 0px;
		padding-bottom: 5px;
	}

	h2 {
		text-align: center;
		font-family: OpenSans;
		font-weight: normal;
		font-size: 22px;
		margin-top: 10px;
		color: var(--brandWhite);
	}

	/* Media Query for Tall Screens (Portrait Mode) */
	@media (max-aspect-ratio: 1/1) {
		.container {
			flex-direction: column; 
		}
		.left,
		.right {
			flex: none;
			width: 100%;
			height: 50%;
		}
		.left {
			border-bottom: solid 1px var(--brandLightBlue);
		}
		.right img {
			width: 100%; 
			height: 100%;
			border-bottom: solid 1px var(--brandLightBlue);
			object-fit: cover; 
		}
	}

	@media (max-width: 800px) {
		h1 {
			font-size: 40px; 
		}

		h2 {
			font-size: 20px; 
		}
		.logo-top {
			width: 225px;
		}
		.logo-bottom {
			width: 150px;
		}
	}

	@media (max-width: 600px) {
		.logo-top {
			width: 200px;
		}
		.logo-bottom {
			width: 125px;
		}
	}


	

	
</style>
