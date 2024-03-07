<script>
	import Top from "../../lib/TopSofC.svelte";
	//import Map from '../lib/Map.svelte';
	//import { showHospitals, showCooling, showPool, showAptNoAir } from './stores.js';
	import "../../assets/global-styles.css";
	import Map from "../../lib/Map.svelte";
	import topImage from "../../assets/high-point-top-image.png";
</script>

/*<svelte:head>
	<meta
		name="viewport"
		content="width=device-width, initial-scale=1, minimum-scale=1"
	/>
</svelte:head>

<Top />

<main>
	<div class="top-image">
		<div class="centre-box">
			<div class="box">
				<h1>High-Point North Carolina <br />Story Map</h1>
			</div>
		</div>
		<img src={topImage} alt="High-Point North Carolina" />
	</div>

	<div class="title">
		<p>Authors, date</p>
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
	</div>

	<!--<Map index = "vulnerability" {showHospitals} {showCooling} {showPool} {showAptNoAir} />-->

	<div class="text">
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
			Urna nunc id cursus metus aliquam eleifend mi in nulla. Scelerisque
			in dictum non consectetur a erat nam at lectus. Sed viverra ipsum
			nunc aliquet bibendum. Faucibus a pellentesque sit amet porttitor
			eget dolor morbi non. Donec enim diam vulputate ut pharetra sit amet
			aliquam id. Morbi tristique senectus et netus et malesuada. Diam
			quis enim lobortis scelerisque fermentum. Pellentesque nec nam
			aliquam sem. Tortor dignissim convallis aenean et. Rhoncus dolor
			purus non enim praesent elementum facilisis leo vel. Arcu cursus
			euismod quis viverra nibh cras pulvinar mattis. Lectus magna
			fringilla urna porttitor rhoncus dolor purus non.
		</p>
	</div>
	<div class="map">
		<Map />
	</div>
	<!--<Map index = "heatdegree" {showHospitals} {showCooling} {showPool} {showAptNoAir} />-->

	<!--<Map index = "adaptive" {showHospitals} {showCooling} {showPool} {showAptNoAir} />-->

	<!--<Map index = "sensitivity" {showHospitals} {showCooling} {showPool} {showAptNoAir} />-->

	<div class="text">
		<h3>Data Sources:</h3>

		<p>
			Briefly describe data sources and methods, etc. <a
				href="https://github.com/Moraine729/Toronto_Heat_Vulnerability"
				>https://github.com/Moraine729/Toronto_Heat_Vulnerability</a
			>
		</p>
	</div>
</main>

<style>
	/* @font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: 'Roboto', sans-serif;
	} */
	/* #content {
		background-color: #B2A3B5;
		color: #black;
		font-size: 30px;
	} */
	.centre-box {
		position: absolute;
	}
	.top-image .box {
		width: auto; /* Adjust width as needed */
		min-width: 30vw;
		height: auto; /* Adjust height as needed */
		min-height: 300px;
		background-color: rgba(
			255,
			255,
			255,
			0.5
		); /* Semi-transparent white background */
		/* Add other styling properties as needed */
		display: flex;
		justify-content: center; /* Center horizontally */
		align-items: center; /* Center vertically */
	}
	.map {
		position: relative;
		width: auto;
		height: 30%;
		overflow: hidden;
	}
	h1 {
		text-align: center;
		font-size: 50px;
		padding: 50px;
	}
</style>
