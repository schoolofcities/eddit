<script>

	import "../assets/global-styles.css"

	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import LandingCards from "$lib/LandingCards.svelte";

	import titleImage from "../assets/landing/collage.png"
	import map720 from "../../static/landing/landing-map-720.svg?raw"
	import map540 from "../../static/landing/landing-map-540.svg?raw"
	import map360 from "../../static/landing/landing-map-360.svg?raw"

	let width;

	let title = "Data Storytelling for Equitable Development"
	let subTitle = "Case studies from the 2023-24 EDDIT cohorts"

</script>


<svelte:head>

	<title>{title}  | School of Cities</title>

	<meta name="description" content={subTitle} />
	<meta name="author" content="School of Cities, University of Toronto">

	<meta property="og:title" content={title} />
	<meta property="og:description" content={subTitle} />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/design-components/" />
	<meta property="og:image" content="https://raw.githubusercontent.com/schoolofcities/eddit/main/static/web-card.png" />
	<meta property="og:locale" content="en_CA">

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content={title} />
	<meta name="twitter:description" content={subTitle} />
	<meta name="twitter:site" content="https://schoolofcities.github.io/eddit/" />
	<meta name="twitter:image" content="https://raw.githubusercontent.com/schoolofcities/eddit/main/static/web-card.png" /> 

</svelte:head>



<!-- <Password/> -->

<Title 
	title={"Data Storytelling for Equitable Development"}
	subtitle={"Case studies from the 2023-24 EDDIT cohorts"} 
	image={titleImage}
	imageCaption={""}
	imageSource={""}
	backgroundColour={"var(--brandDarkBlue)"}
/>

<div class="half-half-container" bind:offsetWidth={width}>

	<div class="left">

		<div class="text">

			<div class="callout">

				<h2>Equitable Development Data Insight Training	</h2>

				<p>
					In 2023 and 2024, the School of Cities partnered with the University of California, Berkeley to offer the <a href="https://www.equitabledev.org/about" target="_blank"> Equitable Development Data Insight Training (EDDIT) Initiative</a>, in collaboration with <a href="https://www.thecasemade.com/" target="_blank">TheCaseMade</a> and funded by the Robert Wood Johnson Foundation. <a href="https://doi.org/10.1177/08854122251350602" target="_blank">Equitable development</a> is a broad term often used in cities to describe initiatives that aim to reduce disparities in health, wealth, and well-being, with an intentional focus on disinvested places and communities of colour. Using this broad definition, the EDDIT Initiative trained coalitions, organizations, and institutions to leverage urban data and craft effective narratives to drive transformative change in communities across Canada and the United States.  
				</p>

				<p>
					The EDDIT Initiative worked with a total of 10 organizations in small and mid-sized cities over the two-year period, supporting them in understanding, interpreting, and applying urban data to advance locally driven change. This series of case studies, produced by the School of Cities, examines data insights and stories that emerged from our work with each organization, and features inspiring local projects in Canadian and American cities. The case studies zoom out to discuss data analysis, visualization, and storytelling approaches that can be used to tackle mobilization, communication, and implementation challenges more generally. Each case study highlights specific strategies, opportunities, and outcomes in urban data storytelling, offering insights into what works when pursuing and talking about inclusive city-building efforts. 
				</p>

				<p>
					Stay updated for future publications about our new <a href="https://www.equitabledev.org/clients" target="_blank">clients and their data stories</a>. 
				</p>

			</div>

		</div>

	</div>

	<div class="right">

		{#if width >= 1500}

			<div class="svg-container" style="--svg-width: 720px;">
				{@html map720}
			</div>

		{:else if width >= 600}

			<div class="svg-container" style="--svg-width: 720px;">
				{@html map540}
			</div>

		{:else}

			<div class="svg-container" style="--svg-width: 720px;">
				{@html map360}
			</div>

		{/if}

	</div>
	
</div>

<LandingCards/>


<div class="text">

	<h2>Acknowledgements</h2>

	<h3>The Case Study Team</h3>
	<p>
		<i>School of Cities, University of Toronto</i>
		<br>
		Karen Chapple Ph.D,
		Kathryn Exon Smith,
		Sarah A. Smith,
		Jeff Allen Ph.D,
		Isabeaux Graham,
		Julia Greenberg,
		Michelle Zhang,
		Evelyne St-Louis
	</p>

	<h3>The EDDIT Project Team</h3>
	<p>
		<i>University of Toronto & University of California, Berkeley </i>
		<br>
		Karen Chapple Ph.D.,
		Evelyne St-Louis,
		Michelle Zhang,
		Kathryn Exon Smith,
		Jeff Allen Ph.D.,
		Julia Greenberg
		Sara O’Connor Ph.D.,
		Paul Boniface Akaabre Ph.D.,
		Angel Yang,
		Nima Ashtari,
		Sandra Romero,
		Qi-Sheng Chen,
		Remus Herteg,
		Michael Liu,
		Cameron Kerr,
		Muhammad Khalis Bin Samion,
		Karen Trapenberg Frick Ph.D.

	</p>

	<h3>TheCaseMade</h3>
	<p>
		Tiffany Manuel (DrT) Ph.D.,
		Lindsay Knotts,
		Jennifer Rich,
		Mariel Ferreiro,
		Samara Crawford Herrera
	</p>

</div>

<br><br><br>


<Footer/>

