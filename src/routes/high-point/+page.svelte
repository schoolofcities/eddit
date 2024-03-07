<script>
	import Top from "../../lib/TopSofC.svelte";
	//import Map from '../lib/Map.svelte';
	//import { showHospitals, showCooling, showPool, showAptNoAir } from './stores.js';
	import "../../assets/global-styles.css";
	import Map from "../../lib/Map.svelte";
	import topImage from "../../assets/high-point-top-image.png";
</script>

<svelte:head>
	<meta
		name="viewport"
		content="width=device-width, initial-scale=1, minimum-scale=1"
	/>
</svelte:head>

<!-- <Top /> -->

<main>
	<div class="top-image" style="background-image: url('{topImage}');">
		<div class="title">
			<h1>High-Point Story Map</h1>
		</div>
	</div>

	<div class="text">
		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
			eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
			ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
			aliquip ex ea commodo consequat. Duis aute irure dolor in
			reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
			pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
			culpa qui officia deserunt mollit anim id est laborum.
		</p>

		<p>
			Sollicitudin aliquam ultrices sagittis orci a scelerisque purus.
			Vulputate sapien nec sagittis aliquam. Purus semper eget duis at.
			Elit sed vulputate mi sit. Nisl rhoncus mattis rhoncus urna neque.
			Sit amet nisl purus in. Rhoncus mattis rhoncus urna neque viverra
			justo nec ultrices dui. A erat nam at lectus urna. Porttitor rhoncus
			dolor purus non enim. Facilisis volutpat est velit egestas dui id
			ornare. Erat imperdiet sed euismod nisi. Dui ut ornare lectus sit
			amet. Est velit egestas dui id ornare. Urna nunc id cursus metus
			aliquam eleifend.
		</p>

	</div>

	<div class="image-mid-width">
		<img src="{topImage}" alt="Your Image">
		<p>Caption and/or source of image --- placeholder for now</p>
	</div>

	<div class="text">


		<h2>
			Section Heading
		</h2>
		<p>
			Vitae tortor condimentum lacinia quis vel eros donec ac odio. Mi
			quis hendrerit dolor magna eget est. Vivamus at augue eget arcu
			dictum varius. Ac placerat vestibulum lectus mauris ultrices eros in
			cursus turpis. Fusce ut placerat orci nulla. Et odio pellentesque
			diam volutpat commodo sed egestas egestas fringilla. Risus sed
			vulputate odio ut enim blandit volutpat. Enim diam vulputate ut
			pharetra sit amet aliquam id diam. Ut ornare lectus sit amet est.
			Tempor commodo ullamcorper a lacus. Diam phasellus vestibulum lorem
			sed.
		</p>
		<p>
			Quisque id diam vel quam elementum pulvinar etiam non quam. Faucibus
			pulvinar elementum integer enim neque volutpat. Consequat nisl vel
			pretium lectus. Eleifend quam adipiscing vitae proin sagittis nisl
			rhoncus. Tincidunt dui ut ornare lectus sit amet est. Eu augue ut
			lectus arcu bibendum at varius vel pharetra. Non diam phasellus
			vestibulum lorem sed risus. Diam sollicitudin tempor id eu nisl.
			Urna nunc id cursus metus aliquam eleifend mi in nulla.
		</p>
	</div>

	<div class="map">
		<Map />
	</div>

	<div class="text">


		<h2>
			Section Heading
		</h2>
		<p>
			Vitae tortor condimentum lacinia quis vel eros donec ac odio. Mi
			quis hendrerit dolor magna eget est. Vivamus at augue eget arcu
			dictum varius. Ac placerat vestibulum lectus mauris ultrices eros in
			cursus turpis. Fusce ut placerat orci nulla. Et odio pellentesque
			diam volutpat commodo sed egestas egestas fringilla. Risus sed
			vulputate odio ut enim blandit volutpat. Enim diam vulputate ut
			pharetra sit amet aliquam id diam. Ut ornare lectus sit amet est.
			Tempor commodo ullamcorper a lacus. Diam phasellus vestibulum lorem
			sed.
		</p>
		<p>
			Quisque id diam vel quam elementum pulvinar etiam non quam. Faucibus
			pulvinar elementum integer enim neque volutpat. Consequat nisl vel
			pretium lectus. Eleifend quam adipiscing vitae proin sagittis nisl
			rhoncus. Tincidunt dui ut ornare lectus sit amet est. Eu augue ut
			lectus arcu bibendum at varius vel pharetra. Non diam phasellus
			vestibulum lorem sed risus. Diam sollicitudin tempor id eu nisl.
			Urna nunc id cursus metus aliquam eleifend mi in nulla.
		</p>
	</div>
	
	
</main>

<style>


	.map {
		position: relative;
		width: 960px;
		margin: 0 auto;
		margin-bottom: 30px;
		overflow: hidden;
	}
</style>
