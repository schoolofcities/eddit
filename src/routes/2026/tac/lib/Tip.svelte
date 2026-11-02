<script>
	// hover tooltip. Position it relative to the nearest positioned ancestor (the figure body).
	export let tip = null; // { x, y, title, subtitle?, rows: [[label, value, colour?]], note? }
	export let boundsWidth = 720;

	$: flip = tip && tip.x > boundsWidth * 0.6;
</script>

{#if tip}
	<div class="tip" class:flip style="left: {tip.x}px; top: {tip.y}px;" role="tooltip">
		<div class="tip-title" class:solo={!tip.subtitle}>{tip.title}</div>
		{#if tip.subtitle}<div class="tip-subtitle">{tip.subtitle}</div>{/if}
		{#each tip.rows as [label, value, colour]}
			<div class="tip-row">
				{#if colour}<span class="swatch" style="background: {colour}"></span>{/if}
				<span class="tip-label">{label}</span>
				<span class="tip-value">{value}</span>
			</div>
		{/each}
		{#if tip.note}<div class="tip-note">{tip.note}</div>{/if}
	</div>
{/if}

<style>
	.tip {
		position: absolute;
		z-index: 5;
		pointer-events: none;
		transform: translate(14px, -50%);
		min-width: 190px;
		max-width: 260px;
		background: var(--brandWhite);
		border: solid 1px var(--brandGray);
		border-top-right-radius: 12px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
		padding: 8px 10px;
		font-family: OpenSans;
		font-size: 12px;
		line-height: 17px;
		color: var(--brandGray90);
	}

	.tip.flip {
		transform: translate(calc(-100% - 14px), -50%);
	}

	.tip-title {
		font-family: OpenSansBold;
	}

	.tip-subtitle {
		font-family: OpenSansItalic;
		color: var(--brandGray70);
		margin-bottom: 3px;
	}

	.tip-title.solo {
		margin-bottom: 3px;
	}

	.tip-row {
		display: flex;
		align-items: center;
		gap: 6px;
	}

	.swatch {
		width: 9px;
		height: 9px;
		flex: none;
	}

	.tip-label {
		flex: 1;
		color: var(--brandGray70);
	}

	.tip-value {
		font-family: OpenSansBold;
	}

	.tip-note {
		margin-top: 3px;
		color: var(--brandGray60);
		font-size: 11px;
		line-height: 15px;
	}
</style>
