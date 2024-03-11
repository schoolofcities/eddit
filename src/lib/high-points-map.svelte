<script>
	import { onMount } from "svelte";
	import maplibregl from "maplibre-gl";
	import * as pmtiles from "pmtiles";

	import BaseLayer from "../data/high-point-green.json";
	import cityBoundary from "../data/high-point-boundary.geo.json";
	import Papa from "papaparse";

	let map;
	let highPoint_features = [];
	let PMTILES_URL = "/eddit/high-point/high-point.pmtiles";
	let placeName = "meow";
	let address = "meow";
	let description = "meow";
	let photo_url;
	let id;
	let popup = false;
	const highPoint_points =
		"https://docs.google.com/spreadsheets/d/e/2PACX-1vTL72VgBythiJPdpp5iL-0KQjdmdw9UsfhJIRAYAqQjSIsh212Fw92HBOZX3JTmdpGgbCErukwYRQ3I/pub?gid=494432730&single=true&output=csv";

	//export let index;

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

	function getGoogleDrivePhoto(url){
		var urls = url.split('/')
		var image_url = `https://drive.google.com/uc?export=view&id=${urls[urls.length -2]}`
		return image_url
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
					ID: point.ID,
					ADDRESS: point.Address,
					NAME: point.Name,
					DESCRIPTION: point.Description,
					PHOTO_URL: point["Photo URL"],
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
			center: [-80, 35.9615],
			zoom: 15,
			maxZoom: 18,
			minZoom: 12,
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
			map.addSource("esri-sat", {
				type: "raster",
				tiles: [
					"https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
				],
				tileSize: 256,
				// attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
			});
			map.addLayer({
				id: "sat",
				type: "raster",
				source: "esri-sat",
			});

			// map.addSource("protomaps", {
			// 	type: "vector",
			// 	url: "pmtiles://" + PMTILES_URL,
			// 	//attribution: attributionString,
			// 	//attributionControl: false,
			// });

			// protoLayers.forEach((e) => {
			// 	map.addLayer(e);
			// });

			map.addLayer({
				id: "background-s",
				type: "background",
				paint: {
					"background-color": "#fff",
					"background-opacity": 0.4,
				},
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
					"circle-color": "#012B5C",
					"circle-radius": 6,
					"circle-stroke-color": "white",
					"circle-stroke-width": 2,
				},
			});

			map.addLayer({
				id: "high-points-layer-select",
				type: "circle",
				source: "high-points",
				filter: ["==", ["get", "ID"], 8],
				paint: {
					"circle-color": "#012B5C",
					"circle-radius": 6,
					"circle-stroke-color": "#F1C500",
					"circle-stroke-width": 4,
				},
			});
			map.on("mouseenter", "high-points-layer", () => {
				map.getCanvas().style.cursor = "pointer";
			});

			map.on("mouseleave", "high-points-layer", () => {
				map.getCanvas().style.cursor = "";
			});

			map.on("click", "high-points-layer", (e) => {
				console.log(e.features[0]);
				id = e.features[0].properties.ID;
				placeName = e.features[0].properties.NAME;
				address = e.features[0].properties.ADDRESS;
				description = e.features[0].properties.DESCRIPTION;
				photo_url = e.features[0].properties.PHOTO_URL;
				console.log(photo_url)
				map.setFilter("high-points-layer-select", [
					"==",
					["get", "ID"],
					id,
				]);
				// Calculate offset to position the popup next to the clicked point
				popup = true;
			});
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

<div id="map-wrapper">
	<div id="map-title">
		<h3>Washington Street</h3>
	</div>

	<div id="map">
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

	<div id="info-wrapper">
		<div id="switch-place"></div>
		<div id="place-text">
			{#if placeName == "meow"}
				<h3>Mt. Zion Baptist Church</h3>
				<p>753 Washington St, High Point, NC 27260</p>
				<p>
					Mt. Zion Baptist Church first started meeting on Washington
					Street in 1982 . This church continues to play an important
					role in the Washington Street and broader High Point
					community today.
				</p>
			{:else}
				<h3>{placeName}</h3>
				<p><i>{address}</i></p>
				<p>{description}</p>
			{/if}
		</div>
		<div id="place-photo">
			{#if placeName == "meow"}
			<img
			src="https://live.staticflickr.com/4782/40162484924_b7cd1ca809.jpg"
			width="500"
			height="333"
			alt="DSC_2920"
		/>
			{:else}
			<img
				src= {photo_url}
				width="500"
				height="333"
				alt="Your Image"
			/>
			{/if}
			<!--<img src={photo_url} alt={placeName}>-->
		</div>
	</div>
</div>

<style>
	#map-wrapper {
		margin: 0 auto;
		max-width: 960px;
		width: 100%;
		background-color: #01a18967;
		border-top: solid 1px var(--e-global-color-darkblue);
		border-bottom: solid 1px var(--e-global-color-darkblue);
	}

	#map-title {
		margin: 0 auto;
		height: 38px;
		border-bottom: solid 1px var(--e-global-color-darkblue);
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

	#map {
		width: 100%;
		top: 0px;
		/* border-top: 1px solid var(--brandBlack); */
		/* border-bottom: 1px solid var(--brandBlack); */
		height: 350px;
		border-bottom: solid 1px var(--e-global-color-darkblue);
		position: relative;
		cursor: hand;
	}

	#info-wrapper {
		margin: 0 auto;
		/* overflow: hidden; */
	}

	#switch-place {
		width: 100%;
		height: 19px;
		border-bottom: solid 1px var(--e-global-color-green);
	}

	#place-text {
		float: left;
		padding-top: 0px;
		margin-top: 0px;
		width: 100%;
		max-width: 480px;
		/* background-color: var(--e-global-color-yellow); */
	}
	#place-text h3 {
		font-size: 22px;
		color: var(--e-global-color-darkblue);
		border-bottom: solid 1px var(--e-global-color-green);
		padding-left: 10px;
		padding-right: 10px;
		margin-top: 5px;
	}
	#place-text p {
		margin-top: -20px;
		padding: 10px;
		font-size: 14px;
		line-height: 20px;
		color: var(--e-global-color-black);
	}

	#place-photo {
		overflow: hidden;
		max-width: 480px;
		max-height: 270px;
		border-left: solid 1px var(--e-global-color-green);
		margin: 5px;
	}
	#place-photo img {
		max-width: 480px;
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
