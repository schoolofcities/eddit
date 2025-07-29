<script>

	import "../../assets/global-styles.css"

	import Title from '$lib/Title.svelte';
	import Footer from "$lib/Footer.svelte";
	import Password from "$lib/Password.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/abq-title.jpg";

</script>


<Password/>

<Title
	title={"Albuquerque, NM"}
	subtitle={"Subtitle?"}
	image={titleImage}
/>

<main>

	<div class="text">

		<h1>Lorem ipsum title</h1>

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<GraphicSingle
		svg360={"./albuquerque-nm/web-svg/abq-contextmap-360.svg"}
		svg720={"./albuquerque-nm/web-svg/abq-contextmap-720.svg"}
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
		svg360={"./albuquerque-nm/web-svg/abq-trailmap-360.svg"}
		svg720={"./albuquerque-nm/web-svg/abq-trailmap-720.svg"}
		svg1080={"./albuquerque-nm/web-svg/abq-trailmap-1080.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<GraphicMultiples
		svgPaths={[
			"./albuquerque-nm/web-svg/abq-example-indy-360.svg", 
			"./albuquerque-nm/web-svg/abq-example-sanantonio-360.svg", 
			"./albuquerque-nm/web-svg/abq-example-charlotte-360.svg",
			"./albuquerque-nm/web-svg/abq-example-atlanta-360.svg"
		]}
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
		svg360={"./albuquerque-nm/web-svg/abq-visitor-chart-360.svg"}
		svg720={"./albuquerque-nm/web-svg/abq-visitor-chart-720.svg"}
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
		svg360={"./albuquerque-nm/web-svg/abq-hfin-360.svg"}
		svg720={"./albuquerque-nm/web-svg/abq-hfin-720.svg"}
	/>


	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<GraphicMultiples
		svgPaths={[
			"./albuquerque-nm/web-svg/abq-income-360.svg", 
			"./albuquerque-nm/web-svg/abq-rent-360.svg",
			"./albuquerque-nm/web-svg/abq-hispanic-360.svg"
		]}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

</main>

<Footer/>