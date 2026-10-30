<script>

	import "../../../../assets/global-styles.css"

	import Password from "#lib/Password.svelte";
	import Title from "#lib/Title.svelte";
	import Footer from "#lib/Footer.svelte";

	import DraftNote from "./lib/DraftNote.svelte";
	import WardSplit from "./lib/WardSplit.svelte";
	import OriginDestination from "./lib/OriginDestination.svelte";
	import DistanceRange from "./lib/DistanceRange.svelte";
	import ScarboroughDestinations from "./lib/ScarboroughDestinations.svelte";
	import FlowMap from "./lib/FlowMap.svelte";

	let title = "Citywide Visitation"
	let subTitle = "Cultural venues already serve residents across ward lines"

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
		Cultural venues already operate as a shared citywide system: 52.0% of normalized, ward-mapped activity occurs outside
		residents’ home wards and 20 of 25 wards send a majority of residents’ activity elsewhere (median ward: 77.6%). The lower
		citywide figure reflects a few high-volume venues with substantial local activity. Mention libraries and community centres
		alongside major arts institutions, and the 105 study venues vs. the 2,576-location inventory (ρ = 0.61–0.67).
		Narrative point: cultural investment is simultaneously local and citywide.
	</DraftNote>

	<!-- Figure 1: citywide reach -->
	<WardSplit />

	<!-- ============ SECTION: wards play different but interconnected roles ============ -->

	<DraftNote label="Section: wards play different but interconnected roles (to write)">
		Every ward is both an origin and a destination. Roles from the median split: 7 mutual-exchange hubs, 6 citywide
		destinations, 6 exporters, 6 primarily local wards. These describe position in the network, not success. Don Valley West
		is the two-way example: nearly all residents’ activity goes elsewhere, yet ~85% of activity at its venues comes from
		outside.
	</DraftNote>

	<!-- Figure 2: origin vs destination -->
	<OriginDestination />

	<DraftNote label="Between Figures 2 and 3 (to write)">
		Cross-ward participation is often regional rather than city-spanning. Weighted median straight-line distance: 0.3 km within
		the home ward, 6.2 km across ward lines. Suburb-to-suburb 6.6 km vs. suburb-to-downtown 11.3 km. About 46% of suburban
		residents’ outside-ward activity stays suburban (no longer shown on Figure 3, so the text has to carry it).
		Narrative point: overlapping local, regional and citywide systems; libraries and community centres as the
		distributed layer between major institutions.
	</DraftNote>

	<!-- Figure 3: distance -->
	<DistanceRange />

	<!-- ============ SECTION: Scarborough ============ -->

	<DraftNote label="Section: Scarborough as a developing suburban network (to write)">
		Southwest is downtown-oriented; North, Centre, Agincourt and Rouge Park form a more internally connected north/east cluster.
		Scarborough North: 38.3% to other Scarborough wards, 22.1% North York/Willowdale, 20.1% downtown. Internal trips are shorter
		(4.3 km vs 12.5 km and 13.5 km). Agincourt is the clearest regional destination; North → Agincourt is the strongest internal
		connection but reciprocity is only 0.09. Not driven by one venue: Malvern Library is 34.6% of Scarborough destination
		activity, yet 55.3% of the remainder still comes from other Scarborough wards. Public infrastructure (Scarborough Civic
		Centre Library, Birkdale Community Centre, Agincourt Library) alongside Woodside Square Cinemas.
	</DraftNote>

	<!-- Figure 4: Scarborough destination composition -->
	<ScarboroughDestinations />

	<!-- Figure 5: flow map. Internal flows (pink) are the six strongest; dashed grey arrows are the five largest flows leaving Scarborough -->
	<FlowMap />

	<DraftNote label="After Figure 5 (to write)">
		Where to say what the map shows: North → Agincourt is the strongest internal connection (reciprocity 0.09, so Agincourt is
		mainly a destination); Malvern Library alone is 34.6% of Scarborough destination activity, yet 55.3% of the remainder still comes
		from other Scarborough wards. The dashed arrows are the counterweight: Southwest and Centre still look downtown, and several
		wards look to Willowdale.
	</DraftNote>

	<!-- ============ CONCLUSION ============ -->

	<DraftNote label="Conclusion (to write)">
		Cultural infrastructure is shared infrastructure. Ward boundaries set political responsibility but do not contain the
		benefits of investment. Councillors can strengthen their ward’s place in a wider system: support local hubs, enable cultural
		uses in libraries and community centres, and recognize that investment in one ward benefits residents of several others.
	</DraftNote>

</main>

<Footer/>
