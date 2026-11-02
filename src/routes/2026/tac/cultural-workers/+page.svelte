<script>

	import "../../../../assets/global-styles.css"

	import Password from "#lib/Password.svelte";
	import Title from "#lib/Title.svelte";
	import Footer from "#lib/Footer.svelte";

	import DraftNote from "../lib/DraftNote.svelte";
	import WorkforceScatter from "./lib/WorkforceScatter.svelte";
	import RegionalPairs from "./lib/RegionalPairs.svelte";
	import PriorityLocator from "./lib/PriorityLocator.svelte";
	import WardProfile from "./lib/WardProfile.svelte";

	let title = "Cultural Workers"
	let subTitle = "Cultural workers already live in wards with infrastructure need"

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

	<!-- ============ INTRODUCTION ============ -->

	<DraftNote label="Introduction (to write)">
		Toronto’s cultural workforce is concentrated downtown but not confined to it. Define “cultural workers” (NOC occupations, counted by where they
		live, not where they work). Toronto and East York has 32.5% of the population but 55.4%–74.4% of the cultural workforce, depending on the definition
		(64.4% for the headline measure). Workforce and infrastructure cluster together (ρ = 0.73 for workers vs. total locations; 0.80 for independent
		artists vs. TAC-funded locations). This is not a story of widespread suburban deprivation: it identifies a few wards where workforce, existing
		audiences and regional connections create strong opportunities.
	</DraftNote>

	<!-- Figure 1: workers vs locations. Opens the piece and shows why these wards stand out -->
	<WorkforceScatter />

	<!-- ============ SECTION: finding opportunities for more sustained suburban infrastructure ============ -->

	<DraftNote label="Section: finding opportunities for more sustained suburban infrastructure (to write)">
		Total location counts do not show a consistent suburban shortfall. The clearer difference is in high-frequency funded locations: Etobicoke York
		16.0% of workers vs. 13.4% of locations; North York 10.4% vs. 6.3%; Scarborough 9.1% vs. 7.9%; Toronto and East York 64.4% vs. 72.3%. Downtown’s
		share reflects its role as the centre of a citywide network; the opportunity is a sustained layer of suburban infrastructure (an anchor venue,
		affordable creation space, regular programming, or cultural uses in libraries and community centres).
	</DraftNote>

	<!-- Figure 2: regions, workforce share vs high-frequency funded location share -->
	<RegionalPairs />

	<DraftNote label="After Figure 2 (to write)">
		How the wards were identified: several transparent comparisons rather than one composite “need” score. Twelve initial tests combine three workforce
		measures (creative occupations, broader cultural workers, independent artists) with four infrastructure measures (total locations, locations per
		100,000 residents, TAC-funded locations, venues in the activity sample). Each asks whether a ward has an above-median workforce but below-median
		infrastructure, then checks rank gap and distance below the citywide trend. Willowdale 12 of 12 (all three methods); Don Valley North 8 of 12 (all
		three); Eglinton-Lawrence 12 of 12 (two methods); Don Valley West 9 of 12 (two methods).
		An indicator graphic summarizing the 12 comparisons could go here if wanted (not built yet).
	</DraftNote>

	<!-- ============ SECTION: pathways for expansion ============ -->

	<!-- ============ SECTION: wards illustrate different pathways for expansion ============ -->

	<DraftNote label="Section: four wards illustrate different pathways for expansion (to write)">
		Introduce the four wards and what each shows. Link back to Story 1: the activity data cannot identify cultural workers themselves, but it shows these
		wards are already linked to nearby audiences and institutions. Story 2 identifies where that regional participation coincides with an existing
		workforce and comparatively limited sustained infrastructure.
	</DraftNote>

	<!-- Figure 3: the four wards on a map of the city, numbered 1-4 to match the profiles below -->
	<PriorityLocator />

	<!-- 1. Don Valley North -->
	<div class="text"><h3>1. Don Valley North</h3></div>
	<DraftNote label="Don Valley North text (to write)">
		The clearest numerical shortfall. 1,892 cultural workers but only 42 locations (about 37 per 100,000 residents), including 33 TAC-funded and just 3
		funded at a high or very high frequency. Average workforce rank 15th of 25 wards vs. infrastructure rank 21st; furthest below the citywide trend.
		63% of residents’ activity occurs outside the ward, mostly elsewhere in suburban North York, at a median distance of 4.6 km. The opportunity is a
		stronger local node for an existing workforce and audience.
	</DraftNote>
	<WardProfile name="Don Valley North" />

	<!-- 2. Willowdale -->
	<div class="text"><h3>2. Willowdale</h3></div>
	<DraftNote label="Willowdale text (to write)">
		Shows what an anchor institution can accomplish. 2,234 cultural workers and 54 locations (46 per 100,000 residents), including 50 TAC-funded and 7
		high-frequency funded. Ranks around 12th on workforce but 17th on infrastructure. 94.5% of residents’ recorded activity stays within the ward,
		heavily driven by Meridian Arts Centre, which also attracts residents from surrounding wards (the leading destination for the other three wards).
		Meridian shows how one institution can provide local access and regional benefit while leaving room for a broader ecosystem of community, creation
		and public spaces.
	</DraftNote>
	<WardProfile name="Willowdale" />

	<!-- 3. Eglinton-Lawrence -->
	<div class="text"><h3>3. Eglinton-Lawrence</h3></div>
	<DraftNote label="Eglinton-Lawrence text (to write)">
		An opportunity to activate an existing base. 2,374 cultural workers and 70 locations (60 per 100,000 residents), including 58 TAC-funded but only 5
		high-frequency funded. Ranks around 11th on workforce and 15th on infrastructure. Its raw inventory is not especially small, but 74% of residents’
		activity occurs elsewhere, with Willowdale the leading destination and a median travel distance of 5.4 km. The opportunity may be less about new
		venues than about more frequent programming and stronger cultural use of existing facilities.
	</DraftNote>
	<WardProfile name="Eglinton-Lawrence" />

	<!-- 4. Don Valley West -->
	<div class="text"><h3>4. Don Valley West</h3></div>
	<DraftNote label="Don Valley West text (to write)">
		Also flagged in 9 of 12 comparisons and two of the three methods, so a close neighbour of the three main cases. 2,398 cultural workers and 72
		locations (71 per 100,000 residents), 2 of them high-frequency funded. Almost all of residents’ recorded activity occurs outside the ward, with
		Willowdale (Meridian Arts Centre) the leading destination. Text to be developed.
	</DraftNote>
	<WardProfile name="Don Valley West" />

	<!-- ============ CONCLUSION ============ -->

	<DraftNote label="Conclusion (to write)">
		Build the next layer of Toronto’s cultural network. These wards are not one uniform deficit: Don Valley North offers the clearest case for
		additional local capacity, Willowdale shows the impact of an anchor institution, Eglinton–Lawrence suggests an opportunity to strengthen and
		activate existing locations. The intervention could be a dedicated venue, affordable workspace, regular programming or a library or
		community-centre partnership, building on workers, audiences and regional connections already present.
	</DraftNote>

</main>

<Footer/>
