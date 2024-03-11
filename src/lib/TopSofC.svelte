<script>
	import logo from '/src/assets/top-logo-full.svg';
	import "/src/assets/global-styles.css"
</script>

<div id="bar">

</div>

<style>
	#bar {
		position: fixed;
		overflow: hidden;
   		top: 0px;
		height: 50px;
		background-color: var(--e-global-color-green);
		margin-bottom: 20px;
		border-bottom: 1px solid var(--e-global-color-darkblue);
		width: 100%;
		min-width: 200px;
		padding-left: 0px;
		padding-right: 0px;
		z-index: 15;
		opacity: 0.95;
	}

	#logo {
		margin: auto;
		max-width: 260px;
		height: 50px;
		z-index: 16;
		/* background-color: aquamarine; */
	}

	a {
		color: black;
	}
	a:hover {
		opacity: 0.7;
	}

	img {
		height: 50px;
		color: blue;
	}
	img:hover {
		height: 50px;
		opacity: 0.5;
		cursor: pointer;
	}
</style>
