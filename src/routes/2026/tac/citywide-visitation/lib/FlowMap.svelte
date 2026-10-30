<script>
	// Figure 5: strongest flows of Scarborough residents' activity between Scarborough wards,
	// plus the largest flows that leave Scarborough
	import { wards as scarbWards, flows, venues, meta } from "../assets/scarborough_network.json";
	import { wards as mapWards } from "../assets/ward_map.json";
	import Figure from "./Figure.svelte";
	import Tip from "./Tip.svelte";
	import { regionOf, tint, tipPos } from "./theme.js";

	let width = 720;
	let tip = null;

	const PINK = regionOf("Scarborough").colour;
	const OUT = "#4d4d4d"; // brandGray70: flows that leave Scarborough
	// flows are drawn above a minimum size. Flows leaving Scarborough are much larger than those between its wards,
	// so the cut-offs differ: this keeps the map balanced without crowding it.
	const MIN_INTERNAL = 55; // normalized activity units
	const MIN_OUT = 330;
	const UNITS_MAX = 800; // common width scale for both kinds of flow

	// map window (degrees); x is stretched by cos(latitude) so the map is not squashed
	const LON = [-79.455, -79.095];
	const LAT = [43.625, 43.86];
	const KX = Math.cos((43.74 * Math.PI) / 180);
	const SPAN = { x: (LON[1] - LON[0]) * KX, y: LAT[1] - LAT[0] };

	// label offsets in px at full width (dx, dy, anchor), tuned by eye
	const WARD_LABEL = {
		"Scarborough Southwest": [12, 5, "start"],
		"Scarborough Centre": [-18, 24, "end"],
		"Scarborough-Agincourt": [-18, -17, "end"],
		"Scarborough North": [0, -18, "middle"],
		"Scarborough-Guildwood": [12, 24, "start"],
		"Scarborough-Rouge Park": [0, -19, "middle"]
	};
	const OUT_LABEL = {
		"University-Rosedale": [-8, 22, "middle"],
		"Toronto Centre": [14, 22, "start"],
		"Spadina-Fort York": [10, 4, "start"],
		Willowdale: [-4, -14, "middle"]
	};
	// curvature of an arc, as a fraction of its length (positive bends to the left of travel)
	const BEND = {
		"Scarborough North>Scarborough-Agincourt": 0.16,
		"Scarborough North>Scarborough-Rouge Park": -0.16,
		"Scarborough Centre>Scarborough-Agincourt": 0.16,
		"Scarborough Southwest>University-Rosedale": 0.1,
		"Scarborough Southwest>Toronto Centre": -0.12,
		"Scarborough Centre>Spadina-Fort York": 0.1
	};

	const wardNode = Object.fromEntries(scarbWards.map((w) => [w.ward_name, w]));
	const point = Object.fromEntries(mapWards.map((w) => [w.name, w.point]));
	for (const w of scarbWards) point[w.ward_name] = [w.representative_point.lon, w.representative_point.lat];

	const internal = flows.filter((f) => f.bucket === "other_scarborough" && f.units >= MIN_INTERNAL).sort((a, b) => a.units - b.units);
	const outgoing = flows.filter((f) => f.bucket !== "same_ward" && f.bucket !== "other_scarborough" && f.units >= MIN_OUT).sort((a, b) => a.units - b.units);
	const outDests = [...new Set(outgoing.map((f) => f.dest_ward))];
	const maxVenue = Math.max(...venues.map((v) => v.activity_total));

	const received = Object.fromEntries(scarbWards.map((w) => [w.ward_name, w.received_from_other_scarborough]));
	const maxReceived = Math.max(...Object.values(received));

	$: cw = Math.max(300, width - 40);
	$: compact = cw < 560;
	$: k = cw / SPAN.x; // px per degree of latitude
	$: height = Math.round(SPAN.y * k);
	$: s = Math.min(1, cw / 680); // scale for text and offsets on narrow screens
	$: px = ([lon, lat]) => [(lon - LON[0]) * KX * k, (LAT[1] - lat) * k];
	$: pathOf = (rings) => rings.map((r) => "M" + r.map((c) => px(c).map((v) => v.toFixed(1)).join(",")).join("L") + "Z").join("");
	$: radius = (name) => 4.5 + 6.5 * Math.sqrt((received[name] || 0) / maxReceived);
	$: lw = (units) => (0.8 + 3.4 * units / UNITS_MAX) * Math.max(0.7, s);

	// an arc from a to b with an arrowhead at b. Ends are pulled back by r1 / r2 px.
	$: arrow = (a, b, bend, w, r1, r2) => {
		const [x1, y1] = px(a);
		const [x2, y2] = px(b);
		const dx = x2 - x1;
		const dy = y2 - y1;
		const len = Math.hypot(dx, dy);
		const cx = (x1 + x2) / 2 - dy * bend;
		const cy = (y1 + y2) / 2 + dx * bend;
		const unit = (x, y) => {
			const l = Math.hypot(x, y) || 1;
			return [x / l, y / l];
		};
		const [ux, uy] = unit(cx - x1, cy - y1);
		const [vx, vy] = unit(x2 - cx, y2 - cy);
		const head = 4.5 + 1.5 * w;
		const sx = x1 + ux * r1;
		const sy = y1 + uy * r1;
		const tx = x2 - vx * r2; // arrow tip
		const ty = y2 - vy * r2;
		const bx = tx - vx * head; // base of the arrowhead, where the line stops
		const by = ty - vy * head;
		const hw = head * 0.42;
		return {
			line: `M${sx.toFixed(1)} ${sy.toFixed(1)}Q${cx.toFixed(1)} ${cy.toFixed(1)} ${bx.toFixed(1)} ${by.toFixed(1)}`,
			head: `M${tx.toFixed(1)} ${ty.toFixed(1)}L${(bx - vy * hw).toFixed(1)} ${(by + vx * hw).toFixed(1)}L${(bx + vy * hw).toFixed(1)} ${(by - vx * hw).toFixed(1)}Z`,
			len
		};
	};

	const NOTE = "Normalized activity units (not raw counts of visitors)";

	const showFlow = (e, f, kind) => {
		tip = {
			...tipPos(e),
			title: `${f.origin_ward} → ${f.dest_ward}`,
			subtitle: kind === "in" ? "Flow within Scarborough" : "Flow leaving Scarborough",
			rows: [
				["Normalized activity", Math.round(f.units).toLocaleString("en-CA"), kind === "in" ? PINK : OUT],
				["Share of origin ward’s activity", `${(f.share_of_origin * 100).toFixed(1)}%`]
			],
			note: NOTE
		};
	};
	const showNode = (e, name) => {
		tip = {
			...tipPos(e),
			title: name,
			rows: [["Received from other Scarborough wards", Math.round(received[name]).toLocaleString("en-CA")]],
			note: NOTE
		};
	};
	const showVenue = (e, v) => {
		tip = {
			...tipPos(e),
			title: v.venue_name,
			subtitle: v.ward_name,
			rows: [
				["Normalized activity", Math.round(v.activity_total).toLocaleString("en-CA")],
				["Share of Scarborough venue activity", `${(v.share_of_scarborough_destination_activity * 100).toFixed(1)}%`]
			],
			note: NOTE
		};
	};
	const hideTip = () => (tip = null);
</script>

<Figure
	title="Scarborough’s wards already share a network of venues"
	subtitle="Flows of Scarborough residents’ activity between Scarborough wards and to wards elsewhere in Toronto. Arrows run from a resident’s home ward to the ward of the venue; hover for details."
	caption="Only flows of at least {MIN_INTERNAL} units within Scarborough and {MIN_OUT} units leaving it are drawn. Arrows join ward points, not venue locations, and show straight-line geography rather than routes."
	source="Source: ward-mapped, normalized mobile-device activity at {meta.n_venues} study venues; the {venues.length} in Scarborough are shown."
	bind:width
>
	<div class="legend">
		<span class="item">
			<svg width="30" height="14" aria-hidden="true"><path d="M2 7H22" stroke={PINK} stroke-width="3" /><path d="M28 7L21 3.5V10.5Z" fill={PINK} /></svg>
			Flow between Scarborough wards
		</span>
		<span class="item">
			<svg width="30" height="14" aria-hidden="true"><path d="M2 7H22" stroke={OUT} stroke-width="3" stroke-dasharray="4 2.5" /><path d="M28 7L21 3.5V10.5Z" fill={OUT} /></svg>
			Flow to a ward outside Scarborough
		</span>
		<span class="item">
			<svg width="16" height="16" viewBox="-8 -8 16 16" aria-hidden="true"><circle r="6" fill="#fff" stroke={PINK} stroke-width="2" /></svg>
			Ward (larger = receives more from other Scarborough wards)
		</span>
		<span class="item">
			<svg width="14" height="14" viewBox="-7 -7 14 14" aria-hidden="true"><path d="M0 -5.5L5.5 0L0 5.5L-5.5 0Z" fill="#191919" /></svg>
			Study venue (larger = more activity)
		</span>
	</div>

	<svg width={cw} {height} viewBox="0 0 {cw} {height}" role="img" aria-label="Map of Scarborough with arrows showing the strongest flows of residents' activity between Scarborough wards and to wards outside Scarborough">
		<!-- wards: each tinted by its region -->
		{#each mapWards as w}
			{@const region = regionOf(w.region)}
			<path d={pathOf(w.rings)} fill={tint(region.colour, w.region === "Scarborough" ? 0.2 : 0.09)} stroke="#fff" stroke-width="1.2" stroke-linejoin="round" />
		{/each}

		<!-- flows leaving Scarborough, then flows within it (stronger, on top) -->
		{#each outgoing as f}
			{@const a = arrow(point[f.origin_ward], point[f.dest_ward], BEND[`${f.origin_ward}>${f.dest_ward}`] ?? 0.08, lw(f.units), radius(f.origin_ward) + 2, 7)}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g on:mousemove={(e) => showFlow(e, f, "out")} on:focus={(e) => showFlow(e, f, "out")} on:mouseleave={hideTip} on:blur={hideTip} role="img" tabindex="0" aria-label="{f.origin_ward} to {f.dest_ward}">
				<path d={a.line} fill="none" stroke="transparent" stroke-width="14" />
				<path d={a.line} fill="none" stroke={OUT} stroke-width={lw(f.units)} stroke-dasharray="{5 * Math.max(0.7, s)} {3 * Math.max(0.7, s)}" opacity="0.5" />
				<path d={a.head} fill={OUT} opacity="0.6" />
			</g>
		{/each}
		{#each internal as f}
			{@const a = arrow(point[f.origin_ward], point[f.dest_ward], BEND[`${f.origin_ward}>${f.dest_ward}`] ?? 0.1, lw(f.units), radius(f.origin_ward) + 1.5, radius(f.dest_ward) + 2)}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g on:mousemove={(e) => showFlow(e, f, "in")} on:focus={(e) => showFlow(e, f, "in")} on:mouseleave={hideTip} on:blur={hideTip} role="img" tabindex="0" aria-label="{f.origin_ward} to {f.dest_ward}">
				<path d={a.line} fill="none" stroke="transparent" stroke-width="14" />
				<path d={a.line} fill="none" stroke={PINK} stroke-width={lw(f.units)} opacity="0.8" />
				<path d={a.head} fill={PINK} opacity="0.9" />
			</g>
		{/each}

		<!-- Scarborough ward nodes -->
		{#each scarbWards as w}
			{@const [x, y] = px(point[w.ward_name])}
			{@const o = WARD_LABEL[w.ward_name]}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g on:mousemove={(e) => showNode(e, w.ward_name)} on:focus={(e) => showNode(e, w.ward_name)} on:mouseleave={hideTip} on:blur={hideTip} role="img" tabindex="0" aria-label={w.ward_name}>
				<circle cx={x} cy={y} r={radius(w.ward_name)} fill="#fff" stroke={PINK} stroke-width="2" />
				<text x={x + o[0] * s} y={y + o[1] * s} text-anchor={o[2]} font-size={compact ? 9.5 : 10.5} class="label ward">{w.ward_name}</text>
			</g>
		{/each}

		<!-- destination wards of the outgoing flows -->
		{#each outDests as name}
			{@const [x, y] = px(point[name])}
			{@const o = OUT_LABEL[name] ?? [0, 14, "middle"]}
			<circle cx={x} cy={y} r="3" fill={OUT} opacity="0.8" />
			<text x={x + o[0] * s} y={y + o[1] * s} text-anchor={o[2]} font-size={compact ? 9 : 10} class="label dest">{name}</text>
		{/each}

		<!-- every Scarborough study venue; size shows total activity. Names appear on hover -->
		{#each [...venues].sort((a, b) => b.activity_total - a.activity_total) as v}
			{@const [x, y] = px([v.lon, v.lat])}
			{@const r = 2.6 + 3 * Math.sqrt(v.activity_total / maxVenue)}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g on:mousemove={(e) => showVenue(e, v)} on:focus={(e) => showVenue(e, v)} on:mouseleave={hideTip} on:blur={hideTip} role="img" tabindex="0" aria-label={v.venue_name}>
				<circle cx={x} cy={y} r="11" fill="transparent" />
				<path d="M0 {-r}L{r} 0L0 {r}L{-r} 0Z" transform="translate({x} {y})" fill="#191919" stroke="#fff" stroke-width="1.2" />
			</g>
		{/each}
	</svg>

	<Tip {tip} boundsWidth={cw} />
</Figure>

<style>
	svg {
		display: block;
		overflow: hidden;
		max-width: 100%;
	}
	text {
		font-family: OpenSans, sans-serif;
	}
	.label {
		paint-order: stroke;
		stroke: #fff;
		stroke-width: 3px;
		stroke-linejoin: round;
		fill: var(--brandGray90);
	}
	.dest {
		fill: var(--brandGray70);
		font-style: italic;
	}
	.venue {
		fill: var(--brandGray80);
	}
	.legend {
		display: flex;
		flex-wrap: wrap;
		gap: 4px 16px;
		margin-bottom: 8px;
		font-family: OpenSans;
		font-size: 12px;
		line-height: 16px;
		color: var(--brandGray80);
	}
	.item {
		display: inline-flex;
		align-items: center;
		gap: 6px;
	}
	g[tabindex] {
		outline: none;
	}
</style>
