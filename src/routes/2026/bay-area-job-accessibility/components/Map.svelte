<script>
    import { onMount } from 'svelte';
    import 'maplibre-gl/dist/maplibre-gl.css';
    import maplibregl, { createBaseMapStyle } from "#lib/maplibre.js";

    import BlockGroups from '../assets/block groups.geo.json';
    import Routes from '../assets/transit_routes.json';

    export let candidate = "transit";

    let pageHeight;
    let pageWidth;

    let mapHeight = 600;
    $: if (pageHeight < 800) {
        mapHeight = pageHeight - 200;
    } else {
        mapHeight = 600;
    }

    // ---------------------------------------------------------------
    // Views (buttons, legend titles, breaks, colours) -- from map.html
    // `column` is the property name in the combined block-group data below
    // ---------------------------------------------------------------
    const views = [
        {
            id: 'b',
            tab: 'Baseline',
            legend: 'Jobs Accessible with Current Transit',
            column: 'b',
            routes: true,
            breaks: [10000, 50000, 150000, 400000],
            labels: ['10K', '50K', '150K', '400K'],
            colours: ['#243662', '#387d9f', '#469f8a', '#98be48', '#eac640']
        },
        {
            id: 'r',
            tab: '40% Cuts',
            legend: 'Jobs Accessible at 40% Cuts to Transit',
            column: 'r',
            routes: false,
            breaks: [10000, 50000, 150000, 400000],
            labels: ['10K', '50K', '150K', '400K'],
            colours: ['#243662', '#387d9f', '#469f8a', '#98be48', '#eac640']
        },
        {
            id: 'l',
            tab: 'Mean Percent Loss',
            legend: 'Mean Percent of Jobs Inaccessible at 40% Cuts to Transit',
            column: 'l',
            routes: false,
            breaks: [10, 20, 30, 40],
            labels: ['10%', '20%', '30%', '40%'],
            colours: ['#85c5e5', '#9dadcd', '#9c84ae', '#9d588c', '#9e2666']
        }
    ];

    const noDataColour = '#d9d9d9';
    const layerOpacity = 0.85; // html map is fully opaque (1); lower it to let the basemap show through
    const hoverColour = '#000';

    let currentView = views[0];
    let filterOn = true;
    let routesOn = true;
    let map;
    let mapReady = false;

    // Bounds from map.html (the five-county Bay Area extent), with a little padding
    const maxBounds = [
        [-123.35, 36.65], // SW coords
        [-120.85, 38.35]  // NE coords
    ];

    function fillExpression(view) {
        const value = ['get', view.column];
        return [
            'case',
            ['==', value, null],
            noDataColour,
            [
                'step',
                value,
                view.colours[0],
                view.breaks[0], view.colours[1],
                view.breaks[1], view.colours[2],
                view.breaks[2], view.colours[3],
                view.breaks[3], view.colours[4]
            ]
        ];
    }

    function fmt(v, unit) {
        if (v === null || v === undefined) return 'No data';
        return unit === '%' ? v.toFixed(1) + '%' : v.toLocaleString('en-US');
    }

    function filterFor(on) {
        return on ? ['==', ['get', 'k'], 1] : null;
    }

    function paint() {
        if (!mapReady) return;
        const expr = fillExpression(currentView);
        map.setPaintProperty('BlockGroupsFill', 'fill-color', expr);
        map.setPaintProperty('BlockGroupsLine', 'line-color', expr);
        map.setLayoutProperty('TransitRoutes', 'visibility', currentView.routes && routesOn ? 'visible' : 'none');
    }

    function applyFilter() {
        if (!mapReady) return;
        map.setFilter('BlockGroupsFill', filterFor(filterOn));
        map.setFilter('BlockGroupsLine', filterFor(filterOn));
        popup.remove();
        map.setFilter('BlockGroupsHover', ['==', ['get', 'g'], '']);
    }

    function selectView(view) {
        currentView = view;
        paint();
    }

    function toggleFilter() {
        filterOn = !filterOn;
        applyFilter();
    }

    function toggleRoutes() {
        routesOn = !routesOn;
        paint();
    }

    let popup;

    function popupHTML(p) {
        const row = (id, label, val) =>
            `<div class="row${currentView.id === id ? ' on' : ''}"><span>${label}</span><span>${val}</span></div>`;
        return `<b>Block Group ${p.g}</b><div class="sub">${p.c} County</div>` +
            row('b', 'Current transit', fmt(p.b, 'jobs')) +
            row('r', 'At 40% cuts', fmt(p.r, 'jobs')) +
            row('l', 'Mean % inaccessible', fmt(p.l, '%'));
    }

    onMount(() => {
        map = new maplibregl.Map({
            container: candidate,
            style: createBaseMapStyle(),
            center: [-122.1, 37.5],
            zoom: 7.6,
            maxZoom: 16.5,
            minZoom: 7.5,
            bearing: 0,
            scrollZoom: true,
            maxBounds: maxBounds,
            attributionControl: false
        });
        map.addControl(new maplibregl.NavigationControl(), 'top-left');
        map.addControl(new maplibregl.AttributionControl({ compact: true }), 'bottom-right');
        // MapLibre opens the compact attribution by default; start it collapsed
        map.once('idle', () => {
            const attrib = map.getContainer().querySelector('.maplibregl-ctrl-attrib');
            attrib?.classList.remove('maplibregl-compact-show');
            attrib?.removeAttribute('open');
        });
        map.addControl(new maplibregl.ScaleControl(), 'bottom-left');
        map.scrollZoom.disable();

        popup = new maplibregl.Popup({
            closeButton: false,
            closeOnClick: false,
            offset: 14,
            anchor: 'top-left',
            className: 'bg-popup',
            maxWidth: '260px'
        });

        map.on('load', async function () {

            // Open elevation tiles (AWS Terrain Tiles), shaded by MapLibre
            map.addSource('Terrain', {
                type: 'raster-dem',
                tiles: [
                    'https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png'
                ],
                encoding: 'terrarium',
                tileSize: 256,
                maxzoom: 15,
                attribution: '<a href="https://github.com/tilezen/joerd/blob/master/docs/attribution.md" target="_blank">Terrain Tiles</a> (USGS, Mapzen)'
            });

            // Below the water layers so the bay and ocean stay flat
            map.addLayer({
                id: 'Hillshade',
                type: 'hillshade',
                source: 'Terrain',
                paint: {
                    'hillshade-exaggeration': 0.3,
                    'hillshade-illumination-direction': 315,
                    'hillshade-shadow-color': '#6b665e',
                    'hillshade-highlight-color': '#ffffff',
                    'hillshade-accent-color': '#8f8a82'
                }
            }, 'water');

            map.addSource('BlockGroups', {
                type: 'geojson',
                data: BlockGroups
            });
            map.addSource('Routes', {
                type: 'geojson',
                data: Routes
            });

            map.addLayer({
                id: 'BlockGroupsFill',
                type: 'fill',
                source: 'BlockGroups',
                layout: {},
                paint: {
                    'fill-color': fillExpression(currentView),
                    'fill-opacity': layerOpacity
                }
            });

            // Thin outline in the same colour as the fill (as in map.html) to hide seams
            map.addLayer({
                id: 'BlockGroupsLine',
                type: 'line',
                source: 'BlockGroups',
                layout: {},
                paint: {
                    'line-color': fillExpression(currentView),
                    'line-width': 0.5,
                    'line-opacity': layerOpacity
                }
            });

            map.addLayer({
                id: 'TransitRoutes',
                type: 'line',
                source: 'Routes',
                layout: {
                    visibility: currentView.routes && routesOn ? 'visible' : 'none',
                    'line-cap': 'round',
                    'line-join': 'round'
                },
                paint: {
                    'line-color': '#000',
                    'line-width': ['interpolate', ['linear'], ['zoom'], 4, 0.025, 8, 0.05, 12, 0.1, 16, .4],
                    'line-opacity': 1
                }
            });

            map.addLayer({
                id: 'BlockGroupsHover',
                type: 'line',
                source: 'BlockGroups',
                layout: {},
                filter: ['==', ['get', 'g'], ''],
                paint: {
                    'line-color': hoverColour,
                    'line-width': 2,
                    'line-opacity': 1
                }
            });

            mapReady = true;
            applyFilter();
            paint();

            if (pageHeight > 700 && pageWidth > 800) {
                map.zoomTo(8);
            }
        });

        map.on('mouseenter', 'BlockGroupsFill', () => {
            map.getCanvas().style.cursor = 'pointer';
        });

        map.on('mousemove', 'BlockGroupsFill', (e) => {
            const p = e.features[0].properties;
            map.setFilter('BlockGroupsHover', ['==', ['get', 'g'], p.g]);

            // Properties come back from the map with null as the string "null" in some
            // versions, so normalise before formatting.
            const clean = {};
            for (const key of Object.keys(p)) {
                clean[key] = (p[key] === 'null' || p[key] === null) ? null : p[key];
            }
            for (const key of ['b', 'r', 'l']) {
                if (clean[key] !== null) clean[key] = Number(clean[key]);
            }

            popup.setLngLat(e.lngLat).setHTML(popupHTML(clean)).addTo(map);
        });

        map.on('mouseleave', 'BlockGroupsFill', () => {
            map.getCanvas().style.cursor = '';
            map.setFilter('BlockGroupsHover', ['==', ['get', 'g'], '']);
            popup.remove();
        });

        return () => {
            popup.remove();
            map.remove();
        };
    });
</script>

<svelte:window bind:innerHeight={pageHeight} bind:innerWidth={pageWidth} />

<div class="wrap">
        <div class="legend">
            <div class="lt">{currentView.legend}</div>
            <div class="sw">
                {#each currentView.colours as colour}
                    <div style="background: {colour}; opacity: {layerOpacity}"></div>
                {/each}
            </div>
            <div class="lab">
                {#each currentView.labels as label, i}
                    <span style="left: {((i + 1) * 100) / currentView.colours.length}%">{label}</span>
                {/each}
            </div>
        </div>

    <div class="layout">
        <div class="map-col">
            <div id={candidate} class="map" style="height: {mapHeight}px"></div>
        </div>

        <div class="side" style="--map-h: {mapHeight}px">
            <div class="tabs" role="group" aria-label="Map view">
                {#each views as view}
                    <button
                        type="button"
                        aria-pressed={currentView.id === view.id}
                        on:click={() => selectView(view)}
                    >{view.tab}</button>
                {/each}
            </div>

            <div class="toggles">
                {#if currentView.routes}
                    <button type="button" aria-pressed={routesOn} on:click={toggleRoutes}>
                        Transit routes
                    </button>
                {/if}
                <button type="button" aria-pressed={filterOn} on:click={toggleFilter}>
                    Filter out low density areas
                </button>
            </div>
        </div>
    </div>
</div>

<style>
    /* Keeps the map the same width as the page text.
       Set --text-width on a parent (or change 700px here) to match your article column. */
    .wrap {
        width: 100%;
        max-width: var(--text-width, 700px);
        margin: 0 auto;
    }

    .layout {
        display: flex;
        align-items: flex-start;
        gap: 16px;
        position: relative; /* lets the buttons be placed in the side margin on wide screens, level with the map */
    }

    .map-col {
        flex: 1;
        min-width: 0; /* lets the map shrink inside the flex row */
    }

    .map {
        width: 100%;
        border: 1px solid grey;
    }

    /* Right-hand column: view buttons at the top, toggles at the bottom (level with the map's bottom edge) */
    .side {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        width: 150px;
        flex-shrink: 0;
        height: var(--map-h);
    }

    .tabs,
    .toggles {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    /* View buttons: black fill when selected */
    .tabs button,
    .toggles button {
        width: 100%;
        text-align: left;
        font-family: "Open Sans", Arial, Helvetica, sans-serif;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        cursor: pointer;
        border-radius: 4px;
    }

    .tabs button {
        padding: 9px 12px;
        border: 1.5px solid #000;
        background: #fff;
        color: #000;
        font-size: 13px;
        font-weight: 700;
    }

    .tabs button[aria-pressed="true"] {
        background: #000;
        color: #fff;
    }

    /* Toggle buttons (transit routes, low density filter): lighter, not bold */
    .toggles button {
        padding: 7px 12px;
        border: 1.5px solid #bbb;
        background: #fff;
        color: #666;
        font-size: 12px;
        font-weight: 400;
    }

    .toggles button:hover {
        border-color: #888;
    }

    .toggles button[aria-pressed="true"] {
        background: #eceff3;
        border-color: #6b7280;
        color: #222;
    }

    .tabs button:focus-visible,
    .toggles button:focus-visible {
        outline: 3px solid #888;
        outline-offset: 2px;
    }

    /* Wide screens (enough white space beside the text column):
       the map fills the full text width and the buttons sit in the right-hand margin.
       Breakpoint = text width + 2 x (button column 150px + 16px gap) + some breathing room.
       With a 700px text width that is about 1100px; raise it if you widen the text. */
    @media (min-width: 1100px) {
        .layout {
            display: block;
        }

        .side {
            position: absolute;
            top: 0;
            left: 100%;
            margin-left: 16px;
        }
    }

    /* Narrow screens: buttons go above the map in a row */
    @media (max-width: 700px) {
        .layout {
            flex-direction: column;
        }

        .map-col {
            width: 100%;
        }

        .side {
            order: -1;
            width: 100%;
            height: auto;
            gap: 8px;
        }

        .tabs,
        .toggles {
            flex-direction: row;
            flex-wrap: wrap;
        }

        .tabs button,
        .toggles button {
            width: auto;
        }
    }

    .legend {
        width: 100%;
        margin-bottom: 14px;
        font-family: "Open Sans", Arial, Helvetica, sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.02em;
        color: #000;
    }

    .lt {
        text-align: center;
        font-weight: 700;
        font-size: 13px;
        margin-bottom: 8px;
        letter-spacing: 0.04em;
    }

    .sw {
        display: flex;
        border: 1px solid #000;
    }

    .sw div {
        flex: 1;
        height: 16px;
    }

    .lab {
        position: relative;
        height: 18px;
        margin-top: 3px;
        font-size: 12px;
        font-weight: 600;
    }

    .lab span {
        position: absolute;
        top: 0;
        transform: translateX(-50%);
        white-space: nowrap;
    }

    /* Popup lives inside MapLibre's DOM, so it needs :global */
    :global(.bg-popup .maplibregl-popup-content) {
        background: #fff;
        color: #000;
        border: 1.5px solid #000;
        border-radius: 0;
        padding: 8px 10px;
        font-family: "Open Sans", Arial, Helvetica, sans-serif;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.02em;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
        pointer-events: none;
    }

    :global(.bg-popup .maplibregl-popup-tip) {
        display: none;
    }

    :global(.bg-popup) {
        pointer-events: none;
    }

    :global(.bg-popup b) {
        display: block;
        font-size: 12px;
    }

    :global(.bg-popup .sub) {
        color: #444;
        margin-bottom: 5px;
    }

    :global(.bg-popup .row) {
        display: flex;
        justify-content: space-between;
        gap: 14px;
    }

    :global(.bg-popup .row.on) {
        font-weight: 700;
    }
</style>