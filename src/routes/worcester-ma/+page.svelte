<script>

	import "../../assets/global-styles.css"

	
	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/worcester-title.jpg";

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = ['The Community Builders (TCB) is a non-profit real estate developer that manages over 30,000 mixed-income housing units in 30 metro areas across the United States.',
		'Steve Pomeroy and Maude Marquis-Bissonnette, *Non-Housing Outcomes of Affordable Housing* (Focus Consulting Inc. and Carleton University Centre for Urban Research and Education (CURE): March 2016). [URL](https://carleton.ca/cure/wp-content/uploads/Non_Housing_Outcomes_of_Affordable_Housing.pdf); Matthew A. Thomas, “On the Benefits of Affordable Housing: An Assessment of Recent Literature for Municipalities,” Table de Quartier Sud de l’Ouest-de-l’Île, 2017. [URL](https://tqsoi.org/wp-content/uploads/2018/03/On-the-benefits-of-affordable-housing.pdf); “Investments in Affordable Housing,” HomelessHub, 2017. [URL](https://homelesshub.ca/resource/place-call-home-case-increased-federal-investments-affordable-housing/); Michael Buzzelli, “Is it possible to measure the value of social housing?” Canadian Policy Research Networks: Social Housing Services Corporation, 2009. [URL](https://www.cubiq.ribg.gouv.qc.ca/notice?id=p%3A%3Ausmarcdef_0001228271&locale=fr); Canada Mortgage and Housing Corporation (CMHC), *Affordable Housing for Families: Assessing the Outcomes* (Government of Canada: 2010). [URL](https://publications.gc.ca/site/eng/9.620010/publication.html).',
		'CMHC, *Affordable Housing for Families.*',
		'Thomas, “On the Benefits of Affordable Housing.”',
		'Thomas, “On the Benefits of Affordable Housing.”',
		'Thomas, “On the Benefits of Affordable Housing”; Pomeroy and Marquis-Bissonnette, *Non-Housing Outcomes.*',
		'CMHC, *Affordable Housing for Families.*',
		'Cherise Burda and Karen Chapple, *Housing Supply Mix Strategy 1: Preservation* (TMU City Building & School of Cities: University of Toronto, 2024). [URL](https://schoolofcities.utoronto.ca/wp-content/uploads/2025/04/Housing-Mix-Strategy-1-PRESERVATION.pdf).',
		'Alex F. Schwartz, *Housing Policy in the United States* (New York: Routledge, 2021). [URL](https://doi.org/10.4324/9781003097501).',
		'National Low Income Housing Coalition, *The Gap: A Shortage of Affordable Homes* (March 2025). [URL](https://nlihc.org/gap).',
		'National Low Income Housing Coalition, *The Gap.*',
		'See, for example: Brian An et al., "Factors affecting spillover impacts of LIHTC developments: An analysis of Los Angeles," *Cityscape: A Journal of Policy Development and Research* 25, no. 2: 309–364; Ingrid Gould Ellen et al., “Does federally subsidized rental housing depress neighborhood property values?” *Journal of Policy Analysis and Management* 26, no. 2: 257–280. [URL](https://doi.org/10.1002/pam.20247); George Galster, Peter Tatian, and Kathryn Pettit, "Supportive housing and neighborhood property value externalities," *Land Economics* 80, no. 1 (2004): 33–54. [URL](https://doi.org/10.2307/3147143); Henry O. Pollakowski, David Ritchay, and Zoe Weinrobe, *Effects of Mixed-Income, Multi-Family Rental Housing Developments on Single-Family Housing Values* (Cambridge, MA: Center for Real Estate, Massachusetts Institute of Technology, 2005).',
		'Michael Buzzelli, “Is it possible to measure the value of social housing?”',
		'Corianne Payton Scally, “Beyond NIMBY and poverty deconcentration: reframing the outcomes of affordable rental housing development,” *Housing Policy Debate* 22, no. 3 (2012): 435–461. [URL](https://www.tandfonline.com/doi/full/10.1080/10511482.2012.680477#d1e1107).',
		'David Amborski and Diana Petramala, *Governments in Ontario Making Headway in Using Surplus Lands for Housing* (Centre for Urban Research and Land Development (CUR), 2019). [URL](https://www.ohba.ca/cur-report-surplus-and-underutilized-government-lands-key-to-home-ownership/).'
	];


</script>

<Password/>

<Title
	title={"Investing in affordable housing to support inclusive downtowns"}
	subtitle={"A case study of Worcester, Massachusetts"}
	image={titleImage}
	imageCaption={""}
	imageSource={"Photo by Michelle Zhang"}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='' target='_blank'>Sarah A. Smith</a> & <a href='' target='_blank'>Kathryn Exon Smith</a>"}
			graphics={"<a href='' target='_blank'>Jeff Allen</a> & <a href='' target='_blank'>Isabeaux Graham</a>"}
			date={"August 2025"}
		/>

		<p>
			The United States is facing a growing housing crisis. Rising rents, stagnant wages, and a shortage of affordable units have made it increasingly difficult for people to secure safe and stable housing. At the same time, many existing affordable housing developments — most built decades ago — are aging and in need of reinvestment to continue serving those who need them most. As cities reimagine the future of their downtowns post-COVID, they must consider preserving and supporting existing affordable housing communities along with broader investments in neighbourhoods, to ensure that their residents have safe, healthy places to live and thrive.
		</p>
		<p>
			In central Massachusetts, the city of Worcester is undergoing a period of growth and renewal, with major investments in its downtown core and a stated goal of being the country's most vibrant and livable mid-sized city. However, recent migration from Boston and elsewhere has led to rising housing costs, which has made it more difficult for existing residents to live there. This is especially true downtown, where rents have skyrocketed in recent years, causing high population turnover. These changes have underscored the crucial role that affordable housing plays in allowing residents of all income levels to live in Worcester.
		</p>

	</div>

	<GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester-contextmapV2-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester-contextmapV2-360.svg"}
	/>

	<div class="text">

		<p>
			The non-profit real estate developer <a href="https://tcbinc.org/" target="_blank">The Community Builders (TCB)</a> has operated community-centred affordable housing in Worcester for four decades, including the 400-unit Plumley Village complex in the centre of the city.<Footnote id={addFootnote(fns[0])} /> A core part of TCB’s mission is their Community Life program, which offers supportive services, including tutoring, financial planning, employment coaching, and social activities. These services are intended to help build a sense of community and support economic mobility among residents. While Plumley Village has a network of dedicated service providers and a strong culture of collaborative leadership, there is a high level of need for services, and providers are often under-resourced.
		</p>

	</div>

	<GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester-city-contextmap-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester-city-contextmap-360.svg"}
	/>

	<div class="text">

		<p>
			Maintaining a site like Plumley Village requires ongoing investment. Without sustained support, essential community services such as food pantries and youth programs could be cut. TCB is seeking support from municipal leaders for more investments in these amenities and services to support Plumley Village and its residents. In a moment of broader neighbourhood growth and revitalization, the organization is also looking to be more involved in Worcester’s downtown planning process as Plumley Village is a central residential area in the neighbourhood.
		</p>
		<p>
			This case study highlights the narrative that emerged from the collaborative work between the <a href="https://schoolofcities.github.io/eddit/" target="_blank">EDDIT data storytelling team</a> and TCB, and argues that cities should invest in maintaining and improving existing affordable housing developments, while also enhancing the surrounding environment. By integrating affordable housing into broader neighbourhood planning processes, cities can enhance the connectivity and vibrancy of their communities.
		</p>
		<h2>The benefits of affordable housing</h2>
		<p>
			There is an abundance of research that illustrates the positive health, education, and economic outcomes for families and individuals associated with affordable housing.<Footnote id={addFootnote(fns[1])} /> These studies show that individuals who move into affordable housing experience a significant reduction in stress, improvements to their mental and physical health, and better performance at school.<Footnote id={addFootnote(fns[2])} /> One key advantage of affordable housing is that it allows low-income households to spend more on essentials like food, clothing, and leisure.<Footnote id={addFootnote(fns[3])} /> This additional spending supports the local economy, especially since low- and middle-income residents are more likely to shop at nearby businesses.<Footnote id={addFootnote(fns[4])} />
		</p>
		<p>
			Affordable housing also helps to stabilize households and improve their well-being by increasing their financial stability and decreasing the risk of displacement due to rising rents.<Footnote id={addFootnote(fns[5])} /> In addition, families who move into affordable housing report being more involved and engaged in their communities.<Footnote id={addFootnote(fns[6])} /> While neighbours often resist affordable housing developments due to the perception that they will increase crime, research shows that there is no significant relationship between new affordable housing and crime rates. In fact, some research has shown that affordable housing actually increases residents’ perception of safety.<Footnote id={addFootnote(fns[7])} />
		</p>
		<p>
			Despite the positive impacts of affordable housing, there is a critical shortage of it in the United States. The federal government began investing in public housing in 1937, funding local governments to build and manage housing. Over the last 75 years, the government has shifted to mainly subsidizing private developers to build low-income housing.<Footnote id={addFootnote(fns[8])} /> As a result, the amount of new affordable housing has decreased significantly, creating a growing gap between supply and demand. For example, nearly half of all renter households in the United States spend over 30 percent of their income on housing, with over a quarter spending more than 50 percent.<Footnote id={addFootnote(fns[9])} />
		</p>
	</div>

	<!-- <GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_1in4stat-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_1in4stat-360.svg"}
	/> -->

	<div class="text">

		<p>
			There is a significant shortage of affordable homes for extremely low-income households (those earning at or below either the federal poverty level or 30 percent of the area median income), equating to a national shortage of over 7 million affordable homes across the country.<Footnote id={addFootnote(fns[10])} />
		</p>
	</div>

	<!-- <GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_35affordable-stat-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_35affordable-stat-360.svg"}
	/> -->

	<div class="text">

		<p>
			However, building new affordable housing projects is expensive, and there's a <a href="https://apps.urban.org/features/cost-of-affordable-housing/" target="_blank">significant gap</a> between the rent tenants can pay and the revenue needed to cover the cost of construction and maintenance. Without sufficient government subsidies, creating and sustaining affordable housing is often not feasible. While one part of the long-term solution to the housing crisis is to build more homes and increase the supply of affordable units, another important and immediate part is to preserve and continue to invest in the affordable housing stock that already exists, and support these communities.
		</p>
		<h2>Comparing geographies to understand impact</h2>
		<p>
			TCB wanted to build support for their work and explore the spillover impact of Plumley Village on the broader neighbourhood and city. Subsidized housing, for example, has been found to increase property values and tax revenues in surrounding neighbourhoods, as a result of the removal of blight and an influx of population.<Footnote id={addFootnote(fns[11])} /> These findings suggest that strategically targeted, place-based housing subsidies can revitalize neighbourhoods while also delivering affordable housing. While TCB initially wanted to replicate these kinds of studies by exploring Plumley Village’s impact on the surrounding area, this kind of analysis is often done over a period of several years, and requires more complex econometric methods and data than were within the scope of this project.<Footnote id={addFootnote(fns[12])} /> An evaluation of the relationship between Plumley Village and the surrounding neighbourhood would also need to account for many other factors, such as the housing market, the local economy, and income and racial diversity.<Footnote id={addFootnote(fns[13])} />
		</p>
		<p>
			Instead, the EDDIT team took a simpler approach and compared data for the tract that contains downtown Worcester with the block group that contains Plumley Village to highlight the value of affordable housing and supportive services to these communities. These data are from data collected by TCB, the <a href="https://experience.arcgis.com/experience/22c7182a162d45788dd52a2362f8ed65" target="_blank">CDC’s PLACES</a> national health data portal, and the U.S. Census Bureau.
		</p>
		<p>
			Plumley Village is located in central Worcester, directly adjacent to the city’s main commercial and business district, and is considered part of downtown in the city’s <a href="https://www.worcesterma.gov/planning-regulatory/document-center/now-next-final-plan.pdf" target="_blank">2024 citywide plan</a>. Residents of Plumley Village account for approximately a quarter of downtown’s total residential population. Any public or private investments in Plumley Village — whether in housing, transportation, public space, or social infrastructure — directly impact the vitality and success of the downtown as a whole. Similarly, changes in the downtown’s economic activity, cultural programming, or urban planning have immediate and tangible effects on the daily lives of Plumley Village residents. However, despite their interconnectedness, Plumley Village is located in a different census tract than the one that includes the downtown area.
		</p>
	</div>

	<GraphicSingle
		svg360={"./worcester-ma/web-svg/worcester_map_residential.svg"}
	/>

	<div class="text">
		<p>
			Assessing income-to-poverty ratios across geographies can give a better understanding of the need for affordable housing in downtown neighbourhoods. In many American cities, suburbanization, racially-segregated redevelopment, and renewal projects have led to disproportionately high poverty rates in downtown areas. Worcester exemplifies this trend, with a significantly higher percentage of residents downtown living below the poverty line than in the city as a whole, as defined by the American Community Survey’s income-to-poverty ratio metric. Plumley Village has an even higher percentage of residents living in poverty. Downtown Worcester, including Plumely Village, would benefit from investments in existing affordable housing, and arguably even more affordable housing is needed.
		</p>
	</div>

	<GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_poverty-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_poverty-360.svg"}
	/>

	<div class="text">

		<p>
			In Plumley Village, many wraparound services are offered on site, including the Village Grocery Store, a food pantry with access to the Supplemental Nutrition Program for Women, Infants, and Children (WIC), Boys & Girls Club, homework and computer centre, and tax preparation services. These kinds of holistic interventions have been proven to benefit families’ financial, social, emotional, and physical well-being, while also helping to create a sense of community and engagement among residents. Supportive services have contributed to positive outcomes for residents, including a higher rate of access to primary care and higher rates of health insurance coverage than other residents in the downtown core, and equivalent self-reported health metrics. Though essential to the well-being of Plumley Village’s residents, services require sustained funding in order to keep supporting residents over the long term. 
		</p>

	</div>

	<GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_health-indicators-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_health-indicators-360.svg"}
	/>

	<div class="text">
		<h2>Planning for growth and improvement</h2>
		<p>
			Focusing on preserving affordable housing can be a key strategy in addressing long-term affordability challenges. This approach helps to maintain the availability of affordable housing and prevent further losses due to redevelopment and rising rents.<Footnote id={addFootnote(fns[14])} /> This can be coupled with investments that advance a “whole-community” approach to affordable housing preservation that involves additional investments in residential services and amenities in the surrounding neighbourhood.
		</p>
		<p>
			Many cities have a surplus of public and private land used for parking that could be converted to neighbourhood amenities. In the past decade, several movements have emerged to challenge the amount of land dedicated to parking in urban areas, with advocates calling for these spaces to be repurposed. In particular, there is increasing momentum to transform parking areas for affordable housing, mixed-use development, and community infrastructure such as parks, plazas, and residential services. These changes could not only alleviate the housing crisis, but also promote a more vibrant and inclusive downtown core.
		</p>
		<p>
			The map below, created using <a href="https://www.openstreetmap.org/#map=5/38.01/-95.84" target="_blank">OpenStreetMap (OSM)</a> data, shows how much land in downtown Worcester is dedicated to parking versus community amenities such as <a href="https://schoolofcities.github.io/eddit/greensboro-nc" target="_blank">grocery stores</a> or public parks. Redeveloping even a fraction of these parcels could unlock significant opportunities for supporting local services and building shared amenities that improve quality of life for all downtown residents.
		</p>

	</div>

	<GraphicMultiples
		svgPaths={["./worcester-ma/web-svg/worcester_map_parkinglots.svg","./worcester-ma/web-svg/worcester_map_greenspaces-grocery.svg"]}
	/>

	<div class="text">

		<h2>Prioritizing affordable housing in downtown recovery</h2>
		<p>
			The COVID-19 pandemic caused an exodus of workers from urban centres, and many cities re-evaluated the role their downtowns should play. The dramatic shift in the flow of people in downtowns gave rise to a moment of reflection, sparking demand for change across the country. This has created a unique opportunity to prioritize investments in affordable housing as a key strategy for urban revitalization. Integrating affordable housing construction and preservation into community development and neighbourhood planning processes can help make cities more inclusive, resilient, and equitable. Preserving affordable housing should also be accompanied by investments in wraparound services and amenities that support residents’ health, education, and economic stability. This case study has used data to showcase the value of investing in affordable housing and neighbourhood amenities, and possible sites to expand them in downtown Worcester. A holistic, data-informed approach that connects housing with supportive infrastructure offers a path forward for building stronger, more connected communities.
		</p>
	</div>

	<Footnotes footnotes={footnotes} />

	<div class="details">

		<h2>Additional resources</h2>

		<p>
			<a href="https://experience.arcgis.com/experience/22c7182a162d45788dd52a2362f8ed65" target="_blank">CDC's Places</a>
			<br><br>
			<a href="https://downtownrecovery.com/" target="_blank">Downtown Recovery</a>
			<br><br>
			<a href="https://www.openstreetmap.org/#map=5/38.01/-95.84" target="_blank">OpenStreetMap (OSM)</a>
			<br><br>
			<a href="https://apps.urban.org/features/cost-of-affordable-housing/" target="_blank">The cost of affordable housing: Does it pencil out?</a>
			<br><br>
			<a href="https://tcbinc.org/" target="_blank">The Community Builders, Inc.</a>
			<br><br>
			<a href="https://www.worcesterma.gov/planning-regulatory/document-center/now-next-final-plan.pdf" target="_blank">Worcester citywide plan</a>
		</p>

	</div>

	<!-- <GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_median-age-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_median-age-360.svg"}
	/>

	<GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_family-households-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_family-households-360.svg"}
	/>
	

	<GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_SNAP-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_SNAP-360.svg"}
	/>


	<GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_race-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_race-360.svg"}
	/>

	<GraphicSingle
		svg720={"./worcester-ma/web-svg/worcester_edu-attainment-720.svg"}
		svg360={"./worcester-ma/web-svg/worcester_edu-attainment-360.svg"}
	/> -->


</main>

<Footer/>