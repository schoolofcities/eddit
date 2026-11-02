<script>
	// placeholder for article copy that has not been written yet. Delete these as the text goes in.
	export let label = "Draft note";
</script>

<div class="text">
	<aside>
		<span class="label">{label}</span>
		<slot />
	</aside>
</div>

<style>
	aside {
		margin: 24px 0;
		padding: 10px 14px;
		border: dashed 1px var(--brandGray50);
		background: #fafaf7;
		font-family: OpenSans;
		font-size: 13px;
		line-height: 19px;
		color: var(--brandGray70);
	}
	.label {
		display: block;
		font-family: OpenSansBold;
		font-size: 11px;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--brandGray60);
		margin-bottom: 2px;
	}
</style>
