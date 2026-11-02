<script>
	// items: [{ label, colour, shape? }]
	// { break: true } forces the next item onto a new line.
	// shape: "circle" (dot like the plot), "ring" (empty dot with a dark edge), "outline" (empty box with a dark edge), "hatch" (diagonal stripes), "line" or the default filled swatch
	export let items = [];

	const uid = Math.random().toString(36).slice(2, 8);
</script>

<div class="legend">
	{#each items as item, i}
		{#if item.break}
			<span class="break"></span>
		{:else}
		<span class="item">
			<svg width="14" height="14" viewBox="-7 -7 14 14" aria-hidden="true">
				{#if item.shape === "circle"}
					<circle r="5" fill={item.colour} />
				{:else if item.shape === "ring"}
					<circle r="4.5" fill="#fff" stroke="#191919" stroke-width="1.8" />
				{:else if item.shape === "outline"}
					<rect x="-5.5" y="-5" width="11" height="10" fill="none" stroke="#191919" stroke-width="1.5" />
				{:else if item.shape === "line"}
					<path d="M-7 0H7" stroke={item.colour} stroke-width="2.5" stroke-linecap="round" />
				{:else if item.shape === "hatch"}
					<defs>
						<pattern id="{uid}-{i}" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
							<rect width="4" height="4" fill="#fff" />
							<rect width="1.8" height="4" fill={item.colour} />
						</pattern>
					</defs>
					<rect x="-6" y="-5" width="12" height="10" fill="url(#{uid}-{i})" stroke={item.colour} stroke-width="1" />
				{:else}
					<rect x="-6" y="-5" width="12" height="10" fill={item.colour} />
				{/if}
			</svg>
			{item.label}
		</span>
		{/if}
	{/each}
</div>

<style>
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

	.break {
		flex-basis: 100%;
		height: 0;
	}

	.item {
		display: inline-flex;
		align-items: center;
		gap: 5px;
		white-space: nowrap;
	}
</style>
