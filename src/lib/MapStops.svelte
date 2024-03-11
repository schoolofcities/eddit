<script>
	import { onMount } from "svelte";
	import maplibregl from "maplibre-gl";
	import * as pmtiles from "pmtiles";

	import BaseLayer from "../data/high-point-green.json";
	import historicCentre from "../data/washington-historic-district.geo.json";
	import Papa from "papaparse";

	let map;
	let highPoint_features = [];
	let PMTILES_URL = "/eddit/high-point/high-point.pmtiles";



	/*
	const maxBounds = [
		[-79.771200, 43.440000], // SW coords
		[-78.914763, 43.930740] // NE coords
	];*/
	// ============================functions=============================================

	

	onMount(async () => {
		let protocol = new pmtiles.Protocol();
		maplibregl.addProtocol("pmtiles", protocol.tile);

		// load map
		map = new maplibregl.Map({
			container: "cellular-map",
			style: {
				version: 8,
				name: "Empty",
				glyphs: "https://schoolofcities.github.io/fonts/fonts/{fontstack}/{range}.pbf",
				sources: {},
				layers: [
					{
						id: "background",
						type: "background",
						paint: {
							"background-color": "rgba(0,0,0,0)",
						},
					},
				],
			},
			center: [-79.997, 35.9615],
			zoom: 13,
			maxZoom: 18,
			minZoom: 11,
			bearing: 0,
			scrollZoom: true,
			//maxBounds: maxBounds,
			attributionControl: false,
		});

		// Convert the array into a single string

		// map.addControl(scale, "bottom-left");
		// map.addControl(new maplibregl.NavigationControl(), "top-left");

		map.touchZoomRotate.disableRotation();
		map.dragRotate.disable();
		map.touchZoomRotate.disableRotation();
		map.scrollZoom.disable();

		let protoLayers = BaseLayer;

		map.on("load", function () {

			 map.addSource("protomaps", {
			 	type: "vector",
			 	url: "pmtiles://" + PMTILES_URL,
			 	//attribution: attributionString,
			 	//attributionControl: false,
			});

			protoLayers.forEach((e) => {
	
			 	map.addLayer(e);
			 });

			map.addSource("historic-centre", {
				type: "geojson",
				data: historicCentre,
			});

			map.addLayer({
				id: "historic-centre-lines",
				type: "line",
				source: "historic-centre",
				paint: {
					"line-color": "#1E3765",
					"line-width": 2,
				},
			});
			
		
		});
	});

	function zoomIn() {
		map.zoomIn();
	}

	function zoomOut() {
		map.zoomOut();
	}
</script>

<div id="map-wrapper">
	<div id="map-title">
		<h3>High Point Activity Data</h3>
	</div>

	<div id="cellular-map">
		<div class="map-zoom-wrapper">
			<div on:click={zoomIn} class="map-zoom">
				<svg width="24" height="24">
					<line
						x1="5"
						y1="13"
						x2="19"
						y2="13"
						stroke="#4d4d4d"
						stroke-width="4"
					/>
					<line
						x1="12"
						y1="6"
						x2="12"
						y2="20"
						stroke="#4d4d4d"
						stroke-width="4"
					/>
				</svg>
			</div>
			<div on:click={zoomOut} class="map-zoom">
				<svg width="24" height="24">
					<line
						x1="5"
						y1="13"
						x2="19"
						y2="13"
						stroke="#4d4d4d"
						stroke-width="4"
					/>
				</svg>
			</div>
		</div>
	</div>
</div>

<style>
	#map-wrapper {
		margin: 0 auto;
		max-width: 960px;
		width: 100%;
		background-color:  var(--e-global-color-white);
		border-top: solid 1px var(--e-global-color-green);
	}

	#map-title {
		margin: 0 auto;
		height: 38px;
		border-bottom: solid 1px var(--e-global-color-green);
	}

	#map-title h3 {
		width: 300px;
		margin: 0 auto;
		margin-top: 5px;
		margin-bottom: 5px;
		font-size: 28px;
		color: var(--e-global-color-darkblue);
		text-align: center;
	}

	#cellular-map {
		width: 100%;
		height: 550px;
		border-bottom: solid 1px var(--e-global-color-green);
		position: relative;
		cursor: hand;
	}


	.map-zoom-wrapper {
		position: absolute;
		margin-bottom: 2px;
		top: 5px;
		left: 5px;
		z-index: 2;
		font-family: TradeGothicBold;
	}

	.map-zoom {
		/* display: block; */
		/* position: relative; */
		padding: 0px;
		padding-bottom: 3px;
		padding-left: 1px;
		margin: 0px;
		margin-bottom: -1px;
		font-size: 23px;
		width: 24px;
		height: 24px;
		overflow: hidden;
		overflow-y: hidden;
		background-color: var(--brandWhite);
		color: var(--brandGray80);
		border: solid 1px var(--brandGray);
		border-radius: 24px;
		margin-top: 5px;
		text-align: center;
		margin-left: 20%;
		/* margin: 0 auto; */
		z-index: 2;
	}
	.map-zoom:hover {
		cursor: pointer;
		background-color: var(--brandYellow);
	}
</style>
