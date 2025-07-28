<script>

	// 19, 18.33

	import "../../assets/global-styles.css"

	import Title from '$lib/Title.svelte';
	import Footer from "$lib/Footer.svelte";
	import Password from "$lib/Password.svelte";

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



<Password/>

<Title 
	title={'“Canada’s Favourite Downtown”: Encouraging investments in the core'}
	subtitle={"A case study of Halifax, Nova Scotia"} 
	image={titleImage}
/>

<main>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/halifax-contextmap-360.svg"}
		svg720={"./halifax-ns/web-svg/halifax-contextmap-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>
	
	</div>

	<GraphicMultiples
		svgPaths={["./halifax-ns/web-svg/Halifax_HRM-population-360.svg","./halifax-ns/web-svg/Halifax_DT-population-360.svg" ]}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/Halifax_downtown-map-360.svg"}
		svg720={"./halifax-ns/web-svg/Halifax_downtown-map-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/Halifax_property-assess-360.svg"}
		svg720={"./halifax-ns/web-svg/Halifax_property-assess-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/halifax_canada-recovery-360.svg"}
		svg720={"./halifax-ns/web-svg/halifax_canada-recovery-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/Halifax_monthly-stops-heatmap-360.svg"}
		svg720={"./halifax-ns/web-svg/Halifax_monthly-stops-heatmap-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/Halifax_visits-downtown-360.svg"}
		svg720={"./halifax-ns/web-svg/Halifax_visits-downtown-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>
	
	</div>

	<div class="text">

        <Footnotes footnotes={footnotes} />
		
    </div>


</main>

<Footer/>