<script>

	import "../../../assets/global-styles.css"

	import Password from "#lib/Password.svelte";
	import Title from '#lib/Title.svelte';
	import AuthorDate from "#lib/AuthorDate.svelte";
	import Footer from "#lib/Footer.svelte";
	import GraphicSingle from "#lib/GraphicSingle.svelte";
	import GraphicMultiples from "#lib/GraphicMultiples.svelte";
	import ImageSingle from "#lib/ImageSingle.svelte";
	import VideoSingle from "#lib/VideoSingle.svelte";
	import Map from "./components/Map.svelte";

	import titleImage from "./assets/IMG_7259.jpeg";

	import Footnote from '#lib/Footnote.svelte';
    import Footnotes from '#lib/Footnotes.svelte';
    import { createFootnoteStore } from '#lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;



    const fns = [
		'"BART is facing a financial deficit," *Bay Area Regional Transit* [URL](https://www.bart.gov/about/financials/crisis)',
		'"The SFMTAs Financial Crisis," *SFMTA*, [URL](https://www.sfmta.com/project-updates/sfmtas-financial-crisis)',
		'"GOVERNOR NEWSOM AND STATE LEADERS CHAMPION EAST BAY RIDERS WITH SB 63 APPROVAL," *AC Transit*, October 14, 2025, [URL](https://www.actransit.org/press-release/governor-newsom-state-leaders-champion-east-bay-riders-approving-sb-63)',
		'"Caltrain Budget Deficit," *Caltrain*, [URL](https://www.caltrain.com/caltrain-budget-deficit)',
		'"Accessibility (transport)," *Wikipedia*, [URL](https://en.wikipedia.org/wiki/Accessibility_(transport))',
		'U.S. Census Bureau, *Tenure by Vehicles Available*, (American Community Survey 5-Year Estimates, Table B25044) (2024), Retrieved Oct 5, 2026, [URL](https://data.census.gov/table/ACSDT5Y2024.B25044?q=B25044&g=050XX00US06001$1500000)',
		'"Ridership Reports - September 2026 Ridership OD," *Bay Area Rapid Transit*, [URL](https://www.bart.gov/about/reports/ridership)',
		'"Annual Ridership Reports - Fiscal Year 2026 Annual Ridership Report," *Caltrain*, [URL](https://www.caltrain.com/about-caltrain/statistics-reports/ridership/annual-reports).'
   	];

	let title = "HOW TRANSIT CUTS COULD COST THE BAY AREA"
	let subTitle = "A case study of the San Francisco Bay Area"

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
	title={title}
	subtitle={subTitle}
	image={titleImage}
	imageCaption={"MUNI stop in San Francisco."}
	imageSource={"Photo by Isabeaux Graham, October 2026."}
/>

<main>

	<div class="text">

		<AuthorDate
			authors={"<a href='http://linkedin.com/in/isabeaux-graham/' target='_blank'>Isabeaux Graham</a> & <a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a>"}
			date={"October 2026"}
		/>

		<div class="caption-container">
			<p style="margin-top:-21px; margin-bottom: 42px;">
				<span class="caption-source"><a href="./" target="_blank">Click here to view additional EDDIT case studies</a>.</span>
			</p>
		</div>

		<p>
			Based on 2026 data, the average Bay Area resident can reach more than 247,000 jobs within 60 minutes by transit. That may soon change. Because of a major funding deficit at the start of 2027, Bay Area transit agencies may be forced to cut service. Proposed cuts include BART reducing service by 70% and closing 15 stations,<Footnote id={addFootnote(fns[0])} /> reducing MUNI frequencies up to 50% and cancelling routes including cable cars,<Footnote id={addFootnote(fns[1])} /> AC Transit reducing service up to 37%,<Footnote id={addFootnote(fns[2])} /> and Caltrain reducing service to one train per hour and eliminating weekend service.<Footnote id={addFootnote(fns[3])} />
		</p>
		<p>
			We analyzed how these service cuts could shrink the number of jobs people can reach by public transit, and the impacts vary significantly by county.  For this analysis, we are defining the Bay Area as the five counties of Alameda, Contra Costa, San Francisco, San Mateo, and Santa Clara. We focus on job access because it captures both the transit network (where routes run and how often) and land use (where jobs and destinations are located), so it shows how well transit connects people to the places they need to go. Jobs are spread across a region much like other everyday destinations, which makes job access a good proxy for access to schools, healthcare, groceries, and more.<Footnote id={addFootnote(fns[4])} />
		</p>
		<p>
			Across the Bay Area, job access loss generally grows more slowly than the cut itself. Cutting 40% of routes does not usually cost 40% of jobs, because many trips have alternative routes. For example, at a 40% cut, Santa Clara has a mean 37% reduction in job access while San Francisco sees 13% in reductions. San Francisco has a denser network that allows for some redundancy, but once cuts exceed 60%, its losses climb steeply. Contra Costa also sits far below the proportional loss line, at 20% for a 40% cut, but it has very little transit access to lose in the first place. San Mateo varies the most between cut route iterations, which suggests the county depends on a few key transit routes. In four of the five counties, households without a car could lose access to more jobs than households with at least one vehicle, and in Alameda and Contra Costa, lower-income households would carry a disproportionate share of the loss.
		</p>

	</div>


	<div class="text">

		<h2>WHERE THE JOB ACCESSIBILITY LOSSES LAND</h2>

		<p>
			The following maps show the same story geographically. Job accessibility is concentrated in San Francisco, the East Bay corridor, the Peninsula, and San Jose. At a 40% cut, the heaviest losses fall along the Peninsula and South Bay corridors while San Francisco shows some of the lightest.
		</p>

	</div>
		
	<Map candidate="transit" />

	<div class = "text">	
		<h2>
			WHO IS AFFECTED
		</h2>
		
		<p>
			Disparities in job accessibility loss emerge when examining specific groups of households within each county. We compared zero-vehicle households against all other households, those with at least one vehicle. Within each county, we averaged job accessibility loss across block groups, first weighting each block group by its number of zero-vehicle households and then, separately, by its number of households with a vehicle. 
		</p>
	</div>


	<GraphicSingle
		svg360={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_noveh360.svg"}
		svg720={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_noveh.svg"}
	/>

	<div class = "text">
		<p>
			At a 40% transit cut, zero-vehicle households lose accessibility to more jobs  than other households in four out of the five counties. In Alameda and Contra Costa, they lose access to 1.6 and 1.7 times as many jobs as households with a vehicle, respectively. These households tend to live where transit access is strongest today. However, they are also households with the fewest alternatives for getting to work when service shrinks.
		</p>
		<p>
			San Francisco is the exception. With a much higher share of zero-vehicle households overall (30%), it is households with a vehicle that face the larger job losses. This is likely because San Francisco’s car ownership rates are higher on the outskirts of the city, where fewer routes run. <Footnote id={addFootnote(fns[5])} />
		</p>
		<p>
			How badly a cut hurts depends less on its size than on how much backup a network has. Santa Clara has little to fall back on, while San Francisco and Contra Costa absorb moderate cuts better. In San Mateo, protecting a few key routes could matter more than the overall size of the cut.
		</p>

		<h3>
			ALAMEDA COUNTY
		</h3>

	</div>

	<GraphicSingle
		svg360={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_AlamedaSTAT_360.svg"}
		svg720={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_AlamedaSTATS.svg"}
	/>

	<div class = "text">

		<p>
			Alameda is where transit cuts hit the households with the fewest alternatives the hardest. Households earning less than $75K lose access to 1.66 times as many jobs per household as households earning more than $150K. Zero-vehicle households, which tend to live in the neighbourhoods with the most to lose, lose access to 145K jobs per household compared with 88K for everyone else. 
		</p>
	</div>

	<GraphicSingle
		svg360={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_AlamedaViz_360.svg"}
		svg720={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_AlamedaViz_720.svg"}
	/>

	<div class = "text">

		<p>
			Alameda county is also a major cross-county commuting county. More than half of its residents (55%) work outside the county, including 42.6% who work in one of the four other Bay Area counties. Outside the county, Santa Clara (122K workers) and San Francisco (190K) are the biggest destinations, while the largest group of in-commuters come from Contra Costa. 
		</p>
		<p>
			The key corridors into San Francisco and Santa Clara are I-80 West, I-880 South, and I-680 South, with BART transit lines following the first two. Those roads already see major bottlenecks during rush hour. Looking at every Tuesday since June, where data is available, the drive west on I-80 from Richmond to half way across the Bay Bridge (about 14 miles) has averaged 38 minutes at 8 AM, more than double the 16 minutes it takes outside of rush hour (free flow). Some days it has reached over 50 minutes. On I-880 South from San Lorenzo to northern Fremont (just over 8 miles), the 8 AM trip has averaged 19 minutes, nearly triple the 7 minute commute at free flow, and over the last two months a typical Tuesday has taken about 25 minutes. If public transportation service shrinks, those able to switch to roads will only add to these commute times.
		</p>

		<h3>
			CONTRA COSTA COUNTY
		</h3>
	</div>

	<GraphicSingle
		svg360={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_ContraCostaSTAT_360.svg"}
		svg720={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_ContraCostaSTATS.svg"}
	/>

	<div class = "text">

		<p>
			Contra Costa loses a smaller share of its job accessibility than most of the counties, but that is partly because it has so little transit access to lose. It has by far the fewest baseline accessible jobs of the five counties. Only 7.6% of residents can reach more than 150K jobs, compared with 99.5% of San Francisco residents. 
		</p>
		<p>
			Sixty-four percent of residents work outside the county, the highest rate in the region, including 21% who work in Alameda, almost 110K workers.
		</p>
	</div>

	<GraphicSingle
		svg360={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_ContraCostaVIZ_360.svg"}
		svg720={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_ContraCostaVIZ_720.svg"}
	/>

	<div class = "text">
		<p>
			Sitting on the Alameda and Contra Costa border, the Caldecott Tunnel is a major bottle neck as commuters flow into Alameda in the morning and out in the afternoon. Over the last four months, the average Tuesday drive east on SR-24 from the I-580 interchange in Oakland to southern Walnut Creek (about 12.5 miles) took 31 minutes at 5 PM, compared with an 11 minute travel time outside of rush hour (free flow). BART’s Yellow Line follows the same route in 19 minutes, and on an average weekday in September 2026, more than 12K riders took it west along the SR-24 corridor.<Footnote id={addFootnote(fns[6])} /> For Contra Costa commuters, the road is not an easy substitute if BART service is cut. 
		</p>

		<h3>
			SAN FRANCISCO COUNTY
		</h3>

	</div>

	<GraphicSingle
		svg360={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_SanFranciscoSTAT_360.svg"}
		svg720={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_SanFranciscoSTATS.svg"}
	/>

	<div class = "text">

		<p>
			San Francisco has by far the densest transit network of the five Bay Area counties. Ninety-nine percent of workers live in block groups that reach more than 400K jobs, 828K on average, 3.3x the regional average. At a 40% transit cut, it loses 13% of that access, the lowest share in the region. 
		</p>
		<p>
			San Francisco also breaks the pattern seen in Alameda and Contra Costa. Lower, middle, and high-income households all bear about the same share of the loss as their share of households, and zero-vehicle households lose fewer jobs than households with a car. 
		</p>
		<p>
			About 58% of residents work in San Francisco, but more than 303K workers commute in from the other four counties, more than half of the Bay Area residents who hold jobs there. While the county itself seems resilient to transit cuts, other counties with residents that commute in could lose a larger share of access to San Francisco and thus the city could still lose workers. 
		</p>
		<p>
			The types of jobs are also impacted disproportionately in San Francisco. Professional, scientific, and tech services is the largest industry by jobs reachable in San Francisco (155K on average). Bay Area residents lose access to only 8.7% of those jobs, one of the lowest rates across industries. In contrast, health care, the second largest industry by reachability in the county (119K on average) has a job accessibility loss rate of 15.1%, almost 18K jobs, the second highest rate among industries. Essential workers often keep schedules outside the weekday morning window we modeled in this analysis. Therefore, the losses they face could be larger than shown, and service is thinnest at the hours Health Care workers may need it. 
		</p>

		<h3>
			SAN MATEO COUNTY
		</h3>
	</div>

	<GraphicMultiples
		svgPaths={[
			"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_SanMateoSTAT_360.svg",
			"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_SanMateoVIZ_360.svg"
		]}
	/>

	<div class = "text">

		<p>
			San Mateo’s job accessibility loss is highly dependent on which routes are cut. At a 40% cut, the county loses an average of 36% of its job accessibility, second highest in the region, but across the 35 random cut scenarios (see APPROACH AND LIMITATIONS below), the loss ranged from 23.4% to 47.9%, the widest spread of any county.  That points to a handful of routes carrying the county, so which routes are cut could matter more than how many.
		</p>
		<p>
			San Mateo, at the baseline, already has limited accessibility. Nearly a quarter of residents can reach fewer than 10K jobs. However, the county has the highest share of workers commuting to another Bay Area county at 51%, with 22% going to San Francisco and 19% to Santa Clara. The key arteries for commuting are US-101, I-280, and Caltrain. In Fiscal Year 2026 (July 2025 to June 2026), Caltrain averaged an estimated 14,458 midweek trips per day starting at San Mateo County stations.<Footnote id={addFootnote(fns[7])} /> Our model removes whole routes, while Caltrain’s proposal reduces how often service runs, so it only can approximate that cut, but the implications of reduced transit for this county are clear. 
		</p>

		<h3>
			SANTA CLARA COUNTY
		</h3>

	</div>

	<GraphicSingle
		svg360={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_SantaClaraSTAT_360.svg"}
		svg720={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_SantaClaraSTATS.svg"}
	/>

	<div class = "text">

		<p>
			Santa Clara has the most workers of any Bay Area county (952K resident workers), and with 40% transit cuts has the highest percentage of job accessibility lost at 37%, or nearly 54K jobs lost per worker. The county's transit network has the least to fall back on if cuts happen, with the losses running almost one for one with the cut (proportional loss). 
		</p>
		<p>
			Unlike Alameda and Contra Costa Counties, lower, middle, and high-income households lose job accessibility in proportion to their share of the county. Additionally, no industry has a disproportionate loss at a 40% cut, so the effects spread more evenly across the county. 
		</p>
		<p>
			Santa Clara county also has the largest percent of resident workers that work in the county at nearly 68% with nearly 264K commuting into the county, second only to the 303K Bay Area workers who commute into San Francisco. 
		</p>

		<h2>
			WHAT THIS MEANS
		</h2>

		<p>
			While random cuts in this analysis are not a forecast of what will be cut and what will happen, they show where the transit networks in the Bay Area are most fragile. At a 40% cut level, San Francisco loses about a third of its job accessibility while Santa Clara loses nearly 40%. The burden is also uneven with lower-income and zero-vehicle households experiencing more of the loss in Alameda and Contra Costa counties. Additionally, because more than a third of the region’s workers (36%) cross into one of the other Bay Area counties to work, cuts in one county’s network are felt by workers who live in another. 
		</p>


		<h2>APPROACH & LIMITATIONS</h2>

		<p>
			We randomly removed transit routes across Alameda, Contra Costa, San Francisco, San Mateo, and Santa Clara counties, then measured how many jobs each neighborhood could still reach within an hour. Because the agency proposals range from 16% to 70%, we focus on a 40% cut, roughly the middle of that range, and show the full 10% to 100% range in the charts.
		</p>
		<p>
			Random removal is not a forecast of which routes will be cut, since agencies will likely weigh ridership. It works as a test of how impactful each county’s network is for the commuter and how robust each county’s network is to providing service despite cutting service. Our model also removes whole routes, while some proposals, like Caltrain’s, reduce how often service runs, so it only approximates those cuts.
		</p>

	</div>

	<GraphicSingle
		svg360={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_dose360.svg"}
		svg720={"/eddit/bay-area-job-accessibility/web-svg/JobAccessibility_dose.svg"}
	/>

	<div class="text">

		<p>
			For this analysis, we utilized r5py to construct the Bay Area public transit network. For each cut level, from 10% to 100%, we randomly removed that share of the routes running between 6 and 9 AM on a Tuesday and rebuilt the network from the remaining routes. We repeated this 35 times at each level, using a different random draw (seed) each time. Within a draw, cuts are nested: routes removed at 10% are also removed at 20%, and so on, so results at different cut levels are directly comparable.
		</p>
		<p>
			For each network, a travel time matrix is constructed measuring the travel time of each block group to every other block group. Using job counts by block group from Longitudinal Employer-Household Dynamics (LEHD) data, we then counted how many jobs each block group could reach within 60 minutes and compared that with the present-day baseline. Zero-vehicle household data come from the American Community Survey (2024).
		</p>
		<p>
			Results reflect one weekday morning window and a 60-minute threshold. Routes are removed completely and at random, rather than by ridership or frequency, so the results show network resilience, not predicted outcomes. Additionally, BART specifically has proposed removing stops rather than entire routes, which was not factored into this analysis. 
		</p>
		<p>
			Another limitation with this analysis is that we looked at transit travel times on a Tuesday from 6am to 9am. This looks at when most people are likely to be using public transportation for commuting to 9 to 5 jobs. However, it ignores essential workers who may be working outside of the timeframe. They are likely to face even more limited transit options. 
		</p>

	</div>


	<div class="text">

		<br>
		
		<Footnotes footnotes={footnotes} />

	</div>

</main>

<Footer/>
