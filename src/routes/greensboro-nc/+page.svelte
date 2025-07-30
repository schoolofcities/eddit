<script>

	import "../../assets/global-styles.css"

	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/greensboro-title.jpg";

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		"first footnote"
	];
	

</script>





<!-- <Password/> -->

<Title
	title={"Increasing the availability of healthy food"}
	subtitle={"A case study of Greensboro, North Carolina"}
	image={titleImage}
	imageCaption={"___"}
	imageSource={"___"}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='' target='_blank'>Kathryn Exon Smith</a> & <a href='' target='_blank'>Sarah A. Smith</a>"}
			graphics={"<a href='' target='_blank'>Jeff Allen</a> & <a href='' target='_blank'>Isabeaux Graham</a>"}
			date={"August 2025"}
		/>

		<p>
			The availability of fresh, healthy, and affordable food is linked with reduced levels of obesity and diabetes, higher educational attainment, and longer life expectancy.<Footnote id={addFootnote(fns[0])} /> Yet access to healthy food can vary considerably within cities, leaving some neighbourhoods with limited options. Private-sector retailers are generally reluctant to open brick-and-mortar grocery stores in areas with lower incomes, reinforcing geographic and socioeconomic inequities. However, there are non-traditional opportunities for cities and local organizations to bring more healthy food options to communities that need them.
		</p>

	</div>

	<GraphicSingle
		svg720={"./greensboro-nc/web-svg/greensboro-contextmap-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-contextmap-360.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>


	<div class="callout">

		<h2>Greensboro boro boro borough</h2>

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<GraphicSingle
		svg1080={"./greensboro-nc/web-svg/greensboro-grocery-1080.svg"}
		svg720={"./greensboro-nc/web-svg/greensboro-grocery-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-grocery-360.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<GraphicSingle
		svg720={"./greensboro-nc/web-svg/greensboro-pop-growth-chart-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-pop-growth-chart-360.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<GraphicSingle
		svg1080={"./greensboro-nc/web-svg/greensboro-visits-1080.svg"}
		svg720={"./greensboro-nc/web-svg/greensboro-visits-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-visits-360.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<GraphicSingle
		svg1080={"./greensboro-nc/web-svg/greensboro-potential-1080.svg"}
		svg720={"./greensboro-nc/web-svg/greensboro-potential-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-potential-360.svg"}
	/>

	<Footnotes footnotes={footnotes} />

	<div class="details">

		<h2>Additional resources</h2>

		<p>
			List additional resources...
		</p>

	</div>
	

</main>

<Footer/>