<script>
	// frame shared by every graphic: title + subtitle above, caption + source below.
	// `width` is bound out so charts can switch to a compact layout on narrow screens.
	export let title = "";
	export let subtitle = "";
	export let caption = "";
	export let source = "";
	export let width = 720;
</script>

<figure class="fig" bind:clientWidth={width}>
	<div class="head">
		<h3>{title}</h3>
		{#if subtitle}<p>{@html subtitle}</p>{/if}
	</div>

	<div class="body">
		<slot />
	</div>

	{#if caption || source}
		<div class="caption-container">
			<p>
				<span class="caption-text">{@html caption}</span>
				{#if source}<span class="caption-source"> {@html source}</span>{/if}
			</p>
		</div>
	{/if}
</figure>

<style>
	.fig {
		max-width: 720px;
		margin: 40px auto;
		padding: 0 20px;
		box-sizing: border-box;
	}

	.head h3 {
		font-family: TradeGothicBold;
		font-weight: normal;
		font-size: 22px;
		line-height: 26px;
		margin: 0 0 4px 0;
		color: var(--brandBlack);
	}

	.head p {
		font-family: OpenSans;
		font-size: 13px;
		line-height: 19px;
		color: var(--brandGray70);
		margin: 0 0 14px 0;
	}

	.body {
		position: relative;
	}

	@media screen and (max-width: 600px) {
		.head h3 {
			font-size: 19px;
			line-height: 23px;
		}
	}
</style>
