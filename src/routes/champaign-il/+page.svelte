<script>

	import "../../assets/global-styles.css"

	import Title from '$lib/Title.svelte';
	import Footer from "$lib/Footer.svelte";
	import SingleGraphic from "$lib/SingleGraphic.svelte";
	import SingleGraphicLazy from "$lib/SingleGraphicLazy.svelte";
	import SmallMultiples from "$lib/SmallMultiples.svelte";
	import SingleImage from "$lib/SingleImage.svelte";

	import titleImage from "./assets/champaign-title.jpg";

</script>






<Title
	title={"Champaign, IL"}
	subtitle={"Hello world subtitle"}
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

	<SingleGraphicLazy
		svg720={"./champaign-il/web-svg/champaign-contextmap-720.svg"}
		svg360={"./champaign-il/web-svg/champaign-contextmap-360.svg"}
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