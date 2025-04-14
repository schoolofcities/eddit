<script>
	export let svg1080 = '';
	export let svg720 = '';
	export let svg360 = '';

	let inputSVG;
	let svgWidth = 0;

	const updateSVG = () => {
		const width = window.innerWidth;

		if (width >= 1080 && svg1080) {
			inputSVG = svg1080;
			svgWidth = 1080;
		} else if (width >= 720 && svg720) {
			inputSVG = svg720;
			svgWidth = 720;
		} else {
			inputSVG = svg360;
			svgWidth = 360;
		}
	};

	import { onMount } from 'svelte';
	onMount(() => {
		updateSVG();
		window.addEventListener('resize', updateSVG);
		return () => {
			window.removeEventListener('resize', updateSVG);
		};
	});
</script>

<style>
	.svg-container-wrapper {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: 10px;
		margin-bottom: 10px;
		height: auto;
	}

	.svg-container {
		width: var(--svg-width);
		height: auto;
	}
</style>

<div class="svg-container-wrapper">
	<div class="svg-container" style="--svg-width: {svgWidth}px;">
		{@html inputSVG}
	</div>
</div>
