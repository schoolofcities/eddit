<script>
	import { onMount } from 'svelte';

	export let gif1080 = '';
	export let gif720 = '';
	export let gif360 = '';
	export let alt = '';

	let src = '';
	let gifWidth = 0;
	let container;

	// Pick which GIF to load based on screen width
	function pickGifPath(width) {
		if (width >= 1080 && gif1080) return [gif1080, 1080];
		if (width >= 720 && gif720) return [gif720, 720];
		return [gif360 || gif720 || gif1080, 360];
	}

	function updateSource(width) {
		const [path, widthValue] = pickGifPath(width);
		gifWidth = widthValue;
		if (path !== src) src = path;
	}

	onMount(() => {
		let resizeHandler;

		const observer = new IntersectionObserver(([entry]) => {
			if (entry.isIntersecting) {
				updateSource(window.innerWidth);

				resizeHandler = () => updateSource(window.innerWidth);
				window.addEventListener('resize', resizeHandler);

				observer.disconnect();
			}
		});

		if (container) observer.observe(container);

		return () => {
			observer.disconnect();
			if (resizeHandler) window.removeEventListener('resize', resizeHandler);
		};
	});
</script>

<div class="gif-container-wrapper" bind:this={container}>
	{#if src}
		<img
			class="gif-container"
			{src}
			{alt}
			style="--gif-width: {gifWidth}px;"
			decoding="async"
		/>
	{/if}
</div>

<style>
	.gif-container-wrapper {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: 10px;
		margin-bottom: 10px;
		padding-left: 0px;
		padding-right: 0px;
	}

	.gif-container {
		width: var(--gif-width);
		max-width: 100%;
		height: auto;
		display: block;
	}
</style>