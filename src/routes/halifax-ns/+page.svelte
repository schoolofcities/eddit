<script>

	// 19, 18.33

	import "../../assets/global-styles.css"

	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/halifax-title.jpg"
	import lunchImage from "./assets/lunchtime.jpg"
	import placemImage from "./assets/placemaking.jpg"
	import waterfrontImage from "./assets/waterfront.jpg"

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'David Downey and Cathy Lin, “The Evolution of Business Improvement Districts: From Place Management to Place Leadership,” *Journal of Urban Regeneration & Renewal* 18, no. 4 (2025): 322–35.',
		'Statistics Canada (table), Census Profile, 2021 Census of Population, Statistics Canada Catalogue no. 98-316-X2021001 (Ottawa) Released November 15, 2023 , (accessed August 8, 2025),  [URL](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E); Nova Scotia Department of Finance, GDP by Census Metropolitan Area 2021 (2024), [URL](https://novascotia.ca/finance/statistics/news.asp?id=20491).',
		'Halifax Partnership, “Halifax People - Demographics, Population and Education,” Halifax Partnership, accessed August 8, 2025, [URL](https://halifaxpartnership.com/research-strategy/halifax-index/people/).',
		'Halifax Partnership, “Halifax People.”',
		'Eugenie L. Birch, “Who Lives Downtown?,” in *Redefining Urban and Suburban America: Evidence from Census 2000*, ed. Alan Berube et al. (Brookings Institution Press, 2007).',
		'Canadian Urban Institute, *The Value of Investing in Canadian Downtowns* (2012), [URL](https://canurb.org/wp-content/uploads/120523_The-Value-of-Investing-in-Canadian-Downtowns-compressed.pdf).',
		'Canadian Urban Institute, *The Case for the Core* (2021), [URL](https://canurb.org/publications/case-for-the-core/); Donovan D. Rypkema, “The Importance of Downtown in the 21st Century,” *Journal of the American Planning Association* (Chicago) 69, no. 1 (2003): 9–15, [URL](https://doi.org/10.1080/01944360308976290).',
		'Gilles Duranton and Diego Puga, “The Growth of Cities,” SSRN Scholarly Paper 2309234, Rochester, NY, August 1, 2013, [URL](https://papers.ssrn.com/abstract=2309234).',
		'Downtown Halifax Business Commission, *State of the Downtown Report 2025* (2025), [URL](https://issuu.com/downtownhalifax/docs/sotd_2025_digital_spreads).',
		'Tracy Hadden Loh and Hanna Love, “Breaking the ‘Urban Doom Loop’: The Future of Downtowns Is Shared Prosperity,” *Brookings*, March 23, 2023, [URL](https://www.brookings.edu/articles/breaking-the-urban-doom-loop-the-future-of-downtowns-is-shared-prosperity/).',
		'Canadian Urban Institute, *The Case for the Core*.',
		'Gary Sands et al., “Planning for Post-Pandemic Downtowns of Mid-Size Urban Areas,” *Planning, Practice & Research* (Abingdon) 37, no. 3 (2022): 393–405, [URL](https://doi.org/10.1080/02697459.2021.2016200).',
		'Karen Chapple et al., *The Death of Downtown? Pandemic Recovery Trajectories across 62 North American Cities* (Research Brief) (School of Cities, University of Toronto, 2022).',
		'Fran H. Norris et al., “Community Resilience as a Metaphor, Theory, Set of Capacities, and Strategy for Disaster Readiness,” *American Journal of Community Psychology* (Boston) 41, nos. 1–2 (2008): 127–50, [URL](https://doi.org/10.1007/s10464-007-9156-6).',
		'Halifax Partnership, “Halifax Economy – Growth, Innovation, and Confidence,” Halifax Partnership, accessed August 8, 2025, [URL](https://halifaxpartnership.com/research-strategy/halifax-index/economy/).',
		'Arpit Gupta et al., “Work From Home and the Office Real Estate Apocalypse,” Working Paper 30526, Working Paper Series (National Bureau of Economic Research, September 2022), [URL](https://doi.org/10.3386/w30526).',
		'Aggregated mobility data are provided by Cuebiq, a location intelligence platform. Data are collected from anonymized users who have opted in to provide access to their location data anonymously, through a CCPA- and GDPR-compliant framework. Through its Social Impact program, Cuebiq provides mobility insights for academic research and humanitarian initiatives. The Cuebiq responsible data sharing framework enables research partners to query anonymized and privacy enhanced data, by providing access to an auditable, on-premise Data Cleanroom environment. All final outputs provided to partners are aggregated in order to preserve privacy.',
		'Haley Ryan, “Halifax Remains ‘Canadian Comeback City’ for Downtown Activity,” *CBC News*, February 26, 2025, [URL](https://www.cbc.ca/news/canada/nova-scotia/halifax-best-downtown-recovery-activity-canada-pandemic-covid-19-1.7467172); Karen Chapple et al., “Downtown Recovery Rankings,” October 16, 2023, [URL](https://downtownrecovery.com/).',
		'Tristan Cleveland, “How Halifax Built the Most Vibrant Waterfront in Canada: Decades of Small Changes,” *Happy Cities*, October 26, 2023, [URL](https://happycities.com/blog/halifax-waterfront-power-of-placemaking).',
		'Downtown Halifax Business Commission, “Downtown Halifax’s Art Tour (Self-Guided),” [URL](https://www.google.com/maps/d/viewer?mid=1XuL-8aX9Wto1Nix3AWYqj9wwVditZjg).',
		'Build Nova Scotia, *The Story of Halifax Waterfront*, May 30, 2023, [URL](https://buildns.ca/archive-pages/success-stories/the-story-of-halifax-waterfront/).'
	];

</script>



<Password/>

<Title 
	title={'Becoming “Canada’s Favourite Downtown”: Encouraging investments in the core'}
	subtitle={"A case study of Halifax, Nova Scotia"} 
	image={titleImage}
	imageCaption={"Halifax Waterfront."}
	imageSource={"Photo by Kyle Miller."}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='' target='_blank'>Kathryn Exon Smith</a> & <a href='' target='_blank'>Sarah A. Smith</a>"}
			graphics={"<a href='' target='_blank'>Isabeaux Graham</a> & <a href='' target='_blank'>Jeff Allen</a>"}
			date={"August 2025"}
		/>

		<p>
			Halifax, Nova Scotia has a fast-growing downtown population, but lacks the housing, infrastructure, and services to support this growth over the long term. For many years, the municipal and regional government has invested in growing specific sectors of the economy, without focusing on the downtown as a unique site of culture and economic growth. The <a href="https://downtownhalifax.ca/" target="_blank">Downtown Halifax Business Commission</a> (DHBC) is looking to change this with their <a href="https://downtownhalifax.ca/vision2030" target="_blank">Downtown Halifax Vision 2030 plan</a> (Vision 2030), which calls for increased investment to make the downtown a place where Haligonians of all kinds can live, work, and play. This investment could also build momentum for a stronger and more connected community overall.
		</p>

	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/halifax-contextmap-360.svg"}
		svg720={"./halifax-ns/web-svg/halifax-contextmap-720.svg"}
	/>

	<div class="text">

		<p>
			The aspiration behind Vision 2030 is for Halifax to become “Canada’s favourite downtown.” To that end, the plan includes goals to transform downtown into both a residential neighbourhood and a popular destination for tourists and locals alike, with a revitalized harbourfront, new cultural and entertainment amenities, more housing, better parks, and a multi-modal transportation plan that encourages active and sustainable ways of getting around. The DHBC came to the <a href="https://schoolofcities.github.io/eddit/" target="_blank">EDDIT data storytelling team</a> with the goal of shaping the public conversation about the future of the downtown core. They also wanted to bring critical stakeholders on board with their vision, including residents, the development community, and elected officials at the municipal, regional, and provincial levels.
		</p>

		<p>
			This case study demonstrates how data can be used to craft a compelling narrative that supports investment in local businesses, public infrastructure, and cultural amenities downtown. It addresses common concerns about downtown viability by highlighting the continued importance of city centres as dynamic hubs of regional growth, economic activity, and cultural relevance.
		</p>

		<div class="callout">

			<h2>Commercial sector advocacy and engagement</h2>

			<p>
				The Downtown Halifax Business Commission was established in 1987 as a business improvement district (BID) and today represents over 1,600 businesses in the urban core. All businesses within its boundaries vote on and pay a mandatory levy which the BID holds and uses for advocacy, marketing, communications, and other projects that serve member organizations.
			</p>

			<p>
				As non-profits with a large member base, BIDs can play an important role in advancing a vision that benefits not just their members, but the city as a whole.<Footnote id={addFootnote(fns[0])} /> When creating Vision 2030, the DHBC conducted extensive consultation with the public in addition to its own businesses, ultimately honing in on four priority areas: making downtown a place for everyone to live and play, creating an active harbourfront that is accessible year-round, attracting visitors to downtown, and planning for transit connectivity. The plan’s timeline for implementation (2030) is deliberately short, with the goal of creating a sense of urgency, momentum, and focus. The plan uses rapid implementation as a strategy to achieve early wins at a large enough scale for the community to see the results. 
			</p>

			<p>
				BIDs play an important role in local planning efforts, but their scope is limited, and they must form strong partnerships to be successful. For the bold aims of Vision 2030 to be achieved, the DHBC knew they needed to find other local champions to support and implement its components, particularly the city’s elected representatives. To do this, they needed to demonstrate how downtown is the key to unlocking regional prosperity and quality of life improvements.
			</p>

		</div>

		<h2>Capitalizing on a period of rapid change</h2>

		<p>
			Halifax is the capital of the province of Nova Scotia and has long been an economic hub and a destination for tourism and education in Atlantic Canada. At just over half a million people, the city is home to 46 percent of the province’s population and 58 percent of its GDP.<Footnote id={addFootnote(fns[1])} />
		</p>

		<p>
			It is also one of Canada’s fastest-growing urban areas. Since the COVID-19 pandemic, the city has seen unprecedented and explosive population growth, fuelled by both interprovincial migration and international immigration. Halifax added over 50,000 residents between 2020 and 2024, increasing the city’s population by 10 percent.<Footnote id={addFootnote(fns[2])} /> Many of the city’s newcomers are looking to make a change in lifestyle, and benefit from the region’s relatively low housing costs compared to other cities in Canada.
		</p>

		<p>
			These changes come after decades of population decline, the result of significant youth outmigration and an aging population, which led to a prolonged period of economic stagnation in the late 20th century. The more recent arrivals tend to be younger, with over half of new residents in 2022 being between the ages of 15 and 29.<Footnote id={addFootnote(fns[3])} /> As is common in cities experiencing rapid growth, this influx of population is putting pressure on existing housing, healthcare, and transportation infrastructure.
		</p>
	
	</div>

	<GraphicMultiples
		svgPaths={["./halifax-ns/web-svg/Halifax_HRM-population-360.svg","./halifax-ns/web-svg/Halifax_DT-population-360.svg" ]}
	/>

	<div class="text">

		<p>
			The region has also historically grown outward rather than upward, including through the amalgamation of the city of Halifax with the neighbouring municipalities of Dartmouth, Bedford, and Halifax County in 1996. The Halifax Regional Municipality is now one of the largest municipalities in Canada by area. Relative to its size, Halifax has a small downtown, and many of its residents — and voters — live in rural or suburban environments. As a result of competing economic priorities, there has been less regional and provincial investment in downtown development, with little urgency placed on revitalizing the urban core.
		</p>

		<p>
			The municipality’s sudden population boom is both a challenge and an opportunity. Advocating for investment downtown requires highlighting its existing importance in the region and demonstrating the potential it has for the future. The right investments in the economy, infrastructure, and cultural amenities can set the city up for greater success in the long run, even after the pace of growth slows. Downtown revitalization can make the city more resilient to future shocks in housing, migration, and employment by being the engine that drives growth in infrastructure, transportation, and amenities throughout the region.
		</p>	
	</div>

	
	<ImageSingle
		imageURL={lunchImage}
		caption='Lunchtime at the Halifax harbourfront.'
		source="Image credit: Kyle Miller"
		altText="Photograph of the Halifax harbourfront"
		maxWidth="{680}px"
		link="Yes"
	/>

	<div class="text">

		<h2>Downtowns play a key role in urban growth</h2>

		<p>
			Downtowns are focal points for cultural, civic, and commercial activity.<Footnote id={addFootnote(fns[4])} /> Cities often grow out from their historic centres, and despite sprawling, car-oriented development in the late 20th century, downtowns remain the central point of convergence for transportation networks and economic activity. They are often home to core public and private anchor institutions, such as universities, hospitals, major churches, and civic buildings.<Footnote id={addFootnote(fns[5])} />
		</p>

		<p>
			Beyond physical infrastructure, downtowns also host many of the intangible social networks and civic infrastructures that hold cities together. They are important gathering spots for protest and celebration and sites of public art and culture.<Footnote id={addFootnote(fns[6])} /> By attracting people from the city, region, and beyond, they create agglomerations that foster innovation and spur growth, which in turn helps the entire region to grow.<Footnote id={addFootnote(fns[7])} />
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/Halifax_downtown-map-360.svg"}
		svg720={"./halifax-ns/web-svg/Halifax_downtown-map-720.svg"}
	/>

	<div class="text">

		<p>
			This concept can be illustrated in the outsized impact of downtown on regional sales and tax assessments. Though Halifax’s downtown covers only 0.02 percent of the region’s land mass, the area’s businesses contribute nearly 13 percent of overall property taxes.<Footnote id={addFootnote(fns[8])} /> Investments in the urban core have the potential for disproportionate economic effects, as the city benefits from the innovation and growth that comes from density.<Footnote id={addFootnote(fns[9])} />
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/Halifax_property-assess-360.svg"}
		svg720={"./halifax-ns/web-svg/Halifax_property-assess-720.svg"}
	/>

	<div class="text">

		<h2>Downtowns after the pandemic</h2>

		<p>
			However, downtowns' reliance on connection and proximity contributed to the challenges of many downtown areas during the pandemic. City centres — and the businesses within them — experienced the greatest declines in activity. The pandemic also revealed disparities in access to green spaces and high housing costs in urban cores.<Footnote id={addFootnote(fns[10])} /> Downtowns have recovered from the pandemic more slowly and unevenly than cities as a whole, as many employees began working from home and activity around major downtown office and commercial buildings, retail, and restaurants decreased. 
		</p>

		<p>
			Strategies for reviving downtowns post-pandemic, particularly in small and mid-sized cities like Halifax, often include encouraging a pedestrian-friendly environment with cultural activities, active retail, and a diverse mix of employment.<Footnote id={addFootnote(fns[11])} /> Yet municipal leaders today are confronted with unprecedented budget constraints, and many are waiting to see what kind of activity returns to downtown before investing in new major infrastructure or cultural spaces.<Footnote id={addFootnote(fns[12])} /> The ways that downtown neighbourhoods recover in the next few years will likely affect the long-term recovery of surrounding regions.<Footnote id={addFootnote(fns[13])} /> 
		</p>

		<p>
			In Halifax, concerns about the rising cost of living, including the cost of energy and real estate, have contributed to a sense of pessimism among both the commercial sector and general population.<Footnote id={addFootnote(fns[14])} /> There is a risk that this pessimism becomes a self-fulfilling prophecy, with fewer people coming downtown because they believe there is nothing for them there, and less investment in the spaces, events, and transportation networks that add vitality to the core.<Footnote id={addFootnote(fns[15])} /> To counteract this sentiment and showcase the breadth of activity downtown, the EDDIT team analyzed how many people visited downtown, where they were coming from, and where specifically they were going. 
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/Halifax_monthly-stops-heatmap-360.svg"}
		svg720={"./halifax-ns/web-svg/Halifax_monthly-stops-heatmap-720.svg"}
	/>

	<div class="text">

		<h2>Measuring downtown activity</h2>

		<p>
			As in many cities, there is no single spatial definition of “downtown” in Halifax. Finding data at the scale of the downtown district can also be difficult: while the DHBC team accesses region-wide data from the Halifax Regional Municipality’s economic development organization, there is less available at the neighbourhood scale. For the purposes of their own analysis, the DHBC established boundaries for downtown neighbourhoods. Though these are not official boundaries, they are useful for tracking visitors and concentrations of activity.
		</p>

		<p>
			Using aggregated and anonymized cell phone data from Cuebiq, the team measured monthly visits to downtown as a proxy for activity.<Footnote id={addFootnote(fns[16])} /> These data indicate that downtown Halifax has recovered more rapidly than many other Canadian city centres, and is likely to match pre-pandemic traffic levels by summer 2025.<Footnote id={addFootnote(fns[17])} />
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/halifax_canada-recovery-360.svg"}
		svg720={"./halifax-ns/web-svg/halifax_canada-recovery-720.svg"}
	/>

	<div class="text">

		<p>
			Even more significantly, visitors to downtown come from across the city, reflecting that Halifax residents already visit downtown for work, entertainment, or events. Roughly 85 percent of visitors to downtown in 2023 and 2024 came from within the region, with many visiting several times per month. Encouraging these existing visitors to come downtown more often is one potential strategy for recovery and growth.
		</p>
	
	</div>

	<GraphicSingle
		svg360={"./halifax-ns/web-svg/Halifax_visits-downtown-360.svg"}
		svg720={"./halifax-ns/web-svg/Halifax_visits-downtown-720.svg"}
	/>

	<div class="text">

		<p>
			For downtown to continue to thrive, it will be critical to ensure it remains a year-round destination for residents, not only the seasonal summer tourist population. Investments in great spaces that appeal to a variety of people, family-friendly events and programming, and thoughtful infrastructure are key strategies for creating a vibrant downtown. Fortunately, downtown Halifax has already seen success with this kind of placemaking: over the last several decades, the city has transformed its waterfront from an unwelcoming and declining industrial port to a thriving area with over 100,000 visitors a year.<Footnote id={addFootnote(fns[18])} />
		</p>
	
	</div>

	<ImageSingle
		imageURL={placemImage}
		caption='Placemaking in Downtown Halifax.'
		source="Image credit: T.J. Maguire"
		altText="Photograph of the Downtown Halifax"
		maxWidth="{680}px"
		link="Yes"
	/>

	<div class="text">

		<p>
			Developers and the city have made investments like the C$200 million Queen’s Marque district, public art, unique spaces for small business, and welcoming seating that allows people to linger.<Footnote id={addFootnote(fns[19])} /> Frequent festivals and design features like hammocks and children’s play equipment have made the waterfront one of the city’s premier destinations and a popular community gathering space.<Footnote id={addFootnote(fns[20])} /> Making more investments like these in the rest of downtown would provide benefits both to the public and the city’s budget. 
		</p>
	
	</div>

	<ImageSingle
		imageURL={waterfrontImage}
		caption='The Halifax Waterfront.'
		source="Image credit: T.J. Maguire"
		altText="Photograph of the Halifax Waterfront"
		maxWidth="{680}px"
		link="Yes"
	/>

	<div class="text">
		<p>
			Investing in the Vision 2030 plan today has the potential to increase vibrancy and revenue-generating activity in Halifax’s urban core, which will ultimately lead to better-funded services and infrastructure for the region as whole. A more connected and accessible downtown rewards the whole region, providing opportunities for more people to benefit from the renewed energy and beautiful spaces in the city’s historic centre. By highlighting downtown’s existing assets, data stories like this one can advance the momentum for positive change and create a virtuous cycle of confidence, optimism, and growth.
		</p>
	</div>

	<Footnotes footnotes={footnotes} />

	<div class="details">

		<h2>Additional resources</h2>

		<p>
			<a href="https://downtownhalifax.ca/" target="_blank">Downtown Halifax Business Commission</a>
			<br><br>
			<a href="https://downtownhalifax.ca/vision2030" target="_blank">Downtown Halifax Vision 2030 plan</a>
		</p>

	</div>


</main>

<Footer/>