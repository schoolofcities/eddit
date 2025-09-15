<script>
	import "../assets/global-styles.css"

	// import uniLogos from "../assets/university-logos.svg"
	import berkLogo from "../assets/berkeley-logo.svg"
	import uoftLogo from "../assets/uoft-logo.svg"
	import edditLogo from "../assets/eddit-logo.svg"

	export let title = '';
	export let subtitle = '';
	export let image = '';
	export let imageCaption = '';
	export let imageSource = '';
	export let backgroundColour = 'var(--brandDarkBlue)';

</script>

<div class="container">

	<div class="left" style="background-color: {backgroundColour};">
		<div class="logo-top-container">
		  <a href="https://www.berkeley.edu/" target="_blank" class="logo-link">
		    <img src={berkLogo} alt="UC Berkeley Logo" class="logo-top-left" />
		  </a>
		  <a href="https://schoolofcities.utoronto.ca/" target="_blank" class="logo-link">
		    <img src={uoftLogo} alt="University of Toronto Logo" class="logo-top-right" />
		  </a>
		</div>
				
		<div class="title-text-container">
			<h1>{title}</h1>
			<h2>{subtitle}</h2>
		</div>
		<a href="https://www.equitabledev.org/" target="_blank" class="logo-link">
			<img src={edditLogo} alt="EDDIT Logo" class="logo-bottom" />
		</a>
	</div>
	<div class="right">
		<img src={image} alt="Photo of {subtitle}" />
	</div>
</div>

{#if imageCaption || imageSource}

	<p class="img-caption" >{@html imageCaption} <span id="image-source">{@html imageSource}</span></p>
	
{/if}

<div class="spacer"></div>

<style>
	.container {
		display: flex;
		height: 100vh;
		width: 100%;
		border-bottom: solid 1px var(--brandGray);
		margin-bottom: 0px;
	}

	.left {
		flex: 1;
		border-right: solid 1px var(--brandGray);
		display: flex;
		justify-content: center;
		align-items: center;
		text-align: left;
		position: relative;
	}

	.logo-top-container {
		position: absolute;
		top: 8px;
		left: 50%;
		transform: translateX(-50%);
		justify-content: center;
		align-items: center;
		width: 275px;
		height: auto;
		display: inline-flex;
	}

	.logo-top-left {
		max-width: 86.46px;
		width: 100%;
		height: 50px;
	}

	.logo-top-right{
		max-width: 188.54px;
		width: 100%;
		height: 50px;
	}

	.logo-bottom {
		width: 200px;
		height: auto;
		position: absolute;
		bottom: 24px;
		left: 50%;
		transform: translateX(-50%);
	}

	.logo-link {
		display: flex;
		justify-content: center;
		align-items: center;
		width: fit-content;
	}

	.logo-link:hover {
		opacity: 0.8;
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

	.title-text-container {
		margin-left: 35px;
		margin-right: 35px;
	}

	h1 {
		text-align: left;
		font-family: TradeGothicBold;
		color: var(--brandWhite);
		font-size: 54px;
		line-height: 62px;
		max-width: 720px;
		text-decoration: none;
		font-weight: normal;
		margin-top: 0px;
		margin-bottom: 0px;
		padding: 0px;
		padding-bottom: 10px;
		border-bottom: solid 2px var(--brandYellow);
	}

	h2 {
		text-align: left;
		font-family: SourceSerifItalic;
		color: var(--brandWhite);
		font-weight: normal;
		font-size: 24px;
		margin-top: 8px;
		max-width: 720px;
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

	@media (max-width: 1930px) {
		h1 {
			font-size: 48px;
			line-height: 54px;
		}
		h2 {
			font-size: 22px; 
		}
	}

	@media (max-width: 1500px) {
		h1 {
			font-size: 42px; 
			line-height: 50px;
		}

		h2 {
			font-size: 20px; 
		}
	}

	@media (max-width: 800px) {
		h1 {
			font-size: 32px; 
			line-height: 38px;
		}

		h2 {
			font-size: 16px; 
		}
		.logo-top-container{
			width: 225px;
		}
		.logo-bottom {
			width: 150px;
		}
	}

	@media (max-width: 600px) {

		.logo-top-container{
			width: 200px;
		}
		.logo-bottom {
			width: 125px;
		}
	}

	@media screen and (max-width: 600px) and (max-height: 900px) {
		.container {
			height: calc(100vh + 200px);
		}
	}

	p {
		text-align: right;
		padding-right: 3px;
		margin: 0px;
		box-sizing: border-box;
		width: 100%;
		font-family: OpenSansBold;
		font-weight: normal;
		font-size: 12px;
		line-height: 18px;
	}

	.img-caption {
		font-family: OpenSansBold;
		font-weight: normal;
		color: var(--brandGray70);
		margin-top: 2px;
		margin-bottom: 0px;
		padding-top: 0px;
	}

	#image-source {
		font-family: OpenSans;
		font-weight: normal;
		color: var(--brandGray50);
	}

	.spacer {
		background-color: none;
		height: 50px;
	}

	@media (max-width: 500px) {
		p {
			font-size: 10px;
		}
	}


</style>
