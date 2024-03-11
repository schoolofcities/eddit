<script>
	import { onMount } from "svelte";
	import maplibregl from "maplibre-gl";
	import * as pmtiles from "pmtiles";

	import BaseLayer from "../data/high-point-green.json";
	import historicCentre from "../data/washington-historic-district.geo.json";
	import geohashGrid from "../data/high-point-geohashes-grid.geo.json";
	import notHighPoint from "../data/high-point-not-boundary.geo.json";

	let map;
	let highPoint_features = [];
	let PMTILES_URL = "/eddit/high-point/high-point.pmtiles";

	geohashGrid.features.forEach(feature => {
		const stops = feature.properties.stops;
		const daily_stops = (20 * stops) / 365;
		feature.properties.daily_stops = daily_stops;
	});

	/*
	const maxBounds = [
		[-79.771200, 43.440000], // SW coords
		[-78.914763, 43.930740] // NE coords
	];*/
	//
	

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
			zoom: 12.2,
			maxZoom: 18,
			minZoom: 11,
			bearing: 0,
			scrollZoom: true,
			//maxBounds: maxBounds,
			attributionControl: false,
		});

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
					"raster-saturation": 0,
					"raster-opacity": 0.5
				}
			});

			protoLayers.forEach((e) => {
			 	map.addLayer(e);
			});


			map.addSource("geohash-grid", {
				type: "geojson",
				data: geohashGrid
			});
			map.addLayer({
				id: "geohash-grid",
				type: "fill",
				source: "geohash-grid",
				paint: {
					'fill-color': [
						'step',
						['get', "daily_stops"],
							"#e8f7f4",
							500,
							"#99dacf",
							2500,
							"#3bb7a3",
							5000,
							"#007663",
					],
					"fill-opacity": 0.4
				},
			});
			map.addLayer({
				id: "geohash-grid-line",
				type: "line",
				source: "geohash-grid",
				paint: {
					"line-color": "white",
					"line-opacity": 0.25,
					"line-width": 1
				},
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

			map.addSource("not-high-point", {
				type: "geojson",
				data: notHighPoint,
			});
			map.addLayer({
				id: "not-high-point",
				type: "line",
				source: "not-high-point",
				paint: {
					"line-color": "#01A188",
					"line-width": 2
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
		<h3>High Point Visits Per Day</h3>
		<div id="legend">
			<svg width="300" height="40" xmlns="http://www.w3.org/2000/svg">
				<rect x="0" y="0" width="75" height="15" fill="#e8f7f4"/>
				<rect x="75" y="0" width="75" height="15" fill="#99dacf"/>
				<rect x="150" y="0" width="75" height="15" fill="#3bb7a3"/>
				<rect x="225" y="0" width="75" height="15" fill="#007663"/>

				<text class="legend-label" x="75" y="32" text-anchor="middle">500</text>
				<text class="legend-label" x="150" y="32" text-anchor="middle">2,500</text>
				<text class="legend-label" x="225" y="32" text-anchor="middle">5,000</text>
			</svg>
		</div>
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
		height: 72px;
		border-bottom: solid 1px var(--e-global-color-green);
	}

	#map-title h3 {
		width: 300px;
		margin: 0 auto;
		margin-top: 5px;
		margin-bottom: 5px;
		font-size: 21px;
		color: var(--e-global-color-darkblue);
		text-align: center;
	}

	#legend {
		margin: 0 auto;
		width: 300px;
		border-top: solid 1px var(--e-global-color-green)
	}
	.legend-label {
		fill: var(--e-global-color-darkblue);
	}

	#cellular-map {
		width: 100%;
		height: 500px;
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
