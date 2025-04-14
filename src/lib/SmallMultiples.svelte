<script>
	export let svgs = []; // Array of SVG strings

	let layoutClass = '';

	const updateLayout = () => {
		const width = window.innerWidth;

		if (svgs.length === 2) {
			layoutClass = width < 740 ? 'stack-2' : 'row-2';
		} else if (svgs.length === 3) {
			if (width < 360 * 3) {
				layoutClass = width < 740 ? 'stack-3' : 'two-plus-one';
			} else {
				layoutClass = 'row-3';
			}
		} else if (svgs.length === 4) {
			layoutClass = width < 740 ? 'stack-4' : 'grid-2x2';
		}
	};

	import { onMount } from 'svelte';
	onMount(() => {
		updateLayout();
		window.addEventListener('resize', updateLayout);
		return () => window.removeEventListener('resize', updateLayout);
	});
</script>

<style>
	.svg-grid {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		gap: 10px;
	}

	.svg-box {
		width: 360px;
		height: auto;
	}

	/* Layout classes */
	.row-2, .row-3 {
		flex-direction: row;
	}

	.stack-2, .stack-3, .stack-4 {
		flex-direction: column;
		align-items: center;
	}

	.two-plus-one {
		display: grid;
		grid-template-columns: repeat(2, 360px);
		grid-template-rows: auto auto;
		justify-content: center;
	}

	.two-plus-one .svg-box:nth-child(3) {
		grid-column: 1 / span 2;
		justify-self: center;
	}

	.grid-2x2 {
		display: grid;
		grid-template-columns: repeat(2, 360px);
		grid-template-rows: repeat(2, auto);
		justify-content: center;
	}
</style>

<div class="svg-grid {layoutClass}">
	{#each svgs as svg}
		<div class="svg-box">
			{@html svg}
		</div>
	{/each}
</div>
