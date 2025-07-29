<script>

	import "../../assets/global-styles.css"

	import Title from '$lib/Title.svelte';
	import Footer from "$lib/Footer.svelte";
	import Password from "$lib/Password.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/cook-county-title.jpg";

</script>




<Password/>

<Title
	title={"Cook County, IL"}
	subtitle={"Hello world subtitle"}
	image={titleImage}
/>

<main>

	<div class="text">

		<br><br>
		<p>
			Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>
		<p>
			Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
		</p>

	</div>

	<GraphicSingle
		svg720={"./cook-county-il/web-svg/chicago-contextmap-720.svg"}
		svg360={"./cook-county-il/web-svg/chicago-contextmap-360.svg"}
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
		svg720={"./cook-county-il/web-svg/cook-county-contextmap-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county-contextmap-360.svg"}
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
		svg720={"./cook-county-il/web-svg/cook-county_GLT-policy-chart-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county_GLT-policy-chart-360.svg"}
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
		svg720={"./cook-county-il/web-svg/cook-county_landscape-contract-stat-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county_landscape-contract-stat-360.svg"}
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
		svgPaths={["./cook-county-il/web-svg/cook-county_income-map-360.svg", "./cook-county-il/web-svg/cook-county_minorities-map-360.svg"]}
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
		svgPaths={["./cook-county-il/web-svg/cook-county_NO2-map-360.svg", "./cook-county-il/web-svg/cook-county_PM25-pollution-map-360.svg", "./cook-county-il/web-svg/cook-county_ejc-map-360.svg"]}
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
		svg720={"./cook-county-il/web-svg/cook-county_gasvelectric-chart-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county_gasvelectric-chart-360.svg"}
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
		svgPaths={["./cook-county-il/web-svg/cook-county_asthma-map-360.svg", "./cook-county-il/web-svg/cook-county_dr-visits-map-360.svg"]}
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
		svg720={"./cook-county-il/web-svg/cook-county_commuters-arches-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county_commuters-arches-360.svg"}
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