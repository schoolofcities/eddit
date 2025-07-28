<script>

	// 19, 18.33

	import "../../assets/global-styles.css"

	import Title from '$lib/Title.svelte';
	import Footer from "$lib/Footer.svelte";

	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/halifax-title.jpg"

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Hello I am a footnote',
		'Hello I am a second footnote'
	];

</script>



<Title 
	title={'“Canada’s Favourite Downtown”: Encouraging investments in the core'}
	subtitle={"A case study of Halifax, Nova Scotia"} 
	image={titleImage}
/>

<main>

	<div class="text">

		<p>
			As climate change causes summer temperatures to rise, many cities are looking to trees to provide health benefits and counteract the effects of urban heat events. Yet often the tree canopy is uneven, a legacy of inequitable development patterns and zoning. To ensure that the health and climate benefits of trees can be enjoyed by all residents, cities must be intentional in how they plan, plant, and care for their urban forests.
			<Footnote id={addFootnote(fns[0])} />
		</p>

	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/halifax-contextmap-360.svg"}
		svg720={"./halifax-ns/web-svg/halifax-contextmap-720.svg"}
	/>

	<div class="text">

		<p>
			In Bridgeport, Connecticut, community organizations are working with the municipal government to plant more trees and nurture them to ensure they reach maturity. Bridgeport, a port city on the rail line between New York City and Boston, was once a hub of Connecticut’s manufacturing industry. However, like many former industrial cities, its economy declined in the late twentieth century. The city’s East Side in particular suffered the effects of suburbanization and 1960s urban renewal policies, which demolished many Black and immigrant neighbourhoods to make way for highway projects and new development, some of which never materialized. One legacy of this era is significantly lower tree cover and less access to green spaces on the East Side, where the population is more diverse, and less wealthy, than the city as a whole.
		</p>
	
	</div>

	<div class="text">

        <Footnotes footnotes={footnotes} />
		
    </div>


</main>

<Footer/>