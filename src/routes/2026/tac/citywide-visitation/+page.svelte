<script>

	import "../../../../assets/global-styles.css"

	import Password from "#lib/Password.svelte";
	import Title from "#lib/Title.svelte";
	import Footer from "#lib/Footer.svelte";

	let title = "Citywide Visitation"
	let subTitle = "Coming soon"

</script>


<svelte:head>

	<title>{title} | School of Cities</title>

	<meta name="description" content={subTitle} />
	<meta name="author" content="School of Cities, University of Toronto">
	<meta name="robots" content="noindex" />

</svelte:head>


<Password/>

<Title
	title={title}
	subtitle={subTitle}
/>

<main>

	<div class="text">

		<p>
			This page is under development.
		</p>

	</div>

</main>

<Footer/>
