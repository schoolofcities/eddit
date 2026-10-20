<script>
	export let data;

	// Static redirect: <meta refresh> works without JS (and for crawlers/link unfurlers);
	// the inline script additionally carries over any query string and #hash.
	$: target = data.target;
	$: script = `<script>location.replace(${JSON.stringify(target)}+location.search+location.hash)<\/script>`;
</script>

<svelte:head>
	<title>Redirecting…</title>
	<meta name="robots" content="noindex" />
	<link rel="canonical" href={target} />
	<meta http-equiv="refresh" content={`0; url=${target}`} />
	{@html script}
</svelte:head>

<p style="font-family: sans-serif; padding: 2rem;">
	This page has moved. If you are not redirected automatically, <a href={target}>click here</a>.
</p>
