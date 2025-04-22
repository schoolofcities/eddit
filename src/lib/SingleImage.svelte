<script>
	import "../assets/global-styles.css"

	export let image = '';
	export let subtitle = '';
	export let source = '';
	export let maxWidth = '';
</script>

<div class="container" style="max-width: {maxWidth}">
	<img src={image} alt="" />
	<p class="imgTitle">{subtitle}</p>
	<p class="imgSource" >{@html source}</p>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100%;
		margin: 0 auto;
		padding-top: 20px;
		padding-bottom: 20px;
	}

	img {
		width: 100%;
		height: auto;
		min-height: 500px;
		display: block;
		object-fit: cover;
		object-position: center;
	}


	p {
		text-align: center;
		padding: 5px;
		margin: 0px;
		box-sizing: border-box;
		width: 100%;
	}

	.imgTitle {
		font-family: OpenSansBold;
		font-size: 20px;
		line-height: 22px;
		padding-bottom: 10px;
	}

	.imgSource {
		font-family: OpenSans;
		color: var(--brandGray70);
		font-size: 12px;
		line-height: 18px;
		margin-top: 0px;
		padding-top: 0px;
	}
</style>
