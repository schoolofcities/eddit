<script>
	import { onMount } from "svelte";
	//import { showHospitals, showCooling, showPool, showAptNoAir } from '../routes/stores.js';
	import maplibregl from "maplibre-gl";
	import * as pmtiles from "pmtiles";
	/*
	import Wards from "../data/wards.geo.json";
	import WardPts from "../data/wards-pts.geo.json";
	import Vulnerdata from "../data/data-reduced-final.geo.json";
	import Cooling from "../data/indoor-cooling-centres.geo.json";
	import Pool from "../data/swimming-wading-pools.geo.json";
	import AptNoAir from "../data/apt-no-aircon.geo.json";
	import Hospitals from "../data/hospitals.geo.json";
	import SubwayLines from "../data/subwayLines.geo.json";
	import SubwayStns from "../data/subwayStations.geo.json";*/
	import BaseLayer from "../data/high-point.json";
	import cityBoundary from "../data/high-point-boundary.geo.json";
	import Papa from "papaparse";

	let map;
	let highPoint_features = [];
	let PMTILES_URL = "/eddit/high-point.pmtiles";

	const highPoint_points =
		"https://docs.google.com/spreadsheets/d/e/2PACX-1vTL72VgBythiJPdpp5iL-0KQjdmdw9UsfhJIRAYAqQjSIsh212Fw92HBOZX3JTmdpGgbCErukwYRQ3I/pub?gid=494432730&single=true&output=csv";

	//export let index;

	let pageHeight;
	let pageWidth;

	let mapHeight = 600;
	$: if (pageHeight < 800) {
		mapHeight = pageHeight - 250;
	} else {
		mapHeight = 600;
	}

	let mapWidth = pageWidth;

	// Adding scale bar to the map
	let scale = new maplibregl.ScaleControl({
		maxWidth: 100,
		unit: "metric",
	});

	/*
	// Function to toggle the visibility of Hospitals layer
	function toggleHospitals() {
		showHospitals.update((value) => !value);
		updateLayerVisibility('hospitals', $showHospitals);
	}

	// Function to toggle the visibility of Cooling Centres layer
	function toggleCooling() {
		showCooling.update((value) => !value);
		updateLayerVisibility('cooling-cnts', $showCooling);
	}

	// Function to toggle the visibility of Swimming/Wading Pools layer
	function togglePool() {
		showPool.update((value) => !value);
		updateLayerVisibility('pool-locs', $showPool);
	}

	// Function to toggle the visibility of Apartments without Air Condition layer
	function toggleAptNoAir() {
		showAptNoAir.update((value) => !value);
		updateLayerVisibility('AptNoAir', $showAptNoAir);
	}

	function updateLayerVisibility(layerID, visibility) {
		if (map) {
		map.setPaintProperty(layerID, 'circle-opacity', visibility ? 1 : 0);
		map.setPaintProperty(layerID, 'circle-stroke-opacity', visibility ? 1 : 0);
		}
	}

	$: updateLayerVisibility('hospitals', $showHospitals);
	$: updateLayerVisibility('cooling-cnts', $showCooling);
	$: updateLayerVisibility('pool-locs', $showPool);
	$: updateLayerVisibility('AptNoAir', $showAptNoAir);
  */
	/*
	const maxBounds = [
		[-79.771200, 43.440000], // SW coords
		[-78.914763, 43.930740] // NE coords
	];*/
	// ============================functions=============================================

	// load the google sheet csv data
	async function processCsv(csvLink) {
		const response = await fetch(csvLink);
		const csvData = await response.text();
		const result = await new Promise((resolve) => {
			Papa.parse(csvData, {
				complete: (result) => resolve(result),
				header: true,
				dynamicTyping: true,
				skipEmptyLines: true,
			});
		});

		return result;
	}

	onMount(async () => {
		let protocol = new pmtiles.Protocol();
		maplibregl.addProtocol("pmtiles", protocol.tile);

		// load csv data
		var highPoints = await processCsv(highPoint_points);
		
		// convert to geojson
		highPoints.data.forEach((point) => {
			highPoint_features.push({
				type: "Feature",
				properties: {
					address: point.ADDRESS,
					ID: point.ID,
					STATE: point.STATE,
					ADD_TYPE: point.ADD_TYPE,
				},
				geometry: {
					type: "Point",
					coordinates: [point.LON, point.LAT],
				},
			});
		});
		// create geojson
		var highPoint_geojson = {
			type: "FeatureCollection",
			crs: {
				type: "name",
				properties: {
					name: "urn:ogc:def:crs:OGC:1.3:CRS84",
				},
			},
			features: highPoint_features,
		};
		console.log(highPoint_geojson)

		// load map
		map = new maplibregl.Map({
			container: "map",
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
			center: [-80.0029, 35.9598],
			zoom: 12,
			maxZoom: 13,
			minZoom: 10,
			bearing: 0,
			//projection: 'globe',
			scrollZoom: true,
			//maxBounds: maxBounds,
			attributionControl: true,
		});

		const attributions = [
			'<a href="https://openstreetmap.org">OpenStreetMap</a>',
			// '<a href="https://github.com/Moraine729/Toronto_Heat_Vulnerability">Github</a>',
			'<a href="https://open.toronto.ca/">City of Toronto </a>',
		];

		// Convert the array into a single string
		const attributionString = attributions.join(", ");
		/*
		map.addControl(scale, 'bottom-left');
		// map.addControl(new maplibregl.NavigationControl(), 'top-left');
		
		map.touchZoomRotate.disableRotation();
		map.dragRotate.disable();
		map.touchZoomRotate.disableRotation();
		map.scrollZoom.disable();

		*/
		let protoLayers = BaseLayer;
		console.log(highPoints.data[0].ID);
		//for (let i = 0; i < highPoints.data.length; i++) {
		//console.log(highPoints.data[i].ID);
		//console.log(highPoints.data[i].ADDRESS)
		//console.log(highPoints.data[i].LAT)
		//console.log(highPoints.data[i].LON)
		//}

		map.on("load", function () {
			// Add the source with the concatenated attribution string
			map.addSource("protomaps", {
				type: "vector",
				url: "pmtiles://" + PMTILES_URL,
				//attribution: attributionString,
				//attributionControl: false,
			});

			protoLayers.forEach((e) => {
				map.addLayer(e);
			});

			map.addSource("cityBoundary", {
				type: "geojson",
				data: cityBoundary,
			});

			map.addLayer({
				id: "cityBoundary-lines",
				type: "line",
				source: "cityBoundary",
				paint: {
					"line-color": "#1E3765",
					"line-width": 1,
				},
			});
			map.addSource("high-points", {
				type: "geojson",
				data: highPoint_geojson,
			});

			map.addLayer({
				id: "high-points-layer",
				type: "circle",
				source: "high-points",
				paint: {
					"circle-color": "#a9d6e5",
					"circle-radius": 5,
					"circle-stroke-color": "red",
					"circle-stroke-width": 2,
				},
				//before: "transit-line-bold-ID",
			});
			/*
			if (pageHeight > 700 && pageWidth > 800) {
				map.zoomTo(10.5)
			}

			updateLayerVisibility('hospitals', $showHospitals);
			updateLayerVisibility('cooling-cnts', $showCooling);
			updateLayerVisibility('pool-locs', $showPool);
			updateLayerVisibility('AptNoAir', $showAptNoAir);

			map.setLayoutProperty('Vulnerdata', 'visibility', 'visible');
		*/
		});
	});

	function zoomIn() {
		map.zoomIn();
	}

	function zoomOut() {
		map.zoomOut();
	}
</script>

<!--
<div class="legend">
	
	<h3>{indexs[index].name}</h3>-->

<!-- <p>Index of </p> -->
<!--
	<div style="height: 20px">
		<div
			class="legend-bar"
			style="background-image: linear-gradient(to right,{indexs[index]
				.colours[0]},{indexs[index].colours[1]})"
		></div>
		<div
			class="legend-bar"
			style="background-image: linear-gradient(to right,{indexs[index]
				.colours[1]},{indexs[index].colours[2]})"
		></div>
		<div
			class="legend-bar"
			style="background-image: linear-gradient(to right,{indexs[index]
				.colours[2]},{indexs[index].colours[3]})"
		></div>
		<p>| Lo<span style="letter-spacing: 177px">w</span>| High</p>
	</div>
</div>-->

<div
	id="map"
	class="map"
	style="height: {mapHeight}px; width:{mapWidth}px; margin-top: 50px;"
>
	<!--
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
	</div>-->
</div>

<!--
<div class="buttons">
	<button
		on:click={togglePool}
		class:layerOn={$showPool}
		class:layerOff={!$showPool}>Outdoor Swimming & Wading Pools</button
	>
	<button
		on:click={toggleCooling}
		class:layerOn={$showCooling}
		class:layerOff={!$showCooling}>Cooling Centres</button
	>
	<br />
	<button
		on:click={toggleHospitals}
		class:layerOn={$showHospitals}
		class:layerOff={!$showHospitals}
	>
		Hospitals</button
	>
	<button
		on:click={toggleAptNoAir}
		class:layerOn={$showAptNoAir}
		class:layerOff={!$showAptNoAir}
	>
		Apartments Without Air Conditioning</button
	>
</div>-->

<style>
	.map {
		width: 100%;
		border-top: 1px solid var(--brandBlack);
		border-bottom: 1px solid var(--brandBlack);
	}

	.legend {
		max-width: 615px;
		height: 40px;
		margin: 0 auto;
		padding-left: 15px;
	}
	.legend-bar {
		width: 75px;
		height: 15px;
		display: inline-block;
		margin-left: -5px;
	}

	.buttons {
		max-width: 500px;
		width: 100%;
		margin: 0 auto;
		padding-top: 5px;
		padding-bottom: 5px;
	}
	@media screen and (max-width: 500px) {
		.buttons {
			max-width: 250px;
		}
	}

	button {
		font-family: RobotoBold;
		text-align: left;
		font-size: 14px;
		width: 245px;
		color: white;
		border: 1px solid var(--brandGray);
		padding: 5px;
		margin-bottom: 5px;
		cursor: pointer;
	}

	button:hover {
		opacity: 1;
		background-color: var(--brandYellow);
	}

	.layerOn {
		background-color: white;
		opacity: 1;
		color: var(--brandDarkBlue);
		border: 1px solid var(--brandDarkBlue);
	}

	.layerOff {
		background-color: white;
		color: var(--brandDarkBlue);
		opacity: 0.5;
	}

	p {
		margin-top: -8px;
		margin-bottom: -2px;
	}

	h3 {
		margin-bottom: 10px;
		border-bottom: none;
	}

	.map-zoom-wrapper {
		margin-top: 2px;
		left: 5px;
		position: absolute;
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
		/* margin: 0 auto; */
		z-index: 2;
	}
	.map-zoom:hover {
		cursor: pointer;
		background-color: var(--brandYellow);
	}
</style>
