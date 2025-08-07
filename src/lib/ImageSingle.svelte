<script>
	import "../assets/global-styles.css"

	export let imageURL = '';
	export let caption = '';
	export let source = '';
	export let altText = '';
	export let maxWidth = '';
	export let link = 'Yes'; // Yes or No open link in new tab

	// adjust left-padding based on if image fits the full screen or not
	let containerWidth = 0;
	$: numericMaxWidth = parseInt(maxWidth); // remove "px"
	// $: paddingLeft = containerWidth < numericMaxWidth ? '20px' : '1px';

	// $: console.log(caption, maxWidth, paddingLeft);

</script>

<div 
	class="img-container" 
	style="max-width: {maxWidth};"
	bind:offsetWidth={containerWidth}
	>
	{#if link === 'Yes'}
		<a href={imageURL} target="_blank">
			<img src={imageURL} alt={altText} loading="lazy" />
		</a>
	{:else}
		<img src={imageURL} alt={altText} loading="lazy" />
	{/if}
	<div class="caption-container">
		<p>
			<span class="caption-text">{@html caption}</span>
			<span class="caption-source">{@html source}</span>
		</p>
	</div>
	
</div>

<style>

	.img-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		/* width: 100%; */
		margin: 0 auto;
		padding-top: 10px;
		padding-bottom: 0px;
		margin-bottom: 30px;
		padding-left: 20px;
		padding-right: 20px;
	}

	img {
		width: 100%;
		height: auto;
		max-height: 80%;
		min-height: 200px;
		display: block;
		object-fit: cover;
		object-position: center;
	}

	a {
		display: block;
		width: 100%;
	}

	a:hover {
		opacity: 0.95;
	}

	a img {
		width: 100%;
		height: auto;
		display: block;
	}



	/* .caption-container p {
		font-family: OpenSansBold;
		font-weight: normal;
		color: var(--brandGray80);
		font-size: 12px;
		line-height: 18px;
		margin-top: 2px;
		margin-bottom: 0px;
		padding-top: 0px;
		padding-right: 5px;
	}

	#image-caption :global(a)  {
		font-family: OpenSansBold;
		font-weight: normal;
		color: var(--brandGray80);
	}
	#image-caption :global(a:hover)  {
		color: var(--brandMedGreen);
	}

	#image-source {
		font-family: OpenSans;
		font-weight: normal;
		color: var(--brandGray60);
	}

	#image-source :global(a)  {
		font-family: OpenSans;
		font-weight: normal;
		color: var(--brandGray60);
	}
	#image-source :global(a:hover)  {
		color: var(--brandMedGreen);
	} */

</style>
