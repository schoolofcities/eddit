<script>
	// Figure 2: each region's share of cultural workers (solid) vs its share of high-frequency funded locations (hatched)
	import { DEFINITION } from "./data.js";
	import { regions } from "../assets/regions.json";
	import Figure from "../../lib/Figure.svelte";
	import Legend from "../../lib/Legend.svelte";
	import Tip from "../../lib/Tip.svelte";
	import { GRID, MUTED, regionOf, pct, tick, tipPos } from "../../lib/theme.js";

	let width = 720;
	let tip = null;

	const uid = Math.random().toString(36).slice(2, 8);
	const rows = regions.map((r) => ({
		name: r.region,
		colour: regionOf(r.region).colour,
		workers: r.workforce.labour_cultural_workers.share_of_city_total,
		funded: r.infrastructure.share_of_city_high_frequency,
		population: r.share_of_city_population,
		gap: r.gaps_pp.workforce_share_minus_high_frequency_share
	}));
	const MAX = 0.8;

	$: cw = Math.max(300, width - 40);
	$: compact = cw < 560;
	$: labelW = compact ? 100 : 150;
	$: x0 = labelW + 14;
	$: bw = cw - x0 - 8;
	$: rowH = compact ? 78 : 86;
	$: barH = compact ? 22 : 26;
	$: top = 6;
	$: height = top + rows.length * rowH + 28;
	$: sx = (v) => x0 + (v / MAX) * bw;
	$: fs = compact ? 11 : 12.5;

	const showTip = (e, r) => {
		const gap = r.gap;
		tip = {
			...tipPos(e),
			title: r.name,
			rows: [
				["Share of cultural workers", pct(r.workers, 1)],
				["Share of high-frequency funded locations", pct(r.funded, 1)],
				["Difference", `${gap > 0 ? "+" : "−"}${Math.abs(gap).toFixed(1)} pts`],
				["Share of Toronto’s population", pct(r.population, 1)]
			]
		};
	};
</script>

<Figure
	title="Suburban regions hold a bigger share of Toronto’s cultural workers than of its most frequently funded locations"
	subtitle="Each region’s share of the citywide total. Downtown’s larger share of funded locations reflects its role as the centre of the city’s cultural network."
	caption={DEFINITION}
	source="Frequently funded means a location receiving high or very high Toronto Arts Council funding frequency; it is not funding dollars. Source: custom census tabulation of cultural occupations and the broader inventory of 2,576 arts locations."
	bind:width
>
	<Legend
		items={[
			{ label: "Share of cultural workers", colour: "#727272" },
			{ label: "Share of high-frequency funded locations", colour: "#727272", shape: "hatch" }
		]}
	/>

	<svg width={cw} {height} viewBox="0 0 {cw} {height}" role="img" aria-label="Paired bars comparing each region's share of cultural workers with its share of high-frequency funded locations">
		<defs>
			{#each rows as r, i}
				<pattern id="{uid}-{i}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
					<rect width="6" height="6" fill="#fff" />
					<rect width="2.6" height="6" fill={r.colour} />
				</pattern>
			{/each}
		</defs>

		{#each [0, 0.2, 0.4, 0.6, 0.8] as t}
			<line x1={sx(t)} x2={sx(t)} y1={top} y2={top + rows.length * rowH} stroke={GRID} />
			<text x={sx(t)} y={height - 8} text-anchor={t === 0 ? "start" : "middle"} class="axis-label">{tick(t)}</text>
		{/each}

		{#each rows as r, i}
			{@const y = top + i * rowH}
			{@const y1 = y + (rowH - 2 * barH - 4) / 2}
			{@const y2 = y1 + barH + 4}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g on:mousemove={(e) => showTip(e, r)} on:focus={(e) => showTip(e, r)} on:mouseleave={() => (tip = null)} on:blur={() => (tip = null)} role="img" tabindex="0" aria-label="{r.name}: {pct(r.workers, 1)} of cultural workers, {pct(r.funded, 1)} of high-frequency funded locations">
				<rect x="0" {y} width={cw} height={rowH} fill="transparent" />
				<text x={labelW} y={y + rowH / 2 + 4} text-anchor="end" font-size={fs} class="ward">{r.name}</text>

				<!-- the shorter bar is extended in a faint tint up to the longer one, so the gap sits exactly on its own bar -->
				{#if r.workers < r.funded}
					<rect x={sx(r.workers)} y={y1} width={sx(r.funded) - sx(r.workers)} height={barH} fill={r.colour} opacity="0.2" />
				{:else}
					<rect x={sx(r.funded)} y={y2 - 0.6} width={sx(r.workers) - sx(r.funded)} height={barH + 1.2} fill={r.colour} opacity="0.2" />
				{/if}
				<rect x={sx(0)} y={y1} width={sx(r.workers) - sx(0)} height={barH} fill={r.colour} />
				<rect x={sx(0)} y={y2} width={sx(r.funded) - sx(0)} height={barH} fill="url(#{uid}-{i})" stroke={r.colour} stroke-width="1.2" />

				<text x={Math.max(sx(r.workers), sx(r.funded)) + 6} y={y1 + barH / 2 + 4} font-size={fs - 0.5} class="ward">{pct(r.workers, 1)}</text>
				<text x={Math.max(sx(r.workers), sx(r.funded)) + 6} y={y2 + barH / 2 + 4} font-size={fs - 0.5} class="ward">{pct(r.funded, 1)}</text>
			</g>
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
	g[tabindex]:focus-visible rect:first-child {
		stroke: var(--brandGray90);
		stroke-width: 1.5;
	}
</style>
