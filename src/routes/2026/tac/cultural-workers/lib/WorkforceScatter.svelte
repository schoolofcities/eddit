<script>
	// Figure 3: cultural workers vs total locations for each ward (log scales) with the citywide trend
	import { wards, trend, PRIORITY, fmt, DEFINITION } from "./data.js";
	import Figure from "../../lib/Figure.svelte";
	import Legend from "../../lib/Legend.svelte";
	import Tip from "../../lib/Tip.svelte";
	import { INK, GRID, REGIONS, regionOf, tipPos } from "../../lib/theme.js";

	let width = 720;
	let tip = null;

	const X = [20, 300]; // locations
	const Y = [500, 10000]; // cultural workers
	const xt = [20, 50, 100, 200];
	const yt = [500, 1000, 2000, 5000, 10000];
	const predict = (loc) => Math.expm1(trend.slope * Math.log1p(loc) + trend.intercept);
	const trendPts = Array.from({ length: 40 }, (_, i) => {
		const x = Math.exp(Math.log(X[0]) + ((Math.log(X[1]) - Math.log(X[0])) * i) / 39);
		return [x, predict(x)];
	});

	// label placement (px, anchor) for the four wards examined, tuned by eye
	const LABEL = {
		"Don Valley North": [-11, 4, "end"],
		Willowdale: [-11, -8, "end"],
		"Eglinton-Lawrence": [-9, 22, "end"],
		"Don Valley West": [10, -9, "start"]
	};
	const LABEL_COMPACT = {
		"Don Valley North": [-8, 17, "end"],
		Willowdale: [-10, -9, "end"],
		"Eglinton-Lawrence": [4, 24, "start"],
		"Don Valley West": [10, -9, "start"]
	};

	$: cw = Math.max(300, width - 40);
	$: compact = cw < 560;
	$: left = 52;
	$: right = 10;
	$: top = 8;
	$: ph = compact ? 340 : 430;
	$: height = top + ph + 52;
	$: sx = (v) => left + ((Math.log(v) - Math.log(X[0])) / (Math.log(X[1]) - Math.log(X[0]))) * (cw - left - right);
	$: sy = (v) => top + ph - ((Math.log(v) - Math.log(Y[0])) / (Math.log(Y[1]) - Math.log(Y[0]))) * ph;

	const showTip = (e, w) => {
		tip = {
			...tipPos(e),
			title: w.name,
			subtitle: w.region,
			rows: [
				["Cultural workers", fmt(w.workers)],
				["Locations", fmt(w.locations)],
				["High-frequency funded locations", fmt(w.highFreq)],
				["Workers compared with trend", `${w.ratio.toFixed(1)}×`]
			]
		};
	};
</script>

<Figure
	title="Cultural workers and arts locations tend to go together, with a few suburban exceptions"
	subtitle="Each dot is a ward. Most follow the citywide pattern (the line), but the four outlined wards have more cultural workers than their number of arts locations would suggest. Hover over a dot for details."
	caption={DEFINITION}
	source="Both axes use a log scale, and the line is descriptive, not a target for how many locations a workforce should have (Spearman ρ = {trend.spearman_rho_workers_vs_locations.toFixed(2)}). Source: custom census tabulation of cultural occupations and the broader inventory of 2,576 arts locations."
	bind:width
>
	<Legend
		items={[
			...REGIONS.map((r) => ({ label: r.short, colour: r.colour, shape: "circle" })),
			{ label: "Citywide trend", colour: INK, shape: "line" },
			{ break: true },
			{ label: "Wards examined in this story", shape: "ring" }
		]}
	/>

	<svg width={cw} {height} viewBox="0 0 {cw} {height}" role="img" aria-label="Scatterplot of cultural workers against arts locations for each of Toronto's 25 wards">
		{#each yt as v}
			<line x1={left} x2={cw - right} y1={sy(v)} y2={sy(v)} stroke={GRID} />
			<text x={left - 8} y={sy(v) + 4} text-anchor="end" class="axis-label">{fmt(v)}</text>
		{/each}
		{#each xt as v}
			<line x1={sx(v)} x2={sx(v)} y1={top} y2={top + ph} stroke={GRID} />
			<text x={sx(v)} y={top + ph + 18} text-anchor="middle" class="axis-label">{fmt(v)}</text>
		{/each}
		<text x={left + (cw - left - right) / 2} y={height - 6} text-anchor="middle" class="axis-title">Arts locations in the ward</text>
		<text transform="translate(12 {top + ph / 2}) rotate(-90)" text-anchor="middle" class="axis-title">Cultural workers living in the ward</text>

		<path d={"M" + trendPts.map(([x, y]) => `${sx(x).toFixed(1)},${sy(y).toFixed(1)}`).join("L")} fill="none" stroke={INK} stroke-width="2" stroke-linecap="round" />

		{#each wards.filter((w) => !w.priority) as w}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g on:mousemove={(e) => showTip(e, w)} on:focus={(e) => showTip(e, w)} on:mouseleave={() => (tip = null)} on:blur={() => (tip = null)} role="img" tabindex="0" aria-label={w.name}>
				<circle cx={sx(w.locations)} cy={sy(w.workers)} r="11" fill="transparent" />
				<circle cx={sx(w.locations)} cy={sy(w.workers)} r="5.5" fill={regionOf(w.region).colour} stroke="#4d4d4d" stroke-opacity="0.45" stroke-width="0.8" />
			</g>
		{/each}
		{#each PRIORITY as name}
			{@const w = wards.find((d) => d.name === name)}
			{@const o = (compact ? LABEL_COMPACT : LABEL)[name]}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g on:mousemove={(e) => showTip(e, w)} on:focus={(e) => showTip(e, w)} on:mouseleave={() => (tip = null)} on:blur={() => (tip = null)} role="img" tabindex="0" aria-label={w.name}>
				<circle cx={sx(w.locations)} cy={sy(w.workers)} r="13" fill="transparent" />
				<circle cx={sx(w.locations)} cy={sy(w.workers)} r="6.5" fill={regionOf(w.region).colour} stroke={INK} stroke-width="1.8" />
				<text x={sx(w.locations) + o[0]} y={sy(w.workers) + o[1]} text-anchor={o[2]} font-size={compact ? 10.5 : 12} class="label">{w.name}</text>
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
	.axis-label {
		font-size: 11px;
		fill: var(--brandGray60);
	}
	.axis-title {
		font-size: 11.5px;
		fill: var(--brandGray70);
	}
	.label {
		fill: var(--brandGray90);
		paint-order: stroke;
		stroke: #fff;
		stroke-width: 3px;
		stroke-linejoin: round;
	}
	g[tabindex] {
		outline: none;
	}
</style>
