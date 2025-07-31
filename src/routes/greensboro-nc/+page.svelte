<script>

	import "../../assets/global-styles.css"

	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/greensboro-title.jpg";
	import groceryImage from "./assets/image-grocery.jpg";
	import carrotImage from "./assets/image-carrots.jpg";

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = [
		'Jason Massey et al., “The Association Between Census Tract Healthy Food Accessibility and Life Expectancy in the United States,” *Journal of Urban Health* 100, no. 3 (2023): 572–76, [URL](https://doi.org/10.1007/s11524-023-00742-x).', 
		'Marie T. Ruel et al., “Urban Food Systems and Diets, Nutrition, and Health of the Poor: Challenges, Opportunities, and Research Gaps,” *Handbook on Urban Food Security in the Global South*, Edward Elgar Publishing, 2020, 380–96.',
		'Regina Bellian, “Food Deserts in Urban Areas,” *The Downtown Review* 6, no. 1 (2019), [URL](https://engagedscholarship.csuohio.edu/tdr/vol6/iss1/1).',
		'Nicole I. Larson et al., “Neighborhood Environments: Disparities in Access to Healthy Foods in the U.S.,” *American Journal of Preventive Medicine* 36, no. 1 (2009): 74–81.e10, [URL](https://doi.org/10.1016/j.amepre.2008.09.025).',
		'Jingjing Li and Changjoo Kim, “Exploring Relationships of Grocery Shopping Patterns and Healthy Food Accessibility in Residential Neighborhoods and Activity Space,” *Applied Geography* 116 (March 2020): 102169, [URL](https://doi.org/10.1016/j.apgeog.2020.102169).',
		'Janel Hanmer et al., “Association between Food Insecurity and Health-Related Quality of Life: A Nationally Representative Survey,” *Journal of General Internal Medicine* 36, no. 6 (2021): 1638–47, [URL](https://doi.org/10.1007/s11606-020-06492-9).',
		'Latetia V. Moore and Ana V. Diez Roux, “Associations of Neighborhood Characteristics With the Location and Type of Food Stores,” *American Journal of Public Health* 96, no. 2 (2006): 325–31, [URL](https://doi.org/10.2105/AJPH.2004.058040); Kristian Larsen and Jason Gilliland, “Mapping the Evolution of ‘food Deserts’ in a Canadian City: Supermarket Accessibility in London, Ontario, 1961–2005,” *International Journal of Health Geographics* 7, no. 1 (2008): 16, [URL](https://doi.org/10.1186/1476-072X-7-16).',
		'Kelly M Bower et al., “The Intersection of Neighborhood Racial Segregation, Poverty, and Urbanicity and Its Impact on Food Store Availability in the United States,” *Preventive Medicine* 58 (January 2014): 33–39, [URL](https://doi.org/10.1016/j.ypmed.2013.10.010).',
		'Angela Odoms-Young et al., “Food Insecurity, Neighborhood Food Environment, and Health Disparities: State of the Science, Research Gaps and Opportunities,” *The American Journal of Clinical Nutrition* 119, no. 3 (2024): 850–61, [URL](https://doi.org/10.1016/j.ajcnut.2023.12.019).',
		'Bower et al., “The Intersection of Neighborhood Racial Segregation, Poverty, and Urbanicity.”',
		'Healthy Food Policy Project, Towards Equitable and Just Food Systems: Exploring Food Justice, Food Sovereignty, and Ending Food Apartheid Policy & Practice (2022).',
		'Michael J. Widener, “Spatial Access to Food: Retiring the Food Desert Metaphor,” *Physiology & Behavior* 193 (2018): 257–60, [URL](https://doi-org./10.1016/j.physbeh.2018.02.032).',
		'P. B. Ford and D. A. Dzewaltowski, “Geographic, Racial, Ethnic, and Socioeconomic Disparities in the Availability of Grocery Stores and Supermarkets Among Low-Income Women Across the Urban–Rural Continuum,” *Journal of Hunger & Environmental Nutrition* 5, no. 2 (2010): 216–33, [URL](https://doi.org/10.1080/19320241003800276); Kathryn M. Janda et al., “Who Shops at Their Nearest Grocery Store? A Cross-Sectional Exploration of Disparities in Geographic Food Access among a Low-Income, Racially/Ethnically Diverse Cohort in Central Texas,” *Journal of Hunger & Environmental Nutrition* 19, no. 3 (2024): 355–75, [URL](https://doi.org/10.1080/19320248.2022.2128962).',
		'James D. Wright et al., “Food Deserts: What Is the Problem? What Is the Solution?,” *Society* 53, no. 2 (2016): 171–81, [URL](https://doi.org/10.1007/s12115-016-9993-8); The Annie E. Casey Foundation, Food Deserts in America: Understanding The Impact on Communities with Limited Food Access, February 14, 2021, [URL](https://www.aecf.org/blog/food-deserts-in-america).',
		'Eli Zigas, *Healthy Food Within Reach* (SPUR, 2015), [URL](https://www.spur.org/sites/default/files/2021-05/SPUR_Healthy_Food_Within_Reach_Report.pdf); Michael J. Widener et al., “How Do Changes in the Daily Food and Transportation Environments Affect Grocery Store Accessibility?,” *Applied Geography* 83 (2017): 46–62.',
		'Nadra Hashim, “Reversing Food Desertification: Examining Urban Farming in Louisville, Chicago and Detroit,” *Local Environment* 20, no. 6 (2015): 611–36, [URL](https://doi.org/10.1080/13549839.2014.931364).',
		'Michael Widener et al., “Developing a Mobile Produce Distribution System for Low-Income Urban Residents in Food Deserts,” *Journal of Urban Health: Bulletin of the New York Academy of Medicine* 89, no. 5 (2012), [URL](https://doi.org/10.1007/s11524-012-9677-7); Bellian, “Food Deserts in Urban Areas.”',
		'Aggregated mobility data are provided by Cuebiq, a location intelligence platform. Data is collected from anonymized users who have opted-in to provide access to their location data anonymously, through a CCPA and GDPR-compliant framework. Through its Social Impact program, Cuebiq provides mobility insights for academic research and humanitarian initiatives. The Cuebiq responsible data sharing framework enables research partners to query anonymized and privacy enhanced data, by providing access to an auditable, on-premise Data Cleanroom environment. All final outputs provided to partners are aggregated in order to preserve privacy.',
		'Zigas, *Healthy Food Within Reach*.',
		'Elizabeth Egan, “Triad’s First Piggly Wiggly Set to Open in Greensboro This Summer after Years of Delays,” *Triad Business Journal*, January 9, 2025, [URL](https://www.bizjournals.com/triad/news/2025/01/09/piggly-wiggly-greensboro-triad-retail-grocery-nc.html); Jeremy Vernon, “Opening of Greensboro Piggly Wiggly — First in the Triad — Delayed, New Date TBA,” *WFMY News*, April 3, 2025, [URL](https://www.wfmynews2.com/article/money/business/greensboro-piggly-wiggly-opening-delayed/83-29682696-e014-4a54-ace4-e28a453c0b20).',
		'Joe Killian, “In One of NC’s Many Food Deserts, a Co-Op Grocery Store Closes • NC Newsline,” *NC Newsline*, January 14, 2019, [URL](https://ncnewsline.com/briefs/in-one-of-ncs-many-food-deserts-a-co-op-grocery-store-closes/).',
		'Melissa N. Laska and Jennifer E. Pelletier, *Minimum Stocking Levels and Marketing Strategies of Healthful Foods for Small Retail Food Stores* (Healthy Eating Research, 2016), [URL](https://healthyeatingresearch.org/wp-content/uploads/2016/02/her_minimum_stocking_final.pdf).',
		'Elizabeth F. Racine et al., “Availability of Foods and Beverages in Supplemental Nutrition Assistance Program−Authorized Dollar Stores in a Region of North Carolina,” *Journal of the Academy of Nutrition and Dietetics* 116, no. 10 (2016): 1613–20, [URL](https://doi.org/10.1016/j.jand.2016.03.014).',
		'Society for Public Health Education (SOPHE), *Increasing Access to Healthy Foods Community Toolkit* (2015), [URL](https://www.sophe.org/wp-content/uploads/2017/02/Access-to-Healthy-Foods-Toolkit_April.pdf).',
		'Thomas Reardon, *Growing Food for Growing Cities: Transforming Food Systems in an Urbanizing World* (The Chicago Council on Global Affairs, 2016).'
	];
	

</script>





<!-- <Password/> -->

<Title
	title={"Increasing the availability of healthy food"}
	subtitle={"A case study of Greensboro, North Carolina"}
	image={titleImage}
	imageCaption={"___"}
	imageSource={"___"}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='' target='_blank'>Kathryn Exon Smith</a> & <a href='' target='_blank'>Sarah A. Smith</a>"}
			graphics={"<a href='' target='_blank'>Jeff Allen</a> & <a href='' target='_blank'>Isabeaux Graham</a>"}
			date={"August 2025"}
		/>

		<p>
			The availability of fresh, healthy, and affordable food is linked with reduced levels of obesity and diabetes, higher educational attainment, and longer life expectancy.<Footnote id={addFootnote(fns[0])} /> Yet access to healthy food can vary considerably within cities, leaving some neighbourhoods with limited options. Private-sector retailers are generally reluctant to open brick-and-mortar grocery stores in areas with lower incomes, reinforcing geographic and socioeconomic inequities. However, there are non-traditional opportunities for cities and local organizations to bring more healthy food options to communities that need them.
		</p>

	</div>

	<GraphicSingle
		svg720={"./greensboro-nc/web-svg/greensboro-contextmap-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-contextmap-360.svg"}
	/>

	<div class="text">

		<p>
			In Greensboro, North Carolina, the <a href="https://conehealthfoundation.com" target="_blank">Cone Health Foundation</a>, the philanthropic arm of a large network of healthcare providers, is driven by a desire to address the root causes of health inequities in the city. Recognizing that health is closely tied to economics, transportation, and housing, the foundation has partnered with the City of Greensboro’s Department of Housing and Neighborhood Development and <a href="https://www.eastgreensboronow.com/" target="_blank">East Greensboro NOW</a>, a community economic development agency.
		</p>
		<p>
			This coalition partnered with the <a href="https://schoolofcities.github.io/eddit/" target="_blank">EDDIT data storytelling team</a> with the goal of expanding the availability of healthy and affordable food options throughout the city, particularly in East Greensboro, a historically underserved and economically disadvantaged area.* Greensboro has been a hub for textiles, furniture, and more recently automobile manufacturing, but the city’s growth has been uneven. East Greensboro is still experiencing the effects of 1960s urban renewal policies, and in recent decades development in East Greensboro has lagged behind the rest of the city.
		</p>

	</div>

	<GraphicSingle
		svg1080={"./greensboro-nc/web-svg/greensboro-grocery-1080.svg"}
		svg720={"./greensboro-nc/web-svg/greensboro-grocery-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-grocery-360.svg"}
	/>

	<div class="text">

		<p>
			The coalition’s work centred on identifying creative ways to increase the number of fresh, affordable food options in East Greensboro, such as grocery stores, community gardens, food co-ops, mobile markets, and culturally relevant food vendors. Investments in healthy food options can take many forms — including public funding, private capital, and philanthropic support — and may help launch or expand businesses that supply fresh produce, improve food infrastructure, or create local food distribution networks. Importantly, any investment must be responsive to the needs and voices of the community. This means prioritizing inclusive development that benefits current residents rather than driving up costs and contributing to displacement. Thoughtful, community-informed investments can create long-term food security while also supporting local jobs and building a more equitable local food system.
		</p>
		<p>
			Ultimately, the emerging coalition designed a multi-faceted strategy to persuade both retailers and the city council to invest in improving community food access. They aimed to demonstrate that strengthening the healthy food environment in East Greensboro could not only meet local needs but also serve as a replicable model for other parts of the city. Their goal was to encourage both traditional market-based solutions and alternative community-based approaches to improving access to healthy foods. At the core of their work was the belief that health and quality of life should not be tied to someone’s home zip code, and that everyone should have choices about where to shop and what to eat. The team also worked with community members in East Greensboro to bring their voices into the planning process so they could participate in development decisions made in their neighbourhood.
		</p>

		<h2>
			Factors influencing access to healthy food
		</h2>

		<p>
			Urban food insecurity is often overlooked due to the sheer abundance and variety of food available in cities, yet access to nutritious, affordable, and culturally appropriate diets remains a challenge for many. While urban areas offer diverse food options, disparities in income, location, and infrastructure create significant barriers to healthy eating.<Footnote id={addFootnote(fns[1])} /> National and local studies across the U.S. show that residents of low-income, minority, and rural neighbourhoods are most often affected by poor access to supermarkets and healthy food.<Footnote id={addFootnote(fns[2])} />
		</p>

		<p>
			The availability of healthy food options is not just a health issue, but also an issue of equity and quality of life. Residents of neighbourhoods with better access to food options, mainly via supermarkets, tend to have healthier diets and lower levels of obesity.<Footnote id={addFootnote(fns[3])} /> They also exhibit lower levels of chronic diseases such as diabetes or cardiovascular disease.<Footnote id={addFootnote(fns[4])} /> Both physical and mental health are affected, with food insecurity strongly associated with worse cognitive function, levels of depression and other symptoms such as fatigue and pain.<Footnote id={addFootnote(fns[5])} />
		</p>

	</div>

	<ImageSingle
		imageURL={groceryImage}
		source="Source: PxHere"
		maxWidth="{720}px"
		link="Yes"
	/>

	<div class="text">

		<p>
			In general, lower-income and minority neighbourhoods tend to have fewer fruit and vegetable markets, bakeries, specialty stores, and natural food stores. In contrast, the availability of liquor stores, fast-food restaurants, and unhealthy foods is greater in these neighbourhoods.<Footnote id={addFootnote(fns[6])} />  Grocery store availability decreases in areas with lower incomes, but even in areas with equal levels of poverty, census tracts with higher percentages of Black residents have fewer supermarkets and consequently less access to healthy food.<Footnote id={addFootnote(fns[7])} />  This food insecurity contributes to disproportionately high rates of diet-related chronic disease among these populations.<Footnote id={addFootnote(fns[8])} />
		</p>

		<p>
			Lack of food access in low-income and minority communities is the result of decades of segregationist policies that have deterred investments from food retailers. A 2015 study of 202 U.S. cities found that neighbourhoods redlined by the Home Owners’ Loan Corporation (HOLC) in the 1930s — typically because they were home to poor or racial minority populations — still have lower access to food today compared to areas that received higher HOLC ratings.<Footnote id={addFootnote(fns[9])} /> 
		</p>

	</div>

	<div class="callout">

		<h2>From food deserts to areas of limited access</h2>

		<p>
			The term “food desert” is a common way to refer to communities with limited access to food, but policy researchers and community organizations today are moving away from the term. In part, this is because the term suggests that the lack of access to food in some communities is a natural occurrence, rather than a result of specific choices made by planners and retailers over time. It also fails to acknowledge that communities may have an abundance of places, such as convenience stores, where healthy food choices could be made available.<Footnote id={addFootnote(fns[10])} /> Perhaps most importantly, the term overlooks the need for systemic change to address racial and economic inequities that persist in American cities.<Footnote id={addFootnote(fns[11])} /> This case study refers to East Greensboro as an area with limited food access, highlighting that this is a spatial issue, but one that is neither enduring nor natural.
		</p>

	</div>

	<div class="text">

		<h2>
			Why local availability matters
		</h2>

		<p>
			Many families in East Greensboro and other cities travel outside of their neighbourhood — and sometimes across town — to access adequate food options. While some shoppers may choose to travel further to shop at specific stores or access culturally relevant foods, many have no choice but to travel long distances for groceries.<Footnote id={addFootnote(fns[12])} /> This often reinforces car-based travel patterns, which is a challenge for those with limited access to a vehicle.<Footnote id={addFootnote(fns[13])} /> Most grocery stores also base their hours on traditional work and commuting schedules, which can restrict access for people with non-conventional schedules, or transit users who may not be able to reach them before they close.<Footnote id={addFootnote(fns[14])} /> Many families also face affordability issues and difficulty finding stores that accept food assistance programs like the Supplemental Nutrition Assistance Program (SNAP). Of the vendors that accept these programs, only a small fraction provide fresh produce.<Footnote id={addFootnote(fns[15])} /> Food delivery apps can fill gaps in accessibility to food options, especially for people with limited vehicle access or mobility issues, but cost may be a barrier for some families.
		</p>
		<p>
			Increasing physical access to local grocery stores and supermarkets is therefore a core strategy to improve access to healthy food in low-income communities like East Greensboro. Grocery stores are routinely considered by community members as one of the most desirable types of retail to have nearby, but they may not be equitably distributed across a city if left to market factors alone.<Footnote id={addFootnote(fns[16])} /> Intentional planning and collaboration between municipal governments and economic development agencies is critical to ensure that food systems are equitable across cities, and that urban populations have reliable access to nutritious food nearby.
		</p>

	</div>

	<ImageSingle
		imageURL={carrotImage}
		source="Source: HippoPx"
		maxWidth="{720}px"
		link="Yes"
	/>

	<div class="text">

		<h2>
			Reframing the data to attract retail options
		</h2>

		<p>
			One approach to generating investment in underserved communities like East Greensboro is to show a map of the existing need for healthy food in the area. These kinds of maps can be useful in highlighting the mismatch between population density and the number of grocery stores. In this case, over 80 percent of stores in the city are located in the western part of the city, with a particularly striking gap in the densely-populated area close to downtown. The relative lack of grocery stores in East Greensboro reflects the significant income disparities in that area, and may contribute to the poorer health outcomes that the community experiences relative to other parts of the city and county. 
		</p>

		<p>
			However, rather than focusing on East Greensboro’s deficits, the team focused on its assets by demonstrating that the area has a significant consumer base, and that now is the time to invest in East Greensboro. For example, East Greensboro has a larger population than the western part of Greensboro and is growing nearly twice as fast, making it attractive for potential retail investment.
		</p>

	</div>

	<GraphicSingle
		svg720={"./greensboro-nc/web-svg/greensboro-pop-growth-chart-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-pop-growth-chart-360.svg"}
	/>

	<div class="text">

		<p>
			The EDDIT team also used a combination of spatial data from OpenStreetMap and anonymized and aggregated cell phone mobility data from Cuebiq to determine the extent to which East Greensboro residents visited different food-related retailers across the Greensboro region in 2022.<Footnote id={addFootnote(fns[17])} /> The resulting map shows that while the most commonly visited stores in the city are within East Greensboro, many East Greensboro residents are also travelling to the western part of the city to buy food, suggesting that there is unmet demand for additional food retailers in East Greensboro. These findings challenge the assumption that low-income neighbourhoods lack the consumer base to support new grocery stores, and the data could be used to attract new investment in the community.
		</p>

	</div>

	<GraphicSingle
		svg1080={"./greensboro-nc/web-svg/greensboro-visits-1080.svg"}
		svg720={"./greensboro-nc/web-svg/greensboro-visits-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-visits-360.svg"}
	/>

	<div class="text">

		<h2>
			Working with existing commercial and civic infrastructure
		</h2>

		<p>
			While bringing new investment to East Greensboro was one of the coalition’s main goals, they are cognizant of the many challenges associated with attracting traditional retailers. New grocery stores in particular are a significant investment with a large footprint, and can take years to come to fruition. To attract new investment, cities often must provide incentives such as financing, reducing the amount of parking required, or lowering real estate taxes.<Footnote id={addFootnote(fns[18])} />
		</p>
		<p>
			However, even with city support, opening a new grocery store is a long and difficult process. One grocery store that was initially approved for construction in East Greensboro in 2019 is still in a much-delayed development process.<Footnote id={addFootnote(fns[19])} /> Forecasting consumer behavior is also complicated: a grocery co-op that opened in East Greensboro in 2016 folded just three years later, in part because many residents were out of the habit of shopping locally from decades of travelling elsewhere, and because the co-op format was unfamiliar.<Footnote id={addFootnote(fns[20])} />
		</p>

		<p>
			An alternative approach is to encourage smaller stores or non-traditional places to provide healthier food options. It may be easier to incorporate a new product line in existing stores than to build new ones, and it makes sense to offer food where people are already shopping or spending time.<Footnote id={addFootnote(fns[21])} /> For example, in recent years a growing number of discount retailers like Dollar Tree and Dollar General — which are disproportionately located in lower-income neighbourhoods — have started accepting food assistance programs like SNAP.<Footnote id={addFootnote(fns[22])} /> Community organizations have worked with these retailers to expand the food offering beyond packaged or frozen food to include more fresh, perishable selections.
		</p>

		<p>
			Another idea the Greensboro coalition proposed is to set up healthy, fresh food in non-food spaces, such as community pop-up markets at churches and other faith-based institutions. This provides an avenue for community organizations and neighbourhood associations to get involved in bringing mobile fresh markets, farmer’s markets, food bank sites, and other community markets to areas with limited existing grocery retail.<Footnote id={addFootnote(fns[23])} /> To illustrate the types of places where this could potentially take place, the team queried spatial data for faith-based institutions from OpenStreetMap, and showed these spaces alongside grocery stores and dollar stores.
		</p>

	</div>

	<GraphicSingle
		svg1080={"./greensboro-nc/web-svg/greensboro-potential-1080.svg"}
		svg720={"./greensboro-nc/web-svg/greensboro-potential-720.svg"}
		svg360={"./greensboro-nc/web-svg/greensboro-potential-360.svg"}
	/>

	<div class="text">

		<p>
			Future projects may even explore creating a larger fresh food network, by sourcing food from local Black farmers. These kinds of programs can strengthen supply chains, contribute to sustainability, and spread the city’s economic growth out to the broader region in an inclusive way.<Footnote id={addFootnote(fns[24])} />
		</p>

		<h2>
			Building a sustainable and robust food ecosystem
		</h2>

		<p>
			Ultimately, building an ecosystem of healthy food options requires long-term investments in housing, infrastructure, and transportation so that residents are able to access places like grocery stores. In the meantime, cities can get creative in expanding food access to places that need it through non-traditional means. Partnerships like the one between the Cone Health Foundation, the City of Greensboro, and East Greensboro NOW can help ensure that food systems are equitable and take a holistic approach to accessibility. By using maps to show the opportunities in East Greensboro, this data story allows them to make an even stronger case for food equity to municipal officials, and ensure the community has a sustainable food system for years to come. 
		</p>

	</div>

	<Footnotes footnotes={footnotes} />

	<div class="details">

		<h2>Additional resources</h2>

		<p>
			<a href="https://blackfarmersindex.com/about-bfi" target="_blank">Black Farmers Index</a>
			<br><br>
			<a href="https://conehealthfoundation.com/" target="_blank">Cone Health Foundation</a>
			<br><br>
			<a href="https://www.eastgreensboronow.com/" target="_blank">East Greensboro NOW</a>
		</p>

	</div>
	

</main>

<Footer/>