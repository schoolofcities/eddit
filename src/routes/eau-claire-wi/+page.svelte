<script>

	import "../../assets/global-styles.css"

	import Password from "$lib/Password.svelte";

	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";

	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/eau-claire-title.jpg"

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'footnote1 text',
		'footnote2 text'
	];


</script>



<Password/>

<Title 
	title={"Connecting the Dots: Showcasing the Benefits of Public Transportation "}
	subtitle={"A case study of Eau Claire, Wisconsin"} 
	image={titleImage}
	imageCaption={"Bus stop in Eau Claire."}
	imageSource={"Photo by _________."}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='' target='_blank'>Author Name</a>"}
			graphics={"<a href='' target='_blank'>Author Name</a> & <a href='' target='_blank'>Author Name</a>"}
			date={"August 2025"}
		/>

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/ _eau-claire-contextmap-360.svg"}
		svg720={"./eau-claire-wi/web-svg/ _eau-claire-contextmap-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	
	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_city-reference-map-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_city-reference-map-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

		<div class="callout">

			<h2>
				Callout box
			</h2>

			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
			</p>

		</div>
		
		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_ridership-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_ridership-720.svg"}
	/>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_ridership-map-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_ridership-map-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicMultiples
		svgPaths={["./eau-claire-wi/web-svg/eau-claire_novehicle-map-360.svg", "./eau-claire-wi/web-svg/eau-claire_1vehicle-map-360.svg", "./eau-claire-wi/web-svg/eau-claire_2vehicle-map-360.svg", "./eau-claire-wi/web-svg/eau-claire_3+vehicle-map-360.svg"]}
	/>
	
	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_national-ridership-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_national-ridership-720.svg"}
	/>


	<div class="text">

		<h2>
			The benefits of trees: climate impacts
		</h2>

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_transit-map-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_transit-map-720.svg"}
	/>


	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_mayo-map-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_mayo-map-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_transit-savings-chart-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_transit-savings-chart-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_emissions-savings-chart-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_emissions-savings-chart-720.svg"}
	/>

	<div class="text">

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>

	<Footnotes footnotes={footnotes} />

	<div class="details">

		<h2>Additional resources</h2>

		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>

	</div>
		
</main>

<Footer/>