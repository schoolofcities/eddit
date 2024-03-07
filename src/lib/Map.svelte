<script>
	import { onMount } from "svelte";
	//import { showHospitals, showCooling, showPool, showAptNoAir } from '../routes/stores.js';
	import maplibregl from "maplibre-gl";
	import * as pmtiles from "pmtiles";

	import BaseLayer from "../data/high-point.json";
	import cityBoundary from "../data/high-point-boundary.geo.json";
	import Papa from "papaparse";

	let map;
	let highPoint_features = [];
	let PMTILES_URL = "/eddit/high-point.pmtiles";
	let addresses;
	let description; 
	let popup = false;
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
		console.log(highPoints)
		// convert to geojson
		highPoints.data.forEach((point) => {
			console.log(point)
			console.log(point.Address)
			console.log(point.Description)
			highPoint_features.push({
				type: "Feature",
				properties: {
					ADDRESS: point.Address,
					NAME: point.Name,
					DESCRIPTION: point.Description,
				},
				geometry: {
					type: "Point",
					coordinates: [point.X, point.Y],
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

		map.addControl(scale, "bottom-left");
		map.addControl(new maplibregl.NavigationControl(), "top-left");

		map.touchZoomRotate.disableRotation();
		map.dragRotate.disable();
		map.touchZoomRotate.disableRotation();
		map.scrollZoom.disable();

		let protoLayers = BaseLayer;

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
					"circle-color": "black",
					"circle-radius": 5,
					"circle-stroke-color": "white",
					"circle-stroke-width": 1,
				},
			});
			map.on("mouseenter", "high-points-layer", () => {
				map.getCanvas().style.cursor = "pointer";
			});

			map.on("mouseleave", "high-points-layer", () => {
				map.getCanvas().style.cursor = "";
			});

			map.on("click", "high-points-layer", (e) => {
				console.log(e.features[0])
				addresses = e.features[0].properties.ADDRESS
				description = e.efeatures[0].properties.DESCRIPTION
				// Calculate offset to position the popup next to the clicked point
				popup = true;
			});
			if (pageHeight > 700 && pageWidth > 800) {
				map.zoomTo(10.5);
			}
			/*
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

<div id="map" class="map"
	style="height: {mapHeight}px; width:{mapWidth}px; margin-top: 50px;"
> 
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
	<div class = "popup">
		<div class = "pop-text">
		<p>{addresses}</p> 
		<p>{description}</p>
		</div>
	</div>
</div>




<style>
	.map {
		width: 100%;
		border-top: 1px solid var(--brandBlack);
		border-bottom: 1px solid var(--brandBlack);
		height: auto;
		position:relative;
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
		margin-left: 30px;
		margin-top: 8px;
		margin-bottom: -2px;
	}

	h3 {
		margin-bottom: 10px;
		border-bottom: none;
	}

	.map-zoom-wrapper {
		position: absolute;
		margin-bottom: 2px;
		top: 85%;
		left: 5px;
		z-index: 2;
		font-family: TradeGothicBold;
		margin-left: 10%;
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
	.popup{
		position: absolute;
		top:0;
		width: 100%;
		height: 30%;
		opacity: 1;
	}
	.pop-text{
		position: absolute;
        top: 20%;
        left: 50%;
		width: 100%;
        transform: translate(-50%, -50%);
        padding: 20px;
        background-color: white;
        border: 1px solid black;
	}
</style>
