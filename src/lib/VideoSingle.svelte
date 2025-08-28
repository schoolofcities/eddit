<script>
	import "../assets/global-styles.css"

	export let videoURL = '';
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
	<iframe
	    src={videoURL}
	    title={altText}
	    frameborder="0"
	    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
	    allowfullscreen
	 ></iframe>

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
	}


	iframe {
		width: 100%;
		height: auto;
		aspect-ratio: 16 / 9;
		border: none;
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


</style>
