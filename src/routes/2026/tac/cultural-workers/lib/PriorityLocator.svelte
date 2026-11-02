<script>
	// Figure 3: the four wards examined, numbered on a map of all 25 wards. The numbers are reused on each ward's profile below.
	import { wards as geo } from "../assets/ward_geo.json";
	import { PRIORITY, DEFINITION } from "./data.js";
	import { projector, ringsPath } from "./mapUtils.js";
	import Figure from "../../lib/Figure.svelte";
	import { OUTSIDE } from "../../lib/theme.js";

	let width = 720;

	const WIN = [-79.645, 43.575, -79.11, 43.865];
	const NEUTRAL = "#E9EAE4";
	// nudge of each number from the ward's interior point (px at full width), so it sits in the visual centre of the ward
	const NUDGE = { "Eglinton-Lawrence": [6, 10] };

	$: cw = Math.max(280, Math.min(width - 40, 560));
	$: s = Math.min(1, cw / 560);
	$: ({ px, height } = projector(WIN, cw));
</script>

<Figure
	title="Four neighbouring wards"
	subtitle="The wards examined in this story sit side by side in the north-central part of the city, outside the downtown core."
	caption={DEFINITION}
	source="The profiles below report activity from mobile-device data, which covers all residents of a ward, not only cultural workers. Source: ward boundaries from the City of Toronto; custom census tabulation of cultural occupations; the broader inventory of 2,576 arts locations; mobile-device activity at 105 study venues."
	bind:width
>
	<svg width={cw} {height} viewBox="0 0 {cw} {height}" role="img" aria-label="Map of Toronto's wards with Don Valley North, Willowdale, Eglinton-Lawrence and Don Valley West numbered one to four">
		{#each geo as w}
			<path d={ringsPath(w.rings, px)} fill={PRIORITY.includes(w.name) ? OUTSIDE : NEUTRAL} stroke="#fff" stroke-width="1.2" stroke-linejoin="round" />
		{/each}
		{#each PRIORITY as name, n}
			{@const w = geo.find((d) => d.name === name)}
			{@const [x, y] = px(w.point)}
			{@const o = NUDGE[name] || [0, 0]}
			<circle cx={x + o[0] * s} cy={y + o[1] * s} r={10 * Math.max(0.8, s)} fill="#fff" />
			<text x={x + o[0] * s} y={y + o[1] * s + 4.5 * Math.max(0.8, s)} text-anchor="middle" font-size={13 * Math.max(0.8, s)} class="num">{n + 1}</text>
		{/each}
	</svg>

	<ol class="key">
		{#each PRIORITY as name, n}
			<li><span class="badge">{n + 1}</span>{name}</li>
		{/each}
	</ol>
</Figure>

<style>
	svg {
		display: block;
		margin: 0 auto;
		max-width: 100%;
	}
	.num {
		font-family: OpenSansBold, sans-serif;
		fill: var(--brandMedBlue);
	}
	.key {
		list-style: none;
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		gap: 6px 20px;
		margin: 12px 0 10px 0;
		padding: 0;
		font-family: OpenSans;
		font-size: 13px;
		color: var(--brandGray90);
	}
	.key li {
		display: inline-flex;
		align-items: center;
		gap: 7px;
	}
	.badge {
		width: 20px;
		height: 20px;
		border-radius: 50%;
		background: var(--brandMedBlue);
		color: var(--brandWhite);
		font-family: OpenSansBold;
		font-size: 12px;
		line-height: 20px;
		text-align: center;
	}
</style>
