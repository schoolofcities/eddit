<script>
	// items: [{ label, colour, shape? }]. shape "circle" draws a dot like the plot; default is a filled swatch.
	export let items = [];
</script>

<div class="legend">
	{#each items as item}
		<span class="item">
			<svg width="14" height="14" viewBox="-7 -7 14 14" aria-hidden="true">
				{#if item.shape === "circle"}
					<circle r="5" fill={item.colour} />
				{:else}
					<rect x="-6" y="-5" width="12" height="10" fill={item.colour} />
				{/if}
			</svg>
			{item.label}
		</span>
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

	.item {
		display: inline-flex;
		align-items: center;
		gap: 5px;
		white-space: nowrap;
	}
</style>
