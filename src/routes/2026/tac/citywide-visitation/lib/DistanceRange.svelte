<script>
	// Figure 3: typical home-to-venue distance for four kinds of activity (median dot, middle-50% band)
	import { citywide, meta } from "../assets/distance.json";
	import Figure from "./Figure.svelte";
	import { GRID, OUTSIDE, wrapLabel } from "./theme.js";

	let width = 720;

	// neutral grey for in-ward, then blues for activity across ward lines (light blue = downtown, as in the other figures)
	const colours = { within_home_ward: "#A3A49C", all_cross_ward: OUTSIDE, suburb_to_suburb: "#1E3765", suburb_to_downtown: "#6FC7EA" };
	const rows = citywide.groups;
	const maxKm = 16;

	$: cw = Math.max(300, width - 40);
	$: compact = cw < 560;
	$: labelW = compact ? 104 : 156;
	$: x0 = labelW + 14;
	$: bw = cw - x0 - 14;
	$: rowH = compact ? 46 : 52;
	$: top = 10;
	$: height = top + rows.length * rowH + 34;
	$: sx = (km) => x0 + (km / maxKm) * bw;
	$: fs = compact ? 11 : 12.5;
</script>

<Figure
	title="Crossing a ward line does not mean crossing the city"
	subtitle="Typical straight-line distance from home area to venue. The dot is the median; the band spans the middle half of activity."
	caption="Suburban means wards outside Toronto and East York; downtown means Toronto and East York. Distances are weighted by normalized activity."
	source="Source: straight-line distance from home-area (~1 km cell) centres to {meta.n_venues} study venues; not route distance or travel time."
	bind:width
>
	<svg width={cw} {height} viewBox="0 0 {cw} {height}" role="img" aria-label="Typical distance from home to venue for within-ward, all cross-ward, suburb-to-suburb and suburb-to-downtown activity">
		{#each [0, 2, 4, 6, 8, 10, 12, 14, 16] as km}
			{#if !compact || km % 4 === 0}
				<line x1={sx(km)} x2={sx(km)} y1={top} y2={top + rows.length * rowH} stroke={GRID} />
				<text x={sx(km)} y={height - 8} text-anchor="middle" class="axis-label">{km}{km === 16 ? " km" : ""}</text>
			{/if}
		{/each}

		{#each rows as g, i}
			{@const cy = top + i * rowH + rowH / 2}
			{@const lines = wrapLabel(g.label, compact ? 14 : 22)}
			{#each lines as line, li}
				<text x={labelW} y={cy + 4 + (li - (lines.length - 1) / 2) * 15} text-anchor="end" font-size={fs} class="ward">{line}</text>
			{/each}

			<rect x={sx(g.p25_km)} y={cy - 6} width={sx(g.p75_km) - sx(g.p25_km)} height="12" rx="6" fill={colours[g.key]} opacity="0.45" />
			<circle cx={sx(g.median_km)} {cy} r="8" fill={colours[g.key]} stroke="#fff" stroke-width="2" />
		{/each}
	</svg>
</Figure>

<style>
	svg {
		display: block;
		overflow: visible;
	}
	text {
		font-family: OpenSans, sans-serif;
	}
	.ward {
		fill: var(--brandGray90);
	}
	.axis-label {
		font-size: 11px;
		fill: var(--brandGray60);
	}
</style>
