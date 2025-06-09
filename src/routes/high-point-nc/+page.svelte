<script>

	import "../../assets/global-styles.css"

	import Title from '$lib/Title.svelte';
	import Footer from "$lib/Footer.svelte";
	import SingleGraphic from "$lib/SingleGraphic.svelte";
	import SingleGraphicLazy from "$lib/SingleGraphicLazy.svelte";
	import SmallMultiples from "$lib/SmallMultiples.svelte";
	import SingleImage from "$lib/SingleImage.svelte";

	import titleImage from "./assets/high-point-title.png";

	import { CompareImage } from "svelte-compare-image";

</script>






<Title
	title={"High Point, NC"}
	subtitle={"Hello world subtitle"}
	image={titleImage}
/>

<main>

	<div class="text">

		<h1>Hello hello hello !!!!!!!! :)</h1>

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<SingleGraphicLazy
		svg720={"./high-point-nc/web-svg/highpoint-contextmap-720.svg"}
		svg360={"./high-point-nc/web-svg/highpoint-contextmap-360.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<SingleGraphicLazy
		svg720={"./high-point-nc/web-svg/high-point-map-720.svg"}
		svg360={"./high-point-nc/web-svg/high-point-map-360.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

		<h3>Aerial view of Washington Street in 1958 and 2023</h3>

	</div>

	<div style="max-width: 680px; margin: 0 auto;">
		<CompareImage
			imageLeftSrc="/eddit/high-point/imagery-1958.png"
			imageLeftAlt="left"
			imageRightSrc="/eddit/high-point/imagery-today.png"
			imageRightAlt="right"
			--handle-size="40px"
			--slider-color="#fff"
			--slider-width="5px"
		/>
	</div>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

		<h3>Koonts-McGhee Drug Store Building, 1954 and 2023</h3>
	
	</div>

	<SingleImage
		image={"/eddit/high-point/img-koonts-mcghee-drug-store.png"}
		subtitle={""}
		maxWidth={"680px"}
	/>


	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<SingleGraphicLazy
		svg720={"./high-point-nc/web-svg/highpoint-footfall-720.svg"}
		svg360={"./high-point-nc/web-svg/highpoint-footfall-360.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<SingleGraphicLazy
		svg720={"./high-point-nc/web-svg/high-point_employer-parity-720.svg"}
		svg360={"./high-point-nc/web-svg/high-point_employer-parity-360.svg"}
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