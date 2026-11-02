<script>
	// A one-card numerical summary of a single ward. The same four things appear for every ward, so the cards can be compared.
	import { wards as priority } from "../assets/priority_wards.json";
	import { byName, PRIORITY, fmt } from "./data.js";
	import Figure from "../../lib/Figure.svelte";
	import { WITHIN, OUTSIDE, pct } from "../../lib/theme.js";

	export let name = "";

	const HIGH = "#EBA00F"; // brandOrange: high or very-high-frequency funded locations
	const FUNDED = "#9A9B93"; // other TAC-funded locations
	const OTHER = "#E3E4DF"; // not TAC-funded

	let width = 720;

	$: w = byName[name];
	$: n = PRIORITY.indexOf(name) + 1;
	$: destinations = priority.find((d) => d.ward_name === name).leading_outside_destinations.slice(0, 3);
	$: within = 1 - w.outsideShare;
	$: share = (v) => (v < 0.005 ? "<1%" : pct(v));
	// one dot per location, funded locations first
	$: dots = [
		...Array(w.highFreq).fill(HIGH),
		...Array(w.tacFunded - w.highFreq).fill(FUNDED),
		...Array(w.locations - w.tacFunded).fill(OTHER)
	];
	$: maxShare = Math.max(...destinations.map((d) => d.share_of_all_activity));
	const COLS = 12;
	const PITCH = 12;
</script>

<Figure tight bind:width>
	<div class="card" class:narrow={width < 600}>
		<div class="head">
			<span class="badge">{n}</span>
			<div>
				<h4>{w.name}</h4>
				<p class="region">{w.region}</p>
			</div>
		</div>

		<div class="grid">
			<div class="cell">
				<div class="stats">
					<div>
						<div class="big">{fmt(w.workers)}</div>
						<div class="label">cultural workers live in the ward</div>
					</div>
					<div>
						<div class="big">{fmt(w.locations)}</div>
						<div class="label">arts locations ({fmt(w.per100k)} per 100,000 residents)</div>
					</div>
				</div>

				<svg width={COLS * PITCH} height={Math.ceil(dots.length / COLS) * PITCH + 2} role="img" aria-label="{w.locations} arts locations, {w.highFreq} of them funded at a high or very high frequency">
					{#each dots as c, i}
						<circle cx={(i % COLS) * PITCH + 5} cy={Math.floor(i / COLS) * PITCH + 6} r="4.2" fill={c} />
					{/each}
				</svg>
				<div class="dotkey">
					<span><i style="background:{HIGH}"></i>{w.highFreq} high-frequency funded</span>
					<span><i style="background:{FUNDED}"></i>{w.tacFunded - w.highFreq} other funded</span>
					<span><i style="background:{OTHER}"></i>{w.locations - w.tacFunded} not funded</span>
				</div>
			</div>

			<div class="cell">
				<div class="label head2">Where residents’ activity happens</div>
				<div class="bar">
					<span style="width:{within * 100}%; background:{WITHIN}"></span><span style="width:{w.outsideShare * 100}%; background:{OUTSIDE}"></span>
				</div>
				<div class="barlabels">
					<span>{share(within)} in the ward</span>
					<span>{share(w.outsideShare)} elsewhere</span>
				</div>

				<div class="label head2 gap">Leading destinations elsewhere</div>
				{#each destinations as d}
					<div class="dest">
						<span class="dname">{d.ward_name}</span>
						<span class="dbar"><span style="width:{(d.share_of_all_activity / maxShare) * 100}%"></span></span>
						<span class="dval">{share(d.share_of_all_activity)}</span>
					</div>
				{/each}
				<div class="note">Share of the ward’s residents’ activity</div>
			</div>
		</div>
	</div>
</Figure>

<style>
	.card {
		border: solid 1px var(--brandGray);
		border-top-right-radius: 40px;
		padding: 14px 18px 16px 18px;
		font-family: OpenSans;
		color: var(--brandGray90);
	}
	.head {
		display: flex;
		align-items: center;
		gap: 10px;
		margin-bottom: 12px;
	}
	.badge {
		flex: none;
		width: 26px;
		height: 26px;
		border-radius: 50%;
		background: var(--brandMedBlue);
		color: var(--brandWhite);
		font-family: OpenSansBold;
		font-size: 14px;
		line-height: 26px;
		text-align: center;
	}
	h4 {
		margin: 0;
		font-family: TradeGothicBold;
		font-weight: normal;
		font-size: 21px;
		line-height: 24px;
		color: var(--brandBlack);
	}
	.region {
		margin: 0;
		font-family: OpenSansItalic;
		font-size: 12px;
		line-height: 16px;
		color: var(--brandGray70);
	}
	.grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 18px 28px;
	}
	.narrow .grid {
		grid-template-columns: 1fr;
	}
	.stats {
		display: flex;
		gap: 22px;
		margin-bottom: 12px;
	}
	.big {
		font-family: TradeGothicBold;
		font-size: 32px;
		line-height: 34px;
		color: var(--brandBlack);
	}
	.label {
		font-size: 12px;
		line-height: 16px;
		color: var(--brandGray70);
		max-width: 150px;
	}
	.label.head2 {
		max-width: none;
		margin-bottom: 6px;
	}
	.label.gap {
		margin-top: 20px;
	}
	svg {
		display: block;
	}
	.dotkey {
		display: flex;
		flex-direction: column;
		gap: 2px;
		margin-top: 8px;
		font-size: 11.5px;
		line-height: 16px;
		color: var(--brandGray70);
	}
	.dotkey i {
		display: inline-block;
		width: 9px;
		height: 9px;
		border-radius: 50%;
		margin-right: 6px;
	}
	.bar {
		display: flex;
		height: 18px;
	}
	.bar span {
		display: block;
		height: 100%;
	}
	.barlabels {
		display: flex;
		justify-content: space-between;
		margin-top: 3px;
		font-size: 12px;
		color: var(--brandGray80);
	}
	.dest {
		display: grid;
		grid-template-columns: 1fr 70px 38px;
		align-items: center;
		gap: 8px;
		font-size: 12.5px;
		line-height: 22px;
	}
	.dbar {
		height: 9px;
		background: #f2f3ef;
	}
	.dbar span {
		display: block;
		height: 100%;
		background: var(--brandMedBlue);
	}
	.dval {
		text-align: right;
		color: var(--brandGray80);
	}
	.note {
		margin-top: 4px;
		font-size: 11px;
		color: var(--brandGray60);
	}
</style>
