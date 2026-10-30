<script>
	// Figure 4: where residents of each Scarborough ward do their activity, by destination area
	import { wards as rawWards, meta } from "../assets/scarborough_network.json";
	import { scarborough } from "../assets/distance.json";
	import Figure from "./Figure.svelte";
	import Legend from "./Legend.svelte";
	import Tip from "./Tip.svelte";
	import { INK, WITHIN, regionOf, pct, tick, tipPos, wrapLabel } from "./theme.js";

	let width = 720;
	let tip = null;
	let active = null; // "ward|bucket" of the hovered segment

	// segment order left to right; colours follow the region colours used in Figures 1 and 2
	const buckets = [
		{ key: "same_ward", label: "Within home ward", colour: WITHIN },
		{ key: "other_scarborough", label: "Another Scarborough ward", colour: regionOf("Scarborough").colour },
		{ key: "north_york_willowdale", label: "North York", colour: regionOf("North York").colour },
		{ key: "downtown", label: "Toronto and East York (downtown)", colour: regionOf("Toronto and East York").colour },
		{ key: "elsewhere_in_toronto", label: "Etobicoke York", colour: regionOf("Etobicoke York").colour }
	];
	const median = Object.fromEntries(scarborough.by_destination.map((d) => [d.key, d.median_km]));

	// most downtown-oriented ward at the top
	const wards = [...rawWards].sort((a, b) => b.destination_share.downtown - a.destination_share.downtown);

	$: cw = Math.max(300, width - 40);
	$: compact = cw < 560;
	$: labelW = compact ? 104 : 150;
	$: x0 = labelW + 14;
	$: bw = cw - x0 - 4;
	$: rowH = compact ? 38 : 44;
	$: top = 8;
	$: height = top + wards.length * rowH + 28;
	$: sx = (v) => x0 + v * bw;
	$: fs = compact ? 11 : 12.5;

	const showTip = (e, w, b) => {
		active = `${w.ward_name}|${b.key}`;
		tip = {
			...tipPos(e),
			title: w.ward_name,
			subtitle: `Residents’ activity at venues in: ${b.label}`,
			rows: [
				["Share of residents’ activity", pct(w.destination_share[b.key], 1), b.colour],
				["Median distance (all Scarborough)", `${median[b.key].toFixed(1)} km`]
			]
		};
	};
	const hideTip = () => {
		tip = null;
		active = null;
	};
</script>

<Figure
	title="Scarborough is not one pattern: the southwest looks downtown, the north looks inward"
	subtitle="Where residents of each Scarborough ward do their activity at the study venues, by destination area. Wards are sorted from most to least downtown-oriented."
	caption="Several Scarborough wards host only one to three study venues. Toronto and East York is the downtown core; the other regions are the North York and Etobicoke York Community Council areas."
	source="Source: ward-mapped, normalized mobile-device activity at {meta.n_venues} study venues."
	bind:width
>
	<Legend items={buckets.map((b) => ({ label: b.label, colour: b.colour }))} />

	<svg width={cw} {height} viewBox="0 0 {cw} {height}" role="img" aria-label="Stacked bars showing the destinations of each Scarborough ward's residents' activity">
		{#each wards as w, i}
			{@const y = top + i * rowH}
			{@const cy = y + rowH / 2}
			{@const lines = wrapLabel(w.ward_name, compact ? 15 : 26)}
			<g role="group" aria-label={w.ward_name}>
				{#each lines as line, li}
					<text x={labelW} y={cy + 4 + (li - (lines.length - 1) / 2) * 14} text-anchor="end" font-size={fs} class="ward">{line}</text>
				{/each}

				{#each buckets as b, bi}
					{@const before = buckets.slice(0, bi).reduce((s, k) => s + w.destination_share[k.key], 0)}
					{@const v = w.destination_share[b.key]}
					<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
					<g
						on:mousemove={(e) => showTip(e, w, b)}
						on:focus={(e) => showTip(e, w, b)}
						on:mouseleave={hideTip}
						on:blur={hideTip}
						role="img"
						tabindex="0"
						aria-label="{w.ward_name} to {b.label}: {pct(v)}"
					>
						<rect
							x={sx(before)}
							y={y + 5}
							width={Math.max(0, v * bw - 1.5)}
							height={rowH - 10}
							fill={b.colour}
							stroke={active === `${w.ward_name}|${b.key}` ? INK : "none"}
							stroke-width="1.5"
						/>
					</g>
				{/each}
			</g>
		{/each}

		<!-- axis lines run over the segments so shares can be read against them -->
		{#each [0.25, 0.5, 0.75] as t}
			<line x1={sx(t)} x2={sx(t)} y1={top + 2} y2={top + wards.length * rowH - 2} stroke="#fff" stroke-width="1.2" stroke-dasharray="2 3" stroke-linecap="round" opacity="0.9" pointer-events="none" />
		{/each}
		{#each [0, 0.25, 0.5, 0.75, 1] as t}
			<text x={sx(t)} y={height - 6} text-anchor={t === 0 ? "start" : t === 1 ? "end" : "middle"} class="axis-label">{tick(t)}</text>
		{/each}
	</svg>

	<Tip {tip} boundsWidth={cw} />
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
	g[tabindex] {
		outline: none;
	}
	g[tabindex]:focus-visible rect {
		stroke: var(--brandGray90);
		stroke-width: 1.5;
	}
</style>
