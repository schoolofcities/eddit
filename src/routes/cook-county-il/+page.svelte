<script>

	import "../../assets/global-styles.css"

	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/cook-county-title.jpg";

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

	const fns = ['Christopher W. Tessum et al., “PM2.5 polluters disproportionately and systemically affect people of color in the United States,” *Science Advances*, Vol 7, Issue 18 (2021). DOI: 10.1126/sciadv.abf4491.',
		'Bruno Dupeyron, Andrea Noferini and Tony Payan, *Agents and Structures in Cross-Border Governance*, (Toronto: University of Toronto Press, 2023). [URL](https://utppublishing.com/doi/book/10.3138/9781487502881)',
		'J. T. Lyle, *Regenerative Design for Sustainable Development* (United Kingdom: Wiley, 1994).',
		'J. T. Lyle, *Regenerative Design for Sustainable Development*.',
		'Leah V. Gibbons, “Regenerative—The New Sustainable?” *Sustainability*, 12(13), 2020: 5483. [URL](https://doi.org/10.3390/su12135483).',
		'Christopher David Ruiz Cameron, “The rakes of wrath: urban agricultural workers and the struggle against Los Angeles\'s ban on gas-powered leaf blowers,” *U.C. Davis Law Review*, 33(4), 2000: 1087–1104. [URL](https://lawreview.law.ucdavis.edu/archives/33/4/rakes-wrath-urban-agricultural-workers-and-struggle-against-los-angeless-ban-gas); Jules Boykoff, “The Leaf Blower, Capitalism, and the Atomization of Everyday Life,” *Capitalism Nature Socialism*, 22(3), 2011: 95–113. [URL](https://doi.org/10.1080/10455752.2011.593896).',
		'Donald Miller, "Methods for Assessing Environmental Justice in Planning Evaluation – an Approach and an Application," in *New Principles in Planning Evaluation* (London: Routledge, 2008).',
		'Nefeli Maria Bompoti, Nicholas Coelho, and Lauren Pawlowski, “Is inclusive more elusive? An impact assessment analysis on designating environmental justice communities in the US,” *Environmental Impact Assessment Review*, 104 (2024): 107354. [URL](https://doi.org/10.1016/j.eiar.2023.107354).',
		'Abas Shkembi and Richard L. Neitzel, “Historical Redlining and Cumulative Environmental Impacts across the United States,” *Environmental Science & Technology Letters*, Vol 12, Issue 4 (2025). [URL](https://pubs.acs.org/doi/10.1021/acs.estlett.4c01111).',
		'Shkembi and Neitzel, “Historical Redlining.”'
	];

	let title = "Cross-community Approaches to Climate Action: Transitioning to sustainable landscape practices"
	let subTitle = "A case study of Cook County, Illinois"

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


<Password/>

<Title
	title={"Cross-community Approaches to Climate Action: Transitioning to sustainable landscape practices"}
	subtitle={"A case study of Cook County, Illinois"}
	image={titleImage}
	imageCaption={"Landscaper with leaf blower."}
	imageSource={"Photo by Sóc Năng Động."}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='https://www.linkedin.com/in/sarah-a-smith-79089b2a0/' target='_blank'>Sarah A. Smith</a> & <a href='https://www.linkedin.com/in/kathrynexonsmith/' target='_blank'>Kathryn Exon Smith</a>"}
			graphics={"<a href='http://linkedin.com/in/isabeaux-graham/' target='_blank'>Isabeaux Graham</a>, <a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a> & <a href='https://www.linkedin.com/in/julia-greenberg-23114a130/' target='_blank'>Julia Greenberg</a>"}
			date={"September 2025"}
		/>

		<p>
			Climate change affects not only the environment and infrastructure, but also the well-being of individuals. Its impacts cross municipal, regional, and national boundaries, demanding coordinated, cross-jurisdictional action to collaborate and advance climate solutions equitably. In the western suburbs of Chicago, 14 municipalities came together within Cook County to create the Cross Community Climate Collaborative (C4) with the goal of working together on climate action initiatives. One of their signature projects is a campaign that encourages sustainable landscaping practices by supporting the transition to electric equipment like lawn mowers and leaf blowers. The objective is to improve air quality through the reduction of greenhouse gas (GHG) emissions, while also minimizing the adverse health impacts caused by gas-powered technology. 
		</p>

	</div>
	

	<GraphicSingle
		svg720={"./cook-county-il/web-svg/chicago-contextmap-720.svg"}
		svg360={"./cook-county-il/web-svg/chicago-contextmap-360.svg"}
	/>

	<div class="text">

		<p>
			Like many urban regions in the U.S., the Greater Chicago Area faces significant challenges to achieving environmental justice. Lower-income areas and communities of colour have historically been, and continue to be, disproportionately exposed to harmful environmental conditions, including poor air quality and pollution from industry, light-duty vehicles running on gasoline, construction, and heavy-duty diesel vehicles.<Footnote id={addFootnote(fns[0])} /> Policies that enable the transition from gas- to electric-powered lawn equipment have the potential to improve air quality and reduce noise pollution not only for environmental justice communities, but for everyone. 
		</p>
		<p>
			The <a href="https://schoolofcities.github.io/eddit/" target="_blank">EDDIT data storytelling team</a> worked with C4 to build a story that convinces municipal leadership to elevate and collectively organize the transition to sustainable landscaping practices. Through data storytelling, this case study demonstrates how climate mitigation policies can be approached and implemented in an equitable way, with cross-community governance being the catalyst.
		</p>
		<h2>Working together to achieve equitable change</h2>
		<p>
			In an increasingly interconnected world, challenges like climate change transcend traditional political and geographic boundaries. As a result, collective governance has emerged as an essential model for addressing complex issues, allowing municipalities to work together.<Footnote id={addFootnote(fns[1])} /> Unlike the traditional model of siloed local administrations, cross-community governance emphasizes collaboration, mutual accountability, and participatory structures. This governance framework brings together diverse communities across cities, regions, and racial and income lines, to share decision-making power, coordinate actions, and pursue common goals.
		</p>

	</div>

	<GraphicSingle
		svg720={"./cook-county-il/web-svg/cook-county-contextmap-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county-contextmap-360.svg"}
	/>

	<div class="text">

		<p>
			Cross-community governance thrives under conditions where there is a common challenge that transcends individual interests and demands collective action, such as climate action and sustainability. In Cook County, C4 aims to foster this kind of collaboration across municipal borders on climate-related initiatives. The residents in this vast county live in various smaller jurisdictions, but are strongly interconnected as neighbours who share a border and by the people who travel across these borders daily for work.
		</p>

	</div>

	<GraphicSingle
		svg720={"./cook-county-il/web-svg/cook-county_commuters-arches-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county_commuters-arches-360.svg"}
	/>


	<div class="text">

		<p>
			Though interconnected, C4 municipalities are demographically diverse, particularly along income and racial lines. The broad tax base of the C4 jurisdictions means that communities of all income levels can benefit from projects and policies when they are implemented collectively. C4 also aims to foster locally informed policies that are grounded in the lived experiences of all residents in the region. By fostering cooperation between stakeholders with differing capacities and local knowledge, collective governance can enhance resilience, equity, and long-term sustainability by taking action that results in lasting change.  
		</p>

	</div>

	<GraphicMultiples
		svgPaths={["./cook-county-il/web-svg/cook-county_income-map-360.svg", "./cook-county-il/web-svg/cook-county_minorities-map-360.svg"]}
	/>

	<div class="text">
		<h2>Transitioning to sustainable landscape practices </h2>
		<p>
			The C4 initiative has several projects in development, with the overarching goal of making a greener economy. These include building code adjustments for energy savings and limiting single use plastics.<Footnote id={addFootnote(fns[2])} /> They kicked off one of their first campaigns in 2023, focusing on Green Landscape Technology (GLT), which aims to promote a just and equitable transition to sustainable landscaping practices, such as the electrification of landscaping equipment (for example, leaf blowers and lawn mowers), smart irrigation systems, integrated pest management, and planting of native species. GLTs are part of a systematic approach to environmental sustainability based on regeneration and energy efficiency. Regeneration, or what some call “new wave sustainability,” goes beyond simply reducing environmental harm.<Footnote id={addFootnote(fns[3])} /> It calls for a complete shift in how we live, aiming to integrate human activity with natural systems in ways that actively restore and renew the environment.<Footnote id={addFootnote(fns[4])} />
		</p>
		<p>
			Though C4 wants to encourage all sorts of GLT practices throughout the region, they chose to focus on encouraging the transition to electric lawn equipment for this data story because it is underfunded and needs more attention, but could easily be implemented with the proper policies. Municipalities in the United States have already started adopting such practices. Some local governments, mostly in Illinois and California, have <a href="https://pirg.org/edfund/resources/interactive-map-of-lawn-mower-and-leaf-blower-policies/" target="_blank">implemented</a> bans or restrictions on leaf blowers and gas-powered lawn equipment, while others have introduced voluntary incentives for transitioning to electronic equipment.
		</p>
	</div>

	<GraphicSingle
		svg720={"./cook-county-il/web-svg/cook-county_GLT-policy-chart-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county_GLT-policy-chart-360.svg"}
	/>

	<div class="text">
		<p>
			There are often economic and political challenges to implementing these policies, and social and cultural dynamics play a major role in how they are received by the public.<Footnote id={addFootnote(fns[5])} /> For example, some landscape workers in Southern California felt that local efforts to ban gas-powered leaf blowers unjustly targeted the Hispanic population that own and work for many of the landscaping businesses there and would incur the high cost of transitioning to electric equipment. For this reason, it is important that small landscaping businesses are supported financially in the transition phase, through public subsidies or other funding mechanisms.
		</p>
		<p>
			Advocacy efforts should also highlight the long-term health benefits of electric equipment for landscape workers, such as reduced air and noise pollution from cleaner and quieter equipment. The chart below reveals that electric lawn equipment overall produces 25 percent lower dBA than gas-powered equipment and is much less likely to cause hearing loss with long and repeated exposure. Given that 77 percent of landscape workers in Illinois work in the Greater Chicago Area, there are thousands of workers who could potentially benefit from this transition.
		</p>

	</div>

	<GraphicSingle
		svg720={"./cook-county-il/web-svg/cook-county_landscape-contract-stat-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county_landscape-contract-stat-360.svg"}
	/>

	<GraphicSingle
		svg720={"./cook-county-il/web-svg/cook-county_gasvelectric-chart-720.svg"}
		svg360={"./cook-county-il/web-svg/cook-county_gasvelectric-chart-360.svg"}
	/>

	<div class="text">
		<h2>Environmental justice: Creating healthy spaces for all</h2>

		<p>
			Emerging in the 1980s, the concept of <strong>environmental justice</strong> arose from studies that analyzed the correlation between race, income, and environmental risk. These studies found that hazardous facilities (for example, incinerators, sewage treatment plants, and bus depots), were disproportionately located near low-income and minority populations, who were often the least able to remedy the impacts or relocate.<Footnote id={addFootnote(fns[6])} /> This concept has evolved to encompass the idea that all people, regardless of race, income, or background, have the right to live in a clean, healthy, and safe environment, and should be meaningfully involved in environmental policymaking.<Footnote id={addFootnote(fns[7])} />
		</p>
		<p>
			These disproportionate levels of exposure are in part due to the legacies of systematic racism in urban planning, such as redlining. Redlining refers to the Homeowners’ Loan Corporation’s discriminatory practice of designating certain neighbourhoods a high mortgage risk. Facilities like hazardous waste and wastewater discharge sites, as well as infrastructure like highways, were disproportionately built in these “redlined” neighbourhoods.<Footnote id={addFootnote(fns[8])} /> While residential racial segregation was legally banned in the 1960s, these land use patterns persisted in racialized and low-income neighbourhoods for decades. Today, neighbourhoods that were historically redlined are associated with nearly 50 percent higher levels of air pollution compared to areas that were designated as “desirable” areas for financial investment.<Footnote id={addFootnote(fns[9])} />
		</p>
		<p>
			In Illinois, the state is making efforts to protect the environment and the health of all its residents. For example, the Illinois Environmental Protection Agency has an <a href="https://epa.illinois.gov/topics/environmental-justice/ej-policy.html" target="_blank">Environmental Justice Policy</a> which enables the agency to address concerns and promote environmental equity. Similarly, state programs such as <a href="https://www.illinoissfa.com/environmental-justice-communities/" target="_blank">Illinois Solar for All</a> have dedicated a quarter of their budget to administer solar projects in Environmental Justice Communities (EJCs). EJCs have been designated and <a href="https://www.illinoissfa.com/environmental-justice-communities-map/" target="_blank">mapped</a> by this program as areas which face a greater risk of pollution exposure due to a combination of environmental and socioeconomic factors.
		</p>
		<p>
			Ensuring that collective governance strategies are equitable requires identifying and prioritizing these areas that are disproportionately affected by environmental hazards. The map below, which shows environmental justice communities in blue, reveals that all C4 jurisdictions contain areas that are particularly vulnerable to environmental hazards, and highlights the widespread need for climate change mitigation policies.
		</p>

	</div>

	<GraphicSingle
		svg360={"./cook-county-il/web-svg/cook-county_ejc-map-360.svg"}
	/>

	<div class="text">

		<p>
			While there are environmental justice communities in all C4 jurisdictions, neighbourhoods with more low-income and non-white residents such as Maywood, Bellwood, Broadview, and Hillside, tend to experience higher levels of pollution and poorer air quality. The maps below show the prevalence of fine particulate matter (PM<sub>2.5</sub>) and nitrogen dioxide (NO<sub>2</sub>), harmful air pollutants created by burning fossil fuels, including by using gas-powered vehicles and equipment. PM<sub>2.5</sub> consists of extremely small particles that can penetrate deep into the lungs and even enter the bloodstream, contributing to serious health problems like asthma and heart disease. NO<sub>2</sub> can irritate the lungs, worsen respiratory conditions, and increase the risk of infections, especially in children.
		</p>
		<p>
			Using gas-powered landscaping equipment releases more of these pollutants into the air, worsening health conditions like asthma among residents who live nearby. The maps below show that there is a significant amount of overlap between areas with higher rates of asthma and environmental justice communities, highlighting the urgent need for policies that mitigate environmental harm, particularly in these areas.
		</p>

	</div>

	<GraphicMultiples
		svgPaths={[
			"./cook-county-il/web-svg/cook-county_PM25-pollution-map-360.svg",
			"./cook-county-il/web-svg/cook-county_NO2-map-360.svg",  
			"./cook-county-il/web-svg/cook-county_asthma-map-360.svg"
		]}
	/>

	<div class="text">
		<h2>Tackling climate change together</h2>

		<p>
			The C4 initiative represents a promising model for how cross-community governance can address the intertwined challenges of climate change, equity, and environmental justice. By representing 14 interconnected municipalities through data, this story demonstrates how collaborative policymaking can work to mitigate climate change and its effects on residents. This case study uses maps of environmental justice communities to show how these policies can be approached and implemented in an equitable way. Climate change will continue to affect all communities, but C4’s approach offers a vital example of how collective action rooted in justice can create a healthier, more sustainable future for all.
		</p>

		<div class="details">
			<p>
				<i>The authors would like to thank Karen Chapple, Michelle Zhang, Julia Greenberg, and Evelyne St-Louis for their contributions to editing and informing this case study.</i>
			</p>
		</div>

		<Footnotes footnotes={footnotes} />

		<div class="details">

			<h2>Additional resources</h2>

			<p>
				<a href="https://sga-staging.cloudaccess.host/wp-content/uploads/2025/06/C4-Guidebook-1.pdf" target="_blank">C4 Guidebook</a>
				<br><br>
				<a href="https://www.illinoissfa.com/environmental-justice-communities-map/" target="_blank">Environmental Justice Communities Map</a>
				<br><br>
				<a href="https://experience.arcgis.com/experience/aa364c77db684dfa92afa5094b69f6ff" target="_blank">Illinois EPA EJ Start Map</a>
				<br><br>
				<a href="https://epa.illinois.gov/topics/environmental-justice/ej-policy.html" target="_blank">Illinois EPA - Environmental Justice (EJ) Policy</a>
				<br><br>
				<a href="https://pirg.org/edfund/resources/interactive-map-of-lawn-mower-and-leaf-blower-policies/" target="_blank">Interactive map of lawn mower and leaf blower policies in the United States</a>
			</p>

		</div>

	</div>


</main>

<Footer/>