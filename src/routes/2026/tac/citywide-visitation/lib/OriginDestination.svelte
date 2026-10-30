<script>
	// Figure 2: dumbbell of "residents' activity outside the ward" vs "venue activity from outside the ward"
	import { wards as rawWards, meta } from "../assets/ward_reach.json";
	import Figure from "./Figure.svelte";
	import Legend from "./Legend.svelte";
	import Tip from "./Tip.svelte";
	import { INK, GRID, OUTSIDE, VISITORS, regionOf, pct, tick, tipPos } from "./theme.js";

	let width = 720;
	let tip = null;

	// biggest gap (residents go out far more than visitors come in) at the top
	const wards = [...rawWards].sort((a, b) => b.origin_dest_gap - a.origin_dest_gap);

	$: cw = Math.max(300, width - 40);
	$: compact = cw < 560;
	$: labelW = compact ? 134 : 160;
	$: x0 = labelW + 12;
	$: bw = cw - x0 - 12;
	$: rowH = compact ? 22 : 25;
	$: top = 22;
	$: height = top + wards.length * rowH + 34;
	$: sx = (v) => x0 + v * bw;
	$: fs = compact ? 10.5 : 12;

	const showTip = (e, w) => {
		const gap = Math.round(w.origin_dest_gap * 100);
		tip = {
			...tipPos(e),
			title: w.ward_name,
			rows: [
				["Residents’ activity outside ward", pct(w.origin_outside_share), OUTSIDE],
				["Venue activity from outside", pct(w.dest_outside_share), VISITORS],
				["Gap", `${gap > 0 ? "+" : ""}${gap} pts`]
			],
			subtitle: regionOf(w.region).name,
			note: `${w.n_venues} study ${w.n_venues === 1 ? "venue" : "venues"} in this ward`
		};
	};

</script>

<Figure
	title="Wards both send residents out and draw visitors in"
	subtitle="For each ward: how much of its residents’ activity happens elsewhere versus how much of the activity at its study venues comes from other wards. Wards at the top send out far more than they draw in."
	caption="Venue-side shares rest on a small number of venues (most wards host one to three), so read individual wards as illustrations rather than rankings."
	source="Source: ward-mapped, normalized mobile-device activity at {meta.n_venues} study venues."
	bind:width
>
	<Legend
		items={[
			{ label: "Residents’ activity outside home ward", colour: OUTSIDE, shape: "circle" },
			{ label: "Venue activity from outside residents", colour: VISITORS, shape: "circle" }
		]}
	/>

	<svg width={cw} {height} viewBox="0 0 {cw} {height}" role="img" aria-label="Dumbbell chart comparing, for each ward, the share of residents' activity outside the ward and the share of venue activity from outside the ward">
		<!-- gridlines + axis -->
		{#each [0, 0.25, 0.5, 0.75, 1] as t}
			<line x1={sx(t)} x2={sx(t)} y1={top - 4} y2={top + wards.length * rowH} stroke={t === 0.5 ? INK : GRID} stroke-width={t === 0.5 ? 1.4 : 1} stroke-dasharray={t === 0.5 ? "2 3" : null} stroke-linecap="round" />
			<text x={sx(t)} y={height - 8} text-anchor={t === 0 ? "start" : t === 1 ? "end" : "middle"} class="axis-label">{tick(t)}</text>
		{/each}

		{#each wards as w, i}
			{@const y = top + i * rowH}
			{@const cy = y + rowH / 2}
			{@const o = sx(w.origin_outside_share)}
			{@const v = sx(w.dest_outside_share)}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g
				on:mousemove={(e) => showTip(e, w)}
				on:focus={(e) => showTip(e, w)}
				on:mouseleave={() => (tip = null)}
				on:blur={() => (tip = null)}
				role="img"
				tabindex="0"
				aria-label="{w.ward_name}: residents {pct(w.origin_outside_share)} outside, venues {pct(w.dest_outside_share)} from outside"
			>
				<rect x="0" {y} width={cw} height={rowH} fill="transparent" />
				<text x={labelW} y={cy + 4} text-anchor="end" font-size={fs} class="ward">{w.ward_name}</text>

				<line x1={Math.min(o, v)} x2={Math.max(o, v)} y1={cy} y2={cy} stroke="#B9BAB2" stroke-width="3" stroke-linecap="round" />
				<circle cx={o} {cy} r="5" fill={OUTSIDE} stroke="#fff" stroke-width="1.5" />
				<circle cx={v} {cy} r="5" fill={VISITORS} stroke="#fff" stroke-width="1.5" />
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
	g[tabindex]:focus-visible rect {
		stroke: var(--brandGray90);
		stroke-width: 1.5;
	}
</style>
