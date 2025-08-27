<script>

	import "../../assets/global-styles.css"

	import Password from "$lib/Password.svelte";
	import Title from '$lib/Title.svelte';
	import AuthorDate from "$lib/AuthorDate.svelte";
	import Footer from "$lib/Footer.svelte";
	import GraphicSingle from "$lib/GraphicSingle.svelte";
	import GraphicMultiples from "$lib/GraphicMultiples.svelte";
	import ImageSingle from "$lib/ImageSingle.svelte";

	import titleImage from "./assets/abq-title.jpg";

	import Footnote from '$lib/Footnote.svelte';
    import Footnotes from '$lib/Footnotes.svelte';
    import { createFootnoteStore } from '$lib/footnoteUtils';

	const footnoteStore = createFootnoteStore();
    const { footnotes, addFootnote } = footnoteStore;

    const fns = ['Victor Westphall, "Albuquerque in the 1870s," *New Mexico Historical Review* 23, no. 4 (1948), [URL](https://digitalrepository.unm.edu/cgi/viewcontent.cgi?article=1634&&context=nmhr&&sei-redir=1&referer=https%253A%252F%252Fscholar.google.com%252Fscholar%253Fhl%253Den%2526as_sdt%253D0%25252C5%2526q%253DVictor%252BWestphall%25252C%252B%252522Albuquerque%252Bin%252Bthe%252B1870s%2526btnG%253D#search=%22Victor%20Westphall%2C%20Albuquerque%201870s%22); Chris Wilson, *The Historic Railroad Buildings of Albuquerque: An Assessment of Significance* (1986), [URL](https://documents.cabq.gov/planning/historic-preservation/Wilson%20RR%20Bldg%20Assessm%201986.PDF)',
		'Arianne Carvalhedo Reis and Carla Jellum, “Rail Trail Development: A Conceptual Model for Sustainable Tourism,” *Tourism Planning & Development* 9 (2): 133–47 (2012), [URL](https://doi.org/10.1080/21568316.2011.630748).',
		'J.M. Bowker, John Bergstrom, and Joshua Gill, “Estimating the Economic Value and Impacts of Recreational Trails: A Case Study of the Virginia Creeper Rail Trail,” *Tourism Economics* 13 (2), 2007: 241–260, [URL](https://journals.sagepub.com/doi/abs/10.5367/000000007780823203).',
		'Pascal Scherrer et al., “Rail Trails Literature: Current Status and Future Research,” *Journal of Leisure Research* 52, no. 1 (2021): 97–119, [URL](https://doi.org/10.1080/00222216.2020.1746937).',
		'Aaron Suiter, “Second Wave Rail-to-Trail Initiatives and Ecological Gentrification: Lessons from New York City’s High Line and Atlanta’s Beltline,” *Undergraduate Journal of Humanistic Studies* 2 (January 2016).',
		'Jessica Majors and Sue Burow, *Assessment of the Impact of the Indianapolis Cultural Trail: A Legacy of Gene and Marilyn Glick* (Indiana University Public Policy Institute, 2015), [URL](https://archives.indianapolis.iu.edu/server/api/core/bitstreams/e2424f48-5496-420c-979e-4c91b85370fb/content).',
		'Steve Nivin, *Impact of the San Antonio River Walk* (2014); Andrea Drusch et al., “The River Walk Transformed San Antonio. Could Panther Island Do the Same for Fort Worth?,” *San Antonio Report*, July 9, 2023, [URL](https://sanantonioreport.org/san-antonio-river-walk-fort-worth-panther-island-economic-development-floods/).',
		'Yvette Hammett Hull, “Atlanta’s Beltline Becomes Crucial Part of Economic Uplift, Promoter of Green Space,” *Playmakers*, December 5, 2024, [URL](https://communityplaymaker.com/discoveries/atlantas-beltline-becomes-crucial-part-of-economic-uplift-promoter-of-green-space/).',
		'Christopher Coutts and Rebecca Miles, "Greenways as Green Magnets: The Relationship Between the Race of Greenway Users and Race in Proximal Neighborhoods," *Journal of Leisure Research* 43, no. 3 (2011): 317–333, [URL](https://www.tandfonline.com/doi/abs/10.1080/00222216.2011.11950239).',
		'Kevin Loughran, “Parks for Profit: The High Line, Growth Machines, and the Uneven Development of Urban Public Spaces,” *City & Community* 13, no. 1 (2013), [URL](https://journals.sagepub.com/doi/abs/10.1111/cico.12050); Jeremy Williams, “Fear and Loathing on the High Line: Notes from the Spatial Frontline of Spectacle Techno-Capitalism,” in *Contours of the Illiberal State: Governing Circulation in the Smart Economy*, ed. Boris Vormann and Christian Lammert (Campus Verlag, 2019), [URL](https://www.gbv.de/dms/zbw/1040154778.pdf).',
		'Dan Immergluck, “Atlanta’s BeltLine Shows How Urban Parks Can Drive ‘Green Gentrification’ If Cities Don’t Think about Affordable Housing at the Start,” *The Conversation*, January 25, 2023, [URL](http://theconversation.com/atlantas-beltline-shows-how-urban-parks-can-drive-green-gentrification-if-cities-dont-think-about-affordable-housing-at-the-start-193204); Dan Immergluck and Tharunya Balan, “Sustainable for Whom? Green Urban Development, Environmental Gentrification, and the Atlanta Beltline,” *Urban Geography* (August 4, 2017), 1–17, [URL](https://doi.org/10.1080/02723638.2017.1360041).',
		'Greg Lindsey et al., “Neighborhood Change and Gentrification Near Three Urban Trails,” *Findings Press*, October 22, 2021, [URL](https://doi.org/10.32866/001c.29521); *Business North Carolina*, “How Charlotte’s South End Got So Hot,” November 1, 2019, [URL](https://businessnc.com/how-charlottes-south-end-got-so-hot/).',
		'Karen Chapple and Miriam Zuk, “Forewarned: The Use of Neighborhood Early Warning Systems for Gentrification and Displacement,” *Cityscape: A Journal of Policy Development and Research* 18, no. 3 (2016).',
		'Aggregated mobility data are provided by Cuebiq, a location intelligence platform. Data is collected from anonymized users who have opted-in to provide access to their location data anonymously, through a CCPA and GDPR-compliant framework. Through its Social Impact program, Cuebiq provides mobility insights for academic research and humanitarian initiatives. The Cuebiq responsible data sharing framework enables research partners to query anonymized and privacy enhanced data, by providing access to an auditable, on-premise Data Cleanroom environment. All final outputs provided to partners are aggregated in order to preserve privacy.',
		'Albuquerque Vision Zero, *Year in Review* (2023), [URL](https://www.cabq.gov/municipaldevelopment/documents/albuquerque-vision-zero-year-in-review-2023-_final.pdf); *Consumer Affairs*, “Most Dangerous Cities for Pedestrians and Cyclists [2025],” July 22, 2025, [URL](https://www.consumeraffairs.com/automotive/most-dangerous-cities-for-pedestrians-and-cyclists.html); National Safety Council, “Motor-Vehicle Deaths by State (2023),” accessed August 4, 2025, [URL](https://injuryfacts.nsc.org/state-data/motor-vehicle-deaths-by-state/).',
		'Min Jiao et al., “Optimizing the Shade Potential of Trees by Accounting for Landscape Context,” *Sustainable Cities and Society* 70 (July 1, 2021): 102905, [URL](https://doi.org/10.1016/j.scs.2021.102905).',
		'Karen Chapple and Miriam Zuk, “Forewarned.”',
		'Laura Bliss, “The High Line’s Biggest Issue—And How Its Creators Are Learning From Their Mistakes,” *Bloomberg.com*, February 7, 2017, [URL](https://www.bloomberg.com/news/articles/2017-02-07/the-high-line-and-equity-in-adaptive-reuse).',
		'Metra Sheshbaradaran, “Rail to Trail & Green Gentrification” (2024), [URL](https://storymaps.arcgis.com/stories/78fb72ee7e8a45bdae2eb685e21385e8).'
   	];

</script>


<Password/>

<Title
	title={"From Tracks to Trail: Planning for equitable (re)development"}
	subtitle={"A case study of Albuquerque, New Mexico"}
	image={titleImage}
	imageCaption={"Underused rail spur in Albuquerque."}
	imageSource={"Photo by Jeff Allen, August 2023."}
/>

<main>

	<div class="text">

		<AuthorDate
			writing={"<a href='https://www.linkedin.com/in/kathrynexonsmith/' target='_blank'>Kathryn Exon Smith</a> & <a href='https://www.linkedin.com/in/sarah-a-smith-79089b2a0/' target='_blank'>Sarah A. Smith</a>"}
			graphics={"<a href='https://jamaps.github.io/' target='_blank'>Jeff Allen</a>, <a href='https://www.linkedin.com/in/remus-herteg-150402235/' target='_blank'>Remus Herteg</a>, & <a href='' target='_blank'>Isabeaux Graham</a>"}
			date={"August 2025"}
		/>

		<p>
			Dormant and underused infrastructure represents both a challenge and an opportunity for cities. Vacant lots, aging transit corridors, and decommissioned industrial sites can be redeveloped to create vibrant and popular spaces that reflect and serve local communities. However, economic changes brought about by infrastructure redevelopment projects can lead to gentrification, which has prompted demands for more anti-displacement protections for nearby residents.
		</p>
		<p>
			In the city of Albuquerque, New Mexico, plans are underway to transform a former rail corridor running through the downtown into an 11-kilometre (7-mile) multi-use urban trail that will connect downtown neighbourhoods, businesses, and cultural sites. The city’s <a href="https://www.cabq.gov/mra" target="_blank">Metropolitan Redevelopment Agency</a> is leading the effort to fundraise and mobilize the community around this social infrastructure investment and ensure that the development of the trail is beneficial, not detrimental, for nearby residents. The agency worked with the <a href="https://schoolofcities.github.io/eddit/" target="_blank">EDDIT team</a> to create a data story about the benefits of the Rail Trail as a social investment that can enhance rather than displace the surrounding communities.
		</p>

	</div>

	<GraphicSingle
		svg360={"./albuquerque-nm/web-svg/abq-contextmap-360.svg"}
		svg720={"./albuquerque-nm/web-svg/abq-contextmap-720.svg"}
	/>

	<div class="text">

		<h2>A growing trend of adaptive reuse</h2>

		<p>
			Railroads have played a significant role in the historical development of many North American cities, moving people and goods in and out of the downtown core and contributing to their growth. In Albuquerque in the late 19th century, the Santa Fe Railway company built and maintained a number of freight and passenger corridors through the city. As the company grew, they added a complex of railway maintenance shops in the Barelas neighbourhood near downtown, which became the largest industrial site in the state and the city’s largest employer.<Footnote id={addFootnote(fns[0])} />
		</p>
		<p>
			Over time, as road transportation increased, many rail corridors across the country fell out of use, and the lands surrounding them became vacant. Today, cities like Albuquerque are considering how these rail tracks and adjacent lands can be repurposed for the public good. The tracks’ central location makes them ideally situated to become green spaces or cultural trails, which will breathe new life into former industrial parcels.<Footnote id={addFootnote(fns[1])} /> Attracting foot traffic to these areas has the potential to drive economic development, as visitors support the growth of local businesses like shops, cafés, and restaurants, which generates positive spillover effects for the surrounding area.<Footnote id={addFootnote(fns[2])} /> Reviving vacant and underused spaces can strengthen the downtown economy, broaden the municipal tax base, and contribute to a more vibrant, livable urban centre.<Footnote id={addFootnote(fns[3])} />
		</p>
		<p>
			One of the most famous examples of this kind of adaptive infrastructure reuse is New York City’s High Line, which turned an abandoned elevated rail line in the Chelsea neighbourhood of Manhattan into a 2.3-kilometre (1.4-mile) linear park. Since it opened in 2009, the High Line has become one of the city’s top attractions, with an estimated 8 million visitors each year, and it has spawned a wave of new development in the surrounding area. Property values nearby increased by over 100 percent in the first decade after the project’s announcement.<Footnote id={addFootnote(fns[4])} />
		</p>

		<h3>
			Economic impact of selected linear parks in the United States
		</h3>
		
		<p>
			Linear parks and urban greenways in other cities have seen similar economic benefits. The Indianapolis Cultural Trail in Indiana increased nearby property values by a combined US$1 billion in its first five years and expanded the customer base of businesses along its route, creating new employment opportunities for residents.<Footnote id={addFootnote(fns[5])} /> San Antonio, Texas redeveloped its riverfront over a period of several decades, with a major expansion in 2011 that added 24 kilometres (15 miles) of hiking and biking trails and a series of art installations and public spaces along the river’s downtown stretch. It has become a major attraction for locals and tourists alike, drawing tens of millions of visitors annually and generating billions of dollars in economic activity.<Footnote id={addFootnote(fns[6])} /> The Atlanta Beltline, a 35-kilometre (22-mile) loop trail in Georgia that transformed old rail infrastructure encircling the city into new green spaces, has created an estimated US$9 billion in economic impacts for the city as of 2023, and has spurred new investments in transit and affordable housing.<Footnote id={addFootnote(fns[7])} /> There is great potential for these projects to fulfill both economic and equity objectives by serving as connective tissue for communities, spaces for recreation in dense downtowns, and platforms for additional public and private investment.<Footnote id={addFootnote(fns[8])} /> 
		</p>

		

	</div>

	<GraphicMultiples
		svgPaths={[
			"./albuquerque-nm/web-svg/abq-example-indy-360.svg", 
			"./albuquerque-nm/web-svg/abq-example-sanantonio-360.svg", 
			"./albuquerque-nm/web-svg/abq-example-charlotte-360.svg",
			"./albuquerque-nm/web-svg/abq-example-atlanta-360.svg"
		]}
	/>

	<div class="text">

		<p>
			However, these kinds of redevelopment projects can have unforeseen consequences, as well-intentioned new amenities may not properly serve the existing community and may even lead to displacement as the surrounding neighbourhood changes. The High Line, for example, began as a grassroots initiative but instigated a period of rapid redevelopment in the Chelsea neighbourhood. Luxury condos and upscale businesses catering to affluent tourists replaced local establishments and older housing stock, pushing out existing residents. Many locals, particularly people of colour, felt unwelcome in the space due to increased surveillance and restrictive public-private management.<Footnote id={addFootnote(fns[9])} /> Similarly, as the Atlanta Beltline trail triggered sharp rises in property values and rents along its corridor, some lower-income residents were priced out and forced to relocate further from the city centre.<Footnote id={addFootnote(fns[10])} /> While gentrification of neighbourhoods near linear parks and other green spaces is not universal, it is a contributing factor to rapid neighbourhood change, particularly in cities with existing housing pressures and strong population growth, or where new trails are located near downtown or transit.<Footnote id={addFootnote(fns[11])} /> 
		</p>

		<div class="callout">
			<h2>Gentrification and displacement</h2>
			<p>
				The terms gentrification and displacement are often used interchangeably, but have distinct meanings. <strong>Gentrification</strong> refers to an influx of new capital, usually in the form of real estate investment, and new higher-income or higher-educated residents. Often the new residents are moving from outside of the neighbourhood or city, are of a different race or ethnicity, and have different family compositions, consumer preferences, and social infrastructure needs. Gentrification can in turn lead to <strong>displacement</strong>, when existing residents are forced to leave the neighbourhood — but displacement can also precede gentrification, or the two can occur simultaneously. An ongoing challenge for advocates of equitable development is how to balance improving neighbourhood amenities by creating more access to thriving main streets, public transit, bike paths, or recreational spaces while keeping these communities affordable for all kinds of residents as they become more in-demand.<Footnote id={addFootnote(fns[12])} />
			</p>
		</div>

		<h2>Increasing local connections in Albuquerque</h2>
		<p>
			The trail development team in Albuquerque is well aware of the potential for displacement along the trail and has centred equitable development in their plans. Working with the EDDIT data storytelling team, they wanted to proactively communicate to city leadership and the public that the trail is an opportunity to improve connectivity around downtown and provide more community spaces for residents, while also creating economic opportunity.
		</p>
		<p>
			Reflecting the common concern that public infrastructure improvements like Rail Trails are primarily for tourists, the team emphasized how the trail would expand locals’ sense of community. Murals and art along the trail will connect residents to their cultural history and provide public spaces to gather and linger, contributing to a more vibrant downtown. More downtown activation can also create new economic opportunities that may help to prevent locals from relocating to faster-growing regions, preserving generational knowledge and networks in the city.
		</p>
		<p>
			The data storytelling team worked to highlight the extent to which downtown is already a place well used by Burqueños, and that new green space there would serve residents. The graph below, which uses anonymized and aggregated cell phone mobility data from Cuebiq, shows that in 2022, nearly 80 percent of average daily activity downtown was from visitors who live in the Albuquerque metropolitan area (Bernalillo County), and 22 percent of downtown activity was generated by residents who live downtown.<Footnote id={addFootnote(fns[13])} /> The new trail has the potential create even more activity from the growth of new businesses, creating an environment that both residents and visitors can enjoy.
		</p>

	</div>

	<GraphicSingle
		svg360={"./albuquerque-nm/web-svg/abq-visitor-chart-360.svg"}
		svg720={"./albuquerque-nm/web-svg/abq-visitor-chart-720.svg"}
	/>

	<div class="text">

		<p>
			The trail will also improve connectivity throughout the downtown area, allowing both residents and tourists safer and more efficient access to key destinations. Connectivity also enables existing residents to benefit from improved access to jobs, services, and community spaces. The data storytelling team emphasized how the trail has the potential to reconnect parts of the community that have long been cut off from each other by active freight rail lines, highways, and other dividing infrastructure. They created a map showing how the Rail Trail will add to existing infrastructure to form a loop around some of downtown’s major destinations, including the Old Town, central train station, zoo, and National Hispanic Cultural Center. The trail connects a variety of historic and diverse communities, and links many popular businesses, including the Rail Yards Market and the Old Town Ice Cream Parlor.
		</p>
	</div>

	<GraphicSingle
		svg360={"./albuquerque-nm/web-svg/abq-trailmap-360.svg"}
		svg720={"./albuquerque-nm/web-svg/abq-trailmap-720.svg"}
		svg1080={"./albuquerque-nm/web-svg/abq-trailmap-1080.svg"}
	/>

	<div class="text">

		<h2>Creating safer public spaces</h2>

		<p>
			Like many cities in the U.S., Albuquerque is car-oriented, with wide, busy roads and unsafe crossings. Between 2016 and 2020, Albuquerque had the second-highest number of pedestrian fatalities per capita in the nation, and the city is regularly considered by non-profits such as the National Safety Council and Vision Zero to be the most dangerous in America for these vulnerable road users.<Footnote id={addFootnote(fns[14])} /> The dedicated pedestrian and cycle trail should improve safety by creating a protected route for people to travel through the city. The team highlights the potential benefits of the multi-use trail with a map illustrating pedestrian and cyclist injuries and fatalities involving motor vehicles downtown. A dedicated trail is a safer and more pleasant alternative to the existing infrastructure, one that incorporates grade-separated lanes, wider sidewalks, and more lighting. It is also greener, as <a href="https://schoolofcities.github.io/eddit/bridgeport-ct" target="_blank">tree cover</a> reduces heat in urban areas and encourages outdoor activity, improving the overall health of the community.<Footnote id={addFootnote(fns[15])} /> 
		</p>

	</div>

	<GraphicSingle
		svg360={"./albuquerque-nm/web-svg/abq-hfin-360.svg"}
		svg720={"./albuquerque-nm/web-svg/abq-hfin-720.svg"}
	/>


	<div class="text">

		<h2>Empowering the community with data</h2>

		<p>
			Emphasizing the benefits of developing new social infrastructure like parks and Rail Trails is important because the long-term success of the multi-use trail project depends on community support. If Albuquerque residents see the value of the project, they will be more likely to use the trail, visit nearby local businesses, and advocate for it politically. To address community concerns around gentrification and displacement, the Albuquerque team has developed metrics to monitor neighbourhood change in the surrounding areas. Research suggests that “early warning systems” tracking investment, disinvestment, and population changes at a small scale are a useful tool for democratizing data, and help communities advocate for policies that protect them against displacement.<Footnote id={addFootnote(fns[16])} /> By tracking various housing and community well-being metrics over time in neighbourhoods adjoining the planned Rail Trail development, the Albuquerque team can work with the community to build trust and support for the project, stay accountable to the public, and ensure that new development benefits everyone.
		</p>
		<p>
			Common neighbourhood characteristics that signal gentrification risk include rising home sale prices, proximity to areas with higher housing costs, good transit access, historic architecture, and large housing units. In neighbourhoods at risk of gentrification, it is especially important to monitor changes in property values, rents, tenure, and demographics with a dashboard or other data tool. Doing so can alert local leaders to the need for targeted anti-displacement policies, such as the preservation of existing affordable units and robust incentives to develop housing across a spectrum of price points. Additional policies include community benefits agreements that include residents in the construction or operations of infrastructure projects, which ensure the local community benefits financially.<Footnote id={addFootnote(fns[17])} /> Data dashboards are one way to show the need for these policies and direct municipal leaders to where they can be most effective. 
		</p>
		<p>
			To understand existing conditions in neighbourhoods surrounding the proposed Rail Trail development, the EDDIT team mapped demographic characteristics in nearby census block groups. Another best practice is to identify and map vacant parcels in the area that could be used to construct new housing, both affordable and market rate, as a way to support community organizing for equitable infrastructure development.<Footnote id={addFootnote(fns[18])} /> These maps form an important baseline for analyzing future changes, and can help to build trust in the government or other organizations developing linear parks. 
		</p>

	</div>

	<GraphicMultiples
		svgPaths={[
			"./albuquerque-nm/web-svg/abq-income-360.svg", 
			"./albuquerque-nm/web-svg/abq-rent-360.svg",
			"./albuquerque-nm/web-svg/abq-hispanic-360.svg"
		]}
	/>

	<div class="text">

		<p>
			Urban adaptive reuse initiatives are often described as having both environmental and social benefits, but planners and community members must take care to ensure that they do not induce speculation, exclusion, and displacement. With proactive policies that ensure affordability, protect existing communities, and foster inclusive civic life, recreational infrastructure can be a benefit, rather than deepening socioeconomic inequality. Albuquerque’s data story shows the potential for the Rail Trail — and the democratization of data that accompanies its development — to connect communities safely, expand economic opportunity, elevate the city’s culture and history, and increase transparency, while giving community members the tools to ensure these opportunities benefit all of the city’s residents.
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
				<a href="https://www.cabq.gov/mra/rail-trail" target="_blank">Albuquerque Rail Trail</a>
			</p>

		</div>

	</div>

</main>

<Footer/>