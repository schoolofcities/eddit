<script>
	import { onMount } from "svelte";
	import maplibregl from "maplibre-gl";
	import * as pmtiles from "pmtiles";

	import BaseLayer from "../data/high-point-green.json";
	import cityBoundary from "../data/high-point-boundary.geo.json";
	import historicCentre from "../data/washington-historic-district.geo.json";
	import Papa from "papaparse";

	let map;
	let highPoint_features = [];
	let PMTILES_URL = "/eddit/high-point/high-point.pmtiles";
	let placeName = "";
	let address = "";
	let description = "";
	let photo_url;
	let id;
	let popup = false;
	const highPoint_points =
		"https://docs.google.com/spreadsheets/d/e/2PACX-1vTL72VgBythiJPdpp5iL-0KQjdmdw9UsfhJIRAYAqQjSIsh212Fw92HBOZX3JTmdpGgbCErukwYRQ3I/pub?gid=0&single=true&output=csv";

	const maxBounds = [
		[-80.1, 35.9], // SW coords
		[-79.9, 36.1], // NE coords
	];

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
		console.log(highPoints);
		
		highPoints.data.sort(function (a, b) {
			const nameA = (a.Name || "").toUpperCase();
			const nameB = (b.Name || "").toUpperCase();
			if (nameA < nameB) {
				return -1;
			}
			if (nameA > nameB) {
				return 1;
			}
			return 0;
		});

		for (let i = 0; i < highPoints.data.length; i++) {
			console.log(highPoints.data[i].Name);
		}

		// convert to geojson
		highPoints.data.forEach((point, i) => {
			highPoint_features.push({
				type: "Feature",
				properties: {
					ID: i + 1,
					ADDRESS: point.Address,
					NAME: point.Name,
					DESCRIPTION: point.Description,
					PHOTO_URL: "/eddit/high-point/" + point.ID_Long + ".png",
				},
				geometry: {
					type: "Point",
					coordinates: [point.X, point.Y],
				},
			});
		});
		console.log(highPoint_features)
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

		console.log(highPoint_geojson);

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
			center: [-79.997, 35.962],
			zoom: 15.5,
			maxZoom: 18,
			minZoom: 13,
			bearing: 0,
			scrollZoom: true,
			maxBounds: maxBounds,
			attributionControl: false,
		});

		map.touchZoomRotate.disableRotation();
		map.dragRotate.disable();
		map.touchZoomRotate.disableRotation();
		map.scrollZoom.disable();

		let protoLayers = BaseLayer;

		map.on("load", function () {
			placeName = highPoint_geojson.features[0].properties.NAME;
			address = highPoint_geojson.features[0].properties.ADDRESS;
			description = highPoint_geojson.features[0].properties.DESCRIPTION;
			photo_url = highPoint_geojson.features[0].properties.PHOTO_URL;
			id = highPoint_geojson.features[0].properties.ID;
			map.addSource("protomaps", {
				type: "vector",
				url: "pmtiles://" + PMTILES_URL,
				//attribution: attributionString,
				//attributionControl: false,
			});

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
				paint: {
					"raster-saturation": -0.5,
					"raster-opacity": 0.5,
				},
			});

			protoLayers.forEach((e) => {
				map.addLayer(e);
			});

			map.addSource("historicCentre", {
				type: "geojson",
				data: historicCentre,
			});

			map.addLayer({
				id: "historicCentre-lines",
				type: "line",
				source: "historicCentre",
				paint: {
					"line-color": "#012B5C",
					"line-width": 3,
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
					"circle-color": "#01A188",
					"circle-radius": 6,
					"circle-stroke-color": "white",
					"circle-stroke-width": 2,
				},
			});

			map.addLayer({
				id: "high-points-layer-select",
				type: "circle",
				source: "high-points",
				filter: ["==", ["get", "ID"], 1],
				paint: {
					"circle-color": "#F4D35E",
					"circle-radius": 8,
					"circle-stroke-color": "#012B5C",
					"circle-stroke-width": 4,
				},
			});
			map.on("mouseenter", "*", () => {
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
				map.setFilter("high-points-layer-select", [
					"==",
					["get", "ID"],
					id,
				]);

				popup = true;
				console.log(photo_url);
			});
		});
	});

	function zoomIn() {
		map.zoomIn();
	}

	function zoomOut() {
		map.zoomOut();
	}
	function handleMouseEnter() {
		map.getCanvas().style.cursor = "pointer";
	}
	function getNextImage() {
		if (
			id < highPoint_features[highPoint_features.length - 1].properties.ID
		) {
			id = id + 1;

			// get the info for the new ID
			var filtered = highPoint_features.filter(function (a) {
				return +a.properties.ID == id;
			});
			placeName = filtered[0].properties.NAME;
			address = filtered[0].properties.ADDRESS;
			description = filtered[0].properties.DESCRIPTION;
			photo_url = filtered[0].properties.PHOTO_URL;
			console.log(id);
		} else {
			id = 1;
			console.log(id);
		}

		map.setFilter("high-points-layer-select", ["==", ["get", "ID"], id]);
	}
	function getPreviousImage() {
		if (id > 1) {
			id = id - 1;

			// get the info for the new ID
			var filtered = highPoint_features.filter(function (a) {
				return +a.properties.ID == id;
			});
			placeName = filtered[0].properties.NAME;
			address = filtered[0].properties.ADDRESS;
			description = filtered[0].properties.DESCRIPTION;
			photo_url = filtered[0].properties.PHOTO_URL;
			console.log(id);
		} else {
			id = highPoint_features[highPoint_features.length - 1].properties.ID;
			console.log(id);
		}

		map.setFilter("high-points-layer-select", ["==", ["get", "ID"], id]);
	}
</script>

<div id="map-wrapper">
	<div id="map-title">
		<h3>Washington Street Historic District</h3>
	</div>

	<div id="map" on:mouseenter={handleMouseEnter}>
		
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
		<div id="switch-place">
			<div on:click={getPreviousImage} class="items">
				<svg width="24" height="24">
					<line
						x1="19"
						y1="6"
						x2="5"
						y2="13"
						stroke="#F1F7F7"
						stroke-width="4"
						stroke-linecap="round"
					/>
					<line
						x1="5"
						y1="13"
						x2="19"
						y2="20"
						stroke="#F1F7F7"
						stroke-width="4"
						stroke-linecap="round"
					/>
				</svg>
			</div>
			<div on:click={getNextImage} class="items">
				<svg width="24" height="24">
					<line
						x1="5"
						y1="6"
						x2="19"
						y2="13"
						stroke="#F1F7F7"
						stroke-width="4"
						stroke-linecap="round"
					/>
					<line
						x1="19"
						y1="13"
						x2="5"
						y2="20"
						stroke="#F1F7F7"
						stroke-width="4"
						stroke-linecap="round"
					/>
				</svg>
			</div>
		</div>

		<div id="place-text">
			<h3>{placeName}</h3>
			<p><i>{address}</i></p>
			<p>{description}</p>
			
		</div>

		<div id="place-photo">
			<img src={photo_url} alt="Photo of {placeName}" />
			<!--<img src={photo_url} alt={placeName}>-->
		</div>
	</div>
</div>

<style>
	#map-wrapper {
		margin: 0 auto;
		max-width: 960px;
		width: 100%;
		background-color: var(--e-global-color-white);
		border-top: solid 1px var(--e-global-color-green);
		border-bottom: solid 1px var(--e-global-color-green);
	}

	#map-title {
		margin: 0 auto;
		height: 40px;
		border-bottom: solid 1px var(--e-global-color-green);
	}

	#map-title h3 {
		/* width: 420px; */
		margin: 0 auto;
		margin-top: 5px;
		margin-bottom: 25px;
		font-size: 25px;
		color: var(--e-global-color-darkblue);
		text-align: center;
	}

	#map {
		width: 100%;
		top: 0px;
		/* border-top: 1px solid var(--brandBlack); */
		/* border-bottom: 1px solid var(--brandBlack); */
		height: 350px;
		border-bottom: solid 1px var(--e-global-color-green);
		position: relative;
		cursor: hand;
	}

	#info-wrapper {
		margin: 0 auto;
		min-height: 330px;
		/* height: 330px; */
		/* overflow: hidden; */
	}

	#switch-place {
		width: 100%;
		height: 40px;
		border-bottom: solid 1px var(--e-global-color-green);
		margin: 0 auto;
		margin-bottom: 10px;
		display: flex;
		justify-content: center; /* Center items horizontally */
		align-items: center; /* Center items vertically */
	}

	.items {
		/* display: block; */
		/*position: relative;*/

		padding-bottom: 3px;

		font-size: 23px;
		width: 24px;
		height: 24px;

		overflow: hidden;
		overflow-y: hidden;

		background-color: var(--e-global-color-green);
		color: var(--brandGray80);

		border: solid 1px var(--e-global-color-lightblue);
		/*border-radius: 24px;*/

		/* text-align: center; */

		margin: 0px;
		margin-right: 10px;

		/* margin-top: 5px;
		margin-bottom: 0px;
		margin-left: 10px; */
		/* margin: 0 auto; */
		/* float: left; */
		z-index: 2;
	}
	.items:hover {
		cursor: pointer;
		background-color: var(--brandYellow);
	}


	#place-text {
		float: left;
		padding-top: 0px;
		margin-top: 0px;
		width: 100%;
		max-width: 480px;
	}
	#place-text h3 {
		font-size: 26px;
		color: var(--e-global-color-darkblue);
		background-color: var(--e-global-color-yellow);
		border-bottom: solid 1px var(--e-global-color-yellow);
		padding-left: 10px;
		margin-right: 10px;
		margin-top: 0px;
		margin-bottom: 25px;
	}
	#place-text p {
		margin-top: -20px;
		padding: 10px;
		font-size: 16px;
		line-height: 24px;
		color: var(--e-global-color-black);
	}

	#place-photo {
		overflow: hidden;
		max-width: 480px;
		max-height: 270px;
		border: solid 1px var(--e-global-color-green);
		margin: 0px;
		margin-bottom: 10px;
		opacity: 0.8;
	}

	#place-photo img {
		max-width: 480px;
		width: 500px;
		height: 333px;
	}

	@media screen and (max-width: 960px) {
		#place-text {
			margin: 0 auto;
			max-width: 520px;
		}
		#info-wrapper {
			display: flex;
			flex-wrap: wrap;
		}
		#place-photo {
			overflow: hidden;
			max-width: 600px;
			border: solid 2px "red";
			margin: 0 auto;
			opacity: 0.8;
			padding-bottom: 60px;
			margin-bottom: 10px;
		}
		#place-photo img {
			max-width: 600px;
			padding-bottom: 10px;
		}
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