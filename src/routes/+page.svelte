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
	$: console.log(width);

</script>



<Password/>

<Title 
	title={"Equitable Development Data Insight Training"}
	subtitle={"Case studies from the 2023-24 cohort"} 
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
					In 2023 and 2024, The School of Cities partnered with the University of California, Berkeley to offer the Equitable Development Data Insight Training (EDDIT) Initiative, in collaboration with TheCaseMade, and funded by the Robert Wood Johnson Foundation. Equitable development is a broad term often used in cities to describe a range of initiatives aiming to reduce health, wealth, and wellbeing disparities within communities, with an intentional focus on disinvested places and communities of colour. Using this broad definition, the EDDIT Initiative trains coalitions, organizations, and institutions to leverage urban data and craft effective narratives to drive transformative for change in small and mid-sized cities across Canada and the U.S..
				</p>

				<p>
					The EDDIT Initiative trained a total of 10 organizations over the two year period, supporting them in understanding, interpreting, and applying urban data to advance locally driven change. This series of case studies, produced by the School of Cities, examines data insights and stories that emerged from our work with each organization, and features inspiring local projects in  Canadian and American cities. The case studies zoom out to discuss data analysis, visualization, and storytelling approaches that can be used to tackle mobilization, communication, and implementation challenges. Each case study highlights specific strategies, opportunities, and outcomes in urban data storytelling, offering insights into what works when pursuing and talking about inclusive city-building efforts. 
				</p>

			</div>

		</div>

	</div>

	<div class="right">

		{#if width >= 1430}

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

	<h2>Contributors. Acknowledgements.</h2>

	<p>
		Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
	</p>
	<p>
		Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
	</p>
	<p>
		Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
	</p>

</div>

