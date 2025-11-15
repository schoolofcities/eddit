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
	import barstowImage from "./assets/ec-barstow.jpg"
	import letterheadImage from "./assets/ec-letterhead.jpg"

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = ['Matthew Palm et al., “Facing the Future of Transit Ridership: Shifting Attitudes towards Public Transit and Auto Ownership among Transit Riders during COVID-19,” *Transportation* 51, no. 2 (2024): 645–71, [URL](https://doi.org/10.1007/s11116-022-10344-2).',
		'B. J. Hollars, “All Aboard!,” August 24, 2023, [URL](https://volumeone.org/articles/2023/08/24/325006-all-aboard-trolley).',
		'Brian D. Taylor and Eric A. Morris, “Public Transportation Objectives and Rider Demographics: Are Transit’s Priorities Poor Public Policy?,” *Transportation* 42, no. 2 (2015): 347–67, [URL](https://doi.org/10.1007/s11116-014-9547-0).',
		'Jonathan Skolnik and Richard Schreiner, “Benefits of Transit in Small Urban Areas: A Case Study,” *Transportation Research Record* 1623, no. 1 (1998): 47–56, [URL](https://doi.org/10.3141/1623-07).',
		'Dagney Faulk and Michael Hicks, “The Economic Effects of Bus Transit in Small Cities,” *Public Finance Review* 38, no. 5 (2010): 513–39, [URL](https://doi.org/10.1177/1091142110373611).',
		'Kea Wilson, “Why Transit Reliability Is Difficult in Midsized Cities,” *Streetsblog USA*, January 17, 2024, [URL](https://usa.streetsblog.org/2024/01/17/why-transit-reliability-is-tough-in-midsized-cities); Diana Ionescu, “Mid-Size Cities Struggle to Provide Reliable Transit,” *Planetizen News*, January 18, 2024, [URL](https://www.planetizen.com/news/2024/01/127087-mid-size-cities-struggle-provide-reliable-transit).',
		'Todd Litman, *Transportation Economics Simplified: An Introduction to Cost and Benefit Analysis for Transport Planning and Policy Evaluation* (Victoria Transport Policy Institute, 2021).',
		'Wilson, “Why Transit Reliability Is Difficult in Midsized Cities.”',
		'American Public Transportation Association (APTA), “Ridership Trends,” July 2025, [URL](https://transitapp.com/apta).',
		'Leah Binkovitz, “What Makes Transit Successful? Survey Says It’s Frequency, Reliability and Shorter Travel Times,” Kinder Institute for Urban Research, Rice University, July 12, 2016, [URL](https://kinder.rice.edu/urbanedge/what-makes-transit-successful-survey-says-its-frequency-reliability-and-shorter-travel).',
		'Dristi Neog and Jeffrey Brown, “Transit Ridership Growth in Small Urbanized Areas: Lessons from Seven US Transit Systems,” *Journal of Urban Planning and Development* 148, no. 1 (2022): 05021051, [URL](https://doi.org/10.1061/%28ASCE%29UP.1943-5444.0000771).',
		'Wilson, “Why Transit Reliability Is Difficult in Midsized Cities.”',
		'APTA, “Ridership Trends.”',
		'Elizabeth Deakin et al., *Reviving Public Transit Ridership to Downtowns and Employment Centers: Public Official, Business Leader, and Commuter Perspectives and Strategies for Moving Forward* (Institute of Transportation Studies, University of California, Berkeley, in press).',
		'Neog and Brown, “Transit Ridership Growth in Small Urbanized Areas.”',
		'Nawshin Tabassum et al., “Ways of Increasing Transit Ridership — Lessons Learned from Successful Transit Agencies,” *Case Studies on Transport Policy* 19 (March 2025): 101362, [URL](https://doi.org/10.1016/j.cstp.2024.101362).',
		'Tabassum et al., “Ways of Increasing Transit Ridership”; Faulk and Hicks, “The Economic Effects of Bus Transit in Small Cities.”',
		'Mindy Rhindress and Transit Cooperative Research Program, *Understanding How to Motivate Communities to Support and Ride Public Transportation* (Transportation Research Board, 2008).',
		'C40 Cities Climate Leadership Group, “How to Use Campaigns and Marketing to Encourage Sustainable Transport Choices,” C40 Knowledge Hub, accessed August 8, 2025, [URL](https://www.c40knowledgehub.org/s/article/How-to-use-campaigns-and-marketing-to-encourage-sustainable-transport-choices?language=en_US).',
		'Neog and Brown, “Transit Ridership Growth in Small Urbanized Areas.”',
		'City of Eau Claire, “Introducing Northern Lite: Eau Claire’s New On-Demand Ride Service!,” July 16, 2025, [URL](https://www.eauclairewi.gov/Home/Components/News/News/12129/90).',
		'Litman, *Transportation Economics Simplified.*',
		'Justin Beaudoin et al., “Public Transit Investment and Sustainable Transportation: A Review of Studies of Transit’s Impact on Traffic Congestion and Air Quality,” *Research in Transportation Economics*, Sustainable Transportation, vol. 52 (October 2015): 15–22, [URL](https://doi.org/10.1016/j.retrec.2015.10.004).',
		'Ross Bernet, “How Much CO2 Does A Tree Absorb?,” One Tree Planted, July 25, 2023, [URL](https://onetreeplanted.org/blogs/stories/how-much-co2-does-tree-absorb).'
	];

	let title = "Connecting the Dots: Showcasing the benefits of public transportation"
	let subTitle = "A case study of Eau Claire, Wisconsin"

</script>


<svelte:head>

	<title>{title}  | School of Cities</title>

	<meta name="description" content={subTitle} />
	<meta name="author" content="School of Cities, University of Toronto">

	<meta property="og:title" content={title} />
	<meta property="og:description" content={subTitle} />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://schoolofcities.github.io/design-components/" />
	<meta property="og:image" content="https://raw.githubusercontent.com/schoolofcities/eddit/main/static/web-card.png" />
	<meta property="og:locale" content="en_CA">

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content={title} />
	<meta name="twitter:description" content={subTitle} />
	<meta name="twitter:site" content="https://schoolofcities.github.io/eddit/" />
	<meta name="twitter:image" content="https://raw.githubusercontent.com/schoolofcities/eddit/main/static/web-card.png" /> 

</svelte:head>



<!-- <Password/> -->

<Title 
	title={"Connecting the Dots: Showcasing the benefits of public transportation"}
	subtitle={"A case study of Eau Claire, Wisconsin"} 
	image={titleImage}
	imageCaption={"A friendly bus in Eau Claire."}
	imageSource={"Photo by Michelle Zhang."}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='https://www.linkedin.com/in/kathrynexonsmith/' target='_blank'>Kathryn J. Exon Smith</a> & <a href='https://www.linkedin.com/in/sarah-a-smith-79089b2a0/' target='_blank'> Sarah A. Smith</a>"}
			graphics={"<a href='http://linkedin.com/in/isabeaux-graham/' target='_blank'>Isabeaux Graham</a>, <a href='https://www.linkedin.com/in/michellez-yy' target='_blank'>Michelle Zhang</a>, & <a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a>"}
			date={"September 2025"}
		/>

		<div class="caption-container">
			<p style="margin-top:-21px; margin-bottom: 42px;">
				<span class="caption-source"><a href="./" target="_blank">Click here to view additional EDDIT case studies</a>.</span>
			</p>
		</div>

		<p>
			Public transportation is an essential ingredient for building equitable and connected cities. It provides reliable and affordable access to work, education, health care, family, and community life. However, rising rates of car use and remote work during the pandemic caused many transit systems to experience a drop in ridership, which led to decreased operating revenues and difficulty keeping service levels constant. Five years on, ridership has improved but not fully rebounded to pre-pandemic levels, and many cities are facing difficult decisions about how to plan for future investments.<Footnote id={addFootnote(fns[0])} /> Yet many people still rely on transit, and a lack of transit access has disproportionate effects on those with lower or fixed incomes, as well as those who do not drive or own a vehicle.
		</p>
		<p>
			In Eau Claire, Wisconsin, a team of transit advocates from the community and municipal government wanted to encourage more residents to use the city’s existing public transit service so all could benefit from increased mobility choices, cost savings, and a healthier environment. Eau Claire Transit, the city’s transit service, is in the process of creating a new Transit Development Plan, studying its routes, ridership, and service levels with the aim of better connecting the community and improving access and efficiency with future funding. They came to the <a href="https://schoolofcities.github.io/eddit/" target="_blank">EDDIT data storytelling team</a> to understand and communicate the benefits of transit to the city’s residents, and to grow a stronger community of advocates and users.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/ _eau-claire-contextmap-360.svg"}
		svg720={"./eau-claire-wi/web-svg/ _eau-claire-contextmap-720.svg"}
	/>

	<div class="text">

		<p>
			A city of just over 70,000 people in western Wisconsin, Eau Claire is one of the fastest-growing places in the state, gaining population at roughly three times the state average. Known for its natural beauty, indie bands, and local cuisine, the city is also home to a large student population at the University of Wisconsin-Eau Claire. Public transportation plays a key role in serving this diverse and growing city, especially students, but only about 10 percent of the population in general uses it today. Ridership levels reached a high of around one million trips per year in the decade before the pandemic, and have recovered to just under 700,000 in 2024. As the city continues to expand, ensuring that transit service is able to meet the needs of all residents will be essential for creating an inclusive and connected urban environment.
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
			Like many North American cities, Eau Claire has a long history of transit service. The city ran a network of electric trolley buses in the late nineteenth century, and it was the first in the country to heat its trolleys with electricity.<Footnote id={addFootnote(fns[1])} /> Over time, the rails were removed, and Eau Claire now has a bus-based transit system, with 17 fixed routes crossing the city and stretching into the neighbouring municipality of Altoona.
		</p>

	</div>

	<ImageSingle
		imageURL={barstowImage}
		caption='Streetcars on Barstow Street, 1907.'
		source="Image credit: Wisconsin Historical Society, WHI - 124971."
		altText="Photograph of a Barstow Street looking north."
		maxWidth="{680}px"
		link="Yes"
	/>

	<div class="text">

		<p>
			The existing network provides good coverage to major employment centres and schools, including the university and the various Mayo Clinic Health System clinics, which are centrally located and together employ over 10 percent of the population. It also provides frequent service to the denser, lower-income neighbourhoods near downtown.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_city-reference-map-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_city-reference-map-720.svg"}
	/>

	<div class="text">

		<p>
			Household income, access to affordable housing, and educational attainment levels vary across the city, contributing to differing levels of transportation use. While many households own multiple vehicles, there is a sizeable percentage of the population that relies on transit exclusively for getting around and meeting their daily needs. Often known as “dependent riders,” this group includes individuals who have restricted mobility options or a limited or fixed budget, including students, seniors, veterans, newcomers, and single-parent households.<Footnote id={addFootnote(fns[2])} /> For these residents, transit isn’t a choice, it’s a lifeline that enables access to employment, education, health care, and essential services.<Footnote id={addFootnote(fns[3])} />
		</p>

	</div>

	<GraphicMultiples
		svgPaths={["./eau-claire-wi/web-svg/eau-claire_novehicle-map-360.svg", "./eau-claire-wi/web-svg/eau-claire_2+vehicle-map-360.svg"]}
	/>
	
	<div class="text">

		<p>
			Eau Claire Transit has a strong focus on equitable access, with stair-free buses that can lower to sidewalk level for accessibility purposes. The system is also in the middle of a period of change and growth, with a long-planned central transfer station (with affordable housing built above) set to open in fall 2025. However, funding constraints and depressed levels of ridership pose challenges to increasing service, offering fare subsidies, or other expansions that could take the system to the next level.
		</p>
		<h2>The challenges of providing transit in small cities</h2>
		<p>
			Transit advocacy and research is often focused on large cities, where the majority of transit users live, but public transit is also a critical service for smaller communities, which may have fewer local resources to improve their systems.<Footnote id={addFootnote(fns[4])} /> In part, this is due to historical development patterns in smaller cities, which are less likely to be densely developed, meaning federal and state investments have favoured building more roads and highways, with less investment in building transit routes connecting jobs with housing.<Footnote id={addFootnote(fns[5])} /> As with road users, transit users rarely pay the full cost of maintenance and operations, so most systems require government subsidization.<Footnote id={addFootnote(fns[6])} /> However public transit has historically been more politicized than other means of transportation, and so often suffers from a lack of investment. Over several decades, this has pushed new development to the less-expensive and less regulated auto-oriented city edges, creating a cycle of car dependency, depriving agencies of the fare revenues they need to invest in service improvements, and making it difficult to maintain stable and reliable service for all riders, particularly ones who depend on it the most.<Footnote id={addFootnote(fns[7])} />
		</p>
		<p>
			These trends were exacerbated by the pandemic, which led many to work from home, or to seek alternate means of travel to avoid close contact with others. Across systems in the United States, transit usage dropped to 20 percent of pre-pandemic levels in April 2020, and has yet to fully recover, though smaller systems have fared slightly better.<Footnote id={addFootnote(fns[8])} /> Eau Claire is one example, with ridership only recovering to about 70 percent of pre-pandemic levels.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_national-ridership-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_national-ridership-720.svg"}
	/>


	<div class="text">

		<p>
			Service frequency and reliability are often ranked as top priorities for transit users,<Footnote id={addFootnote(fns[9])} /> yet many smaller agencies, like Eau Claire Transit, face what is referred to as the <a href="https://humantransit.org/2018/02/basics-the-ridership-coverage-tradeoff.html" target="_blank">coverage versus frequency tradeoff</a>. This refers to the challenge of providing access to as much of the city’s geography as possible, in order to ensure that all neighbourhoods and demographics are being served (coverage), but also having frequent enough service on popular routes to accommodate periods of high demand or those who work or travel at non-standard hours, including evenings and weekends (frequency). With a fixed number of vehicles and funding, this represents a choice between serving all residents equally versus maximizing ridership (and therefore lowering necessary subsidies).
		</p>
		<p>
			Smaller cities are more likely than larger cities to have infrequent service, such as buses or trains that run every 15-30 minutes on weekdays and every 60-90 minutes or not at all on weekends, which can dissuade some users.<Footnote id={addFootnote(fns[10])} /> Some agencies struggle to track the dependability of their service, with many lacking real-time arrival information and GPS tracking.<Footnote id={addFootnote(fns[11])} /> The inability to see arrival times and vehicle status can dissuade new users who perceive car travel as more reliable, even if this is not necessarily the case.
		</p>
		<h2>Opportunities for growth</h2>
		<p>
			Despite these challenges, small transit systems also offer signs of growth and opportunities for expansion. Smaller cities of less than 100,000 people, which often run bus-based transit systems, have to date recovered more of their pre-pandemic ridership than larger cities, which tend to include harder-hit commuter rail systems.<Footnote id={addFootnote(fns[12])} /> Areas with high concentrations of health care facilities and educational institutions — which remain mostly in-person — have also been more resilient.<Footnote id={addFootnote(fns[13])} /> The durability of demand shows the critical role transit plays for those who are dependent upon it.
		</p>
		<p>
			Several small cities have also bucked the trend of declining ridership with strategic service changes. The most successful cities have used survey and observational data from existing riders to understand community needs, key gaps in coverage, who the main users of transit are, and their experience of the system.<Footnote id={addFootnote(fns[14])} /> Increasing the number of buses running a core route, for example, can boost ridership for those looking for a frequent and reliable option. Often, as in Eau Claire, service is centred on major retail locations, employment areas, and important educational or workforce training institutions.<Footnote id={addFootnote(fns[15])} /> Partnering with large local institutions to encourage transit use through passes, free or discounted fares for students and employees, or by removing or disincentivizing parking, can also boost transit use, especially if combined with active transportation programs like bike share.<Footnote id={addFootnote(fns[16])} /> Ultimately, integrating planning and land use with transportation systems is the most effective way to encourage residents to use transit, but this is a long-term process that requires building support for the role of transit in the community.
		</p>

	</div>

	<ImageSingle
		imageURL={letterheadImage}
		caption='Eau Claire Transportation Company Letterhead, 1955.'
		source="Image credit: Wisconsin Historical Society, WHI - 91277."
		altText="Photograph of a Barstow Street looking north."
		maxWidth="{680}px"
		link="Yes"
	/>

	<div class="text">

		<h2>Picture yourself on public transportation</h2>
		<p>
			In anticipation of future change or investment, public awareness campaigns can be successful in showing that everyone in the community has a stake in their transit system, in the same way that many people pay into public health care or education for the benefit of all.<Footnote id={addFootnote(fns[17])} /> The idea is to raise awareness of the existing transit system to turn residents into transit users and advocates. These campaigns have found success around the world at generating positive media coverage, improving ridership, and increasing public perception of transit.<Footnote id={addFootnote(fns[18])} /> In smaller regions like Topeka, Redding, and Middle Tennessee they have boosted ridership, and in other cities have built public and political support for more funding through levies to expand service, offer free or discounted fares, or create transit priority lanes.<Footnote id={addFootnote(fns[19])} />
		</p>
		<p>
			In Eau Claire, the team wanted to take advantage of a key moment in the city’s transit history — the 50th anniversary of the city taking over transit service to make it public and the opening of the new transfer centre — to show how public transit can be a robust connector to school, work, health care, and popular destinations, supporting the evolving needs of a growing population. In addition to conducting a detailed study of existing users and potential opportunities for improvement, the City of Eau Claire also aimed to “power up” transit use through a public awareness campaign highlighting the benefits of transit through data storytelling, which they could communicate to community groups, major employers, and the general public. The EDDIT team created data pieces that could support the first element of the campaign, which showcases the current system coverage, highlighting how many people can get downtown within 45 minutes and how accessible major hospitals are by bus.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_transit-map-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_transit-map-720.svg"}
	/>


	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_mayo-map-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_mayo-map-720.svg"}
	/>

	<div class="text">

		<p>
			Here, transit is positioned as a way to expand transportation choices and provide a convenient means of reaching major destinations throughout the city. It also shows how transit can mean independence for those who do not have the option to drive or own a car, including seniors, youth, newcomers, or those without a license, raising awareness of its importance for these groups. The city aims to provide fare-free transit for veterans and children as an additional incentive. For those outside of the coverage area, it will also launch a micro transfer pilot program, in which smaller vehicles pick people up at their door and take them to the central transfer station or elsewhere within the zone for the standard fare.<Footnote id={addFootnote(fns[20])} />
		</p>
		<p>
			The second element of the campaign shows the direct financial benefit of using transit rather than a personal vehicle. In a city where many households are struggling with living costs, using transit for some trips can help reduce reliance on multiple vehicles and ease financial pressure.<Footnote id={addFootnote(fns[21])} /> When car payments, maintenance, fuel, and insurance are included, these savings can be substantial. For lower- and middle-income households especially, the savings associated with shifting some travel to public transit can free up resources for other necessities and improve overall financial stability. The Eau Claire team calculated that redirecting this spending locally could put over US$2 million back into the local economy each year, an additional collective benefit.
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_transit-savings-chart-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_transit-savings-chart-720.svg"}
	/>

	<div class="text">

		<p>
			Taking transit can also have broader community benefits, including reducing traffic congestion and improving air quality by lowering emissions.<Footnote id={addFootnote(fns[22])} /> When people take transit instead of driving, they reduce the number of miles travelled in personal vehicles, and the associated levels of carbon dioxide (CO<sub>2</sub>) and other particulates. To show these environmental effects, the team calculated that returning to pre-pandemic ridership levels could lower CO<sub>2</sub> emissions in the area by over 800,000 pounds per year. That is the same amount of CO<sub>2</sub> that can be absorbed by 36,000 trees, or a forest the size of 180 football fields.<Footnote id={addFootnote(fns[23])} />
		</p>

	</div>

	<GraphicSingle
		svg360={"./eau-claire-wi/web-svg/eau-claire_emissions-savings-chart-360.svg"}
		svg720={"./eau-claire-wi/web-svg/eau-claire_emissions-savings-chart-720.svg"}
	/>

	<div class="text">

		<p>
			At a time of expansion and change in Eau Claire, creating a city of public transit champions is the first step in raising awareness and support for an even more robust and connected system, one that serves the whole population and drives economic growth and equity. With these data, the team can make the benefits of transit more visible, both for individuals and for the community as a whole. Their next step is to focus on targeted outreach strategies and public education to increase ridership and create a virtuous cycle that will generate an even greater presence for public transit for the agency’s next fifty years.
		</p>

	

		<br>
		<p style="font-size: 16px; line-height: 25px;">
			<i>The authors would like to thank Karen Chapple, Michelle Zhang, Julia Greenberg, and Evelyne St-Louis for their contributions to editing and informing this case study.</i>
		</p>
		<br>

		<Footnotes footnotes={footnotes} />

		<div class="details">

			<h2>Additional resources</h2>

			<p>
				<a href="https://volumeone.org/articles/2023/08/24/325006-all-aboard-trolley" target="_blank">History of the Eau Claire Trolley</a>
				<br><br>
				<a href="https://www.eauclairewi.gov/government/our-divisions/transit/transit-administration/transit-development-plan" target="_blank">Eau Claire Transit Development Plan (2020)</a>
			</p>

		</div>

	</div>
		
</main>

<Footer/>