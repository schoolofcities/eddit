<script>
	// Figure 1: share of each ward's residents' activity inside vs outside their home ward
	import { wards as rawWards, citywide, meta } from "../assets/ward_reach.json";
	import Figure from "./Figure.svelte";
	import Legend from "./Legend.svelte";
	import Tip from "./Tip.svelte";
	import { INK, GRID, WITHIN, OUTSIDE, regionOf, pct, tick, tipPos } from "./theme.js";

	let width = 720;
	let tip = null;

	// highest outside share at the top
	const wards = [...rawWards].sort((a, b) => b.origin_outside_share - a.origin_outside_share);
	const cityRow = {
		ward_name: "All wards (activity-weighted)",
		origin_within_share: citywide.within_share,
		origin_outside_share: citywide.outside_share
	};

	$: cw = Math.max(300, width - 40);
	$: compact = cw < 560;
	$: labelW = compact ? 134 : 160;
	$: x0 = labelW + 12;
	$: bw = cw - x0 - 6;
	$: rowH = compact ? 22 : 25;
	$: barH = rowH - 7;
	$: top = 24;
	$: cityY = top + wards.length * rowH + 20;
	$: height = cityY + rowH + 34;
	$: sx = (v) => x0 + v * bw;
	$: fs = compact ? 10.5 : 12;

	const showTip = (e, w, isCity = false) => {
		const region = isCity ? null : regionOf(w.region);
		tip = {
			...tipPos(e),
			title: w.ward_name,
			rows: [
				["Outside home ward", pct(w.origin_outside_share, 1), OUTSIDE],
				["Within home ward", pct(w.origin_within_share, 1), WITHIN]
			],
			subtitle: region ? region.name : "Share of all normalized activity"
		};
	};
</script>

<Figure
	title="Most wards send the majority of their residents’ activity elsewhere"
	subtitle="Share of residents’ activity at the study venues that happens inside versus outside their home ward. Wards are sorted by outside share."
	caption="{citywide.n_wards_majority_outside} of 25 wards send a majority of residents’ activity to venues outside the ward; citywide the figure is {pct(citywide.outside_share, 1)}."
	source="Source: ward-mapped, normalized mobile-device activity at {meta.n_venues} study venues. Normalized activity is not attendance or a count of people."
	bind:width
>
	<Legend items={[{ label: "Outside home ward", colour: OUTSIDE }, { label: "Within home ward", colour: WITHIN }]} />

	<svg width={cw} {height} viewBox="0 0 {cw} {height}" role="img" aria-label="Stacked bars of within-ward and outside-ward activity for each of Toronto's 25 wards">
		<!-- 50% reference -->
		<text x={sx(0.5)} y={top - 9} text-anchor="middle" class="axis-label">50%</text>

		{#each wards as w, i}
			{@const y = top + i * rowH}
			<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
			<g
				on:mousemove={(e) => showTip(e, w)}
				on:focus={(e) => showTip(e, w)}
				on:mouseleave={() => (tip = null)}
				on:blur={() => (tip = null)}
				role="img"
				tabindex="0"
				aria-label="{w.ward_name}: {pct(w.origin_outside_share)} outside home ward"
			>
				<rect x="0" {y} width={cw} height={rowH} fill="transparent" />
				<text x={labelW} y={y + rowH / 2 + 4} text-anchor="end" font-size={fs} class="ward">{w.ward_name}</text>

				<rect x={sx(0)} y={y + 3.5} width={w.origin_within_share * bw} height={barH} fill={WITHIN} />
				<rect x={sx(w.origin_within_share)} y={y + 3.5} width={w.origin_outside_share * bw} height={barH} fill={OUTSIDE} />

				{#if w.origin_within_share >= 0.07}
					<text x={sx(0) + 4} y={y + rowH / 2 + 4} font-size={fs - 1} class="val">{pct(w.origin_within_share)}</text>
				{/if}
				{#if w.origin_outside_share >= 0.07}
					<text x={sx(1) - 4} y={y + rowH / 2 + 4} font-size={fs - 1} text-anchor="end" class="val white">{pct(w.origin_outside_share)}</text>
				{/if}
			</g>
		{/each}

		<!-- citywide bar sits below a hairline -->
		<line x1="0" x2={cw} y1={cityY - 10} y2={cityY - 10} stroke={GRID} />
		<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
		<g
			on:mousemove={(e) => showTip(e, cityRow, true)}
			on:focus={(e) => showTip(e, cityRow, true)}
			on:mouseleave={() => (tip = null)}
			on:blur={() => (tip = null)}
			role="img"
			tabindex="0"
			aria-label="All wards: {pct(citywide.outside_share)} outside home ward"
		>
			<text x={labelW} y={cityY + rowH / 2 + 4} text-anchor="end" font-size={fs} class="ward bold">{compact ? "All wards" : "All wards (weighted)"}</text>
			<rect x={sx(0)} y={cityY + 2} width={citywide.within_share * bw} height={barH + 3} fill={WITHIN} />
			<rect x={sx(citywide.within_share)} y={cityY + 2} width={citywide.outside_share * bw} height={barH + 3} fill={OUTSIDE} />
			<text x={sx(0) + 4} y={cityY + rowH / 2 + 4} font-size={fs - 1} class="val bold">{pct(citywide.within_share)}</text>
			<text x={sx(1) - 4} y={cityY + rowH / 2 + 4} font-size={fs - 1} text-anchor="end" class="val white bold">{pct(citywide.outside_share)}</text>
		</g>

		<!-- dotted 50% line drawn over the bars -->
		<line x1={sx(0.5)} x2={sx(0.5)} y1={top - 4} y2={cityY + rowH + 4} stroke={INK} stroke-width="1.4" stroke-dasharray="2 3" stroke-linecap="round" />

		<!-- x axis -->
		{#each [0, 0.25, 0.5, 0.75, 1] as t}
			<text x={sx(t)} y={height - 8} text-anchor={t === 0 ? "start" : t === 1 ? "end" : "middle"} class="axis-label">{tick(t)}</text>
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
	.val {
		fill: var(--brandGray90);
	}
	.val.white {
		fill: #fff;
	}
	.bold {
		font-family: OpenSansBold, sans-serif;
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
